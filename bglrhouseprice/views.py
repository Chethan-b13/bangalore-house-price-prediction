from django.shortcuts import render
import numpy as np
import pickle
import json

def get_colum_names():
    with open('columns.json','r') as f:
        data_columns  = json.load(f)['data_columns']
    return data_columns

def get_estimated_price(location,sqft,bath,bhk):
    data_columns = get_colum_names()
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1
    X = np.zeros(len(data_columns))
    X[0] = sqft
    X[1] = bath
    X[2] = bhk
    if loc_index >=0:
        X[loc_index] = 1

    with open('banglore_home_price_model.pickle','rb') as f:
            lr = pickle.load(f)

    return np.round(lr.predict([X])[0],2)

def Home(request):
    locations = get_colum_names()[3:]
    return render(request,'index.html',{'locations':locations})

def Estimate(request):
    if request.method == 'POST':

        sqft = request.POST['area_ft']
        bathrooms = request.POST['bathroom']
        bhk = request.POST['bhk']
        location = request.POST['area']
        price = get_estimated_price(location,sqft,bathrooms,bhk)

        return render(request,'estimate.html',{'price':price})