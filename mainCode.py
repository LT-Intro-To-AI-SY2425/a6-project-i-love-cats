import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data=pd.read_csv("AirQualityUCI.csv", sep=";")
#print(data)
x = data["Date"]
y = data["NO2(GT)"]
years=[]
days=[[],[],[],[],[],[],[],[],[],[],[],[],[]]
xSplit=[]
NO2=[[],[],[],[],[],[],[],[],[],[],[],[],[]]
colors=["c",'g','b','r','m','y']

for i in range(len(x)):
    xSplit.append(x[i].split("/"))

fig, graph = plt.subplots(4)

for m in range(1,13):
    for i in range(len(xSplit)):
        #print(data["Time"][i],ySplit[i][1])
        if data["Time"][i]=="04.00.00" and int(xSplit[i][1])==m and data["NO2(GT)"][i]!=-200:
            NO2[m].append(y[i])
            days[m].append(int(xSplit[i][0]))
    
    x=days
    y=NO2
    np.array(x)
    np.array(y)
    #x.reshape[-1,1]
    #y.reshape[-1,1]
    print(x)
    print(y)

# GRAPHING FOR WINTER MONTHS
    if m==12:
        print("m12")
        model = LinearRegression().fit(x[m], y[m])
        coef = round(float(model.coef_[0]), 2)
        intercept = round(float(model.intercept_), 2)
        r_squared = model.score(x[m], y[m])
        plt.plot(x[m], coef*x[m] + intercept, c=colors[m], label=m-12)
        graph[0].scatter(x[m],y[m],c=colors[m-12])

    if m<3:
        print("m3")
        model = LinearRegression().fit(x[m], y[m])
        coef = round(float(model.coef_[0]), 2)
        intercept = round(float(model.intercept_), 2)
        r_squared = model.score(x[m], y[m])
        plt.plot(x[m], coef*x[m] + intercept, c=colors[m], label=m-12)
        graph[0].scatter(x[m],y[m],c=colors[m])
        
#GRAPHING FOR SPRING MONTHS
    if 2<m<6:
        print("m")
        graph[1].scatter(x[m],y[m],c=colors[m-3])

#GRAPHING FOR SUMMER MONTHS
    if 5<m<9:
        print("m")
        graph[2].scatter(x[m],y[m],c=colors[m-6])

#GRAPHING FOR FALL MONTHS
    if 8<m<12:
        print("m")
        graph[3].scatter(x[m],y[m],c=colors[m-9])

    for i in range(4):
        graph[i].set_xlabel("Day")
        graph[i].set_ylabel("y(ppm)")

#print(x)
plt.show()




