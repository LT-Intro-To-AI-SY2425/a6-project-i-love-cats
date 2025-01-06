import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data=pd.read_csv("AirQualityUCI.csv", sep=";")
print(data)
x = data["C6H6(GT)"]
y = [data["Date"],data["Time"]]
print(x,y)