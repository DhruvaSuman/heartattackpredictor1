from django.shortcuts import render,HttpResponse
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import sklearn.ensemble._forest 
# Create your views here.
def index(request):
    return render(request,'index.html')
def predict(request):
    from_joblib = joblib.load("./models/Heart.pkl")
   
    if request.method=="POST":
        age=request.POST.get('age')
        sex=request.POST.get('gender')
        cp=request.POST.get('cp')
        trestbps=request.POST.get('rbp')
        chol=request.POST.get('cl')
        fbs=request.POST.get('fbs')
        restecg=request.POST.get('recg')	
        thalach=request.POST.get('thalach')
        exang=request.POST.get('exang')
        oldpeak=request.POST.get('oldpeak')
        slope=request.POST.get('slp')
        ca=request.POST.get('ca')
        thal=request.POST.get('thal')
        temp={"age":age,"sex":sex,"cp":cp,"trestbps":trestbps,"chol":chol,"fbs":fbs,"restecg":restecg,"thalach":thalach,"exang":exang,"oldpeak":oldpeak,"slope":slope,"ca":ca,"thal":thal}
    testdata = pd.DataFrame(temp,index=[0])
    t=from_joblib.predict(testdata)[0]
    # target : 0= high chance of heart attack 1= less chance of heart attack
    if t==0:
        params={"t":t,"y":temp,"h":"heart attack"}
        return render(request,'predict.html',params)
    else:
        params={"t":t,"y":temp,"h":None}
        return render(request,'predict.html',params)
    