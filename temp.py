import plotly.figure_factory as ff
import pandas as pd
import statistics
import csv
import random
import plotly.graph_objects as go

df = pd.read_csv("class110/data.csv")
data = df["temp"].tolist()
mean = statistics.mean(data)
standardDeviation = statistics.stdev(data)

# fig = ff.create_distplot([data], ["Temp"], show_hist=False)
# fig.add_trace(go.Scatter(x=[mean,mean], y=[0,1], mode="lines", name="MEAN"))
# fig.show()

print("Mean1 :", mean)
print("Standard Deviation1 :", standardDeviation)

dataSet=[]
for i in range(0,100):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    dataSet.append(value)


mean2 = statistics.mean(dataSet)
standardDeviation2 = statistics.stdev(dataSet)

# print("Mean :", mean2)
# print("Standard Deviation :", standardDeviation2)

def random_setOf_mean(counter):
    dataSet=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataSet.append(value)

    mean = statistics.mean(dataSet)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        setOfMeans = random_setOf_mean(100)
        mean_list.append(setOfMeans)
    
    show_fig(mean_list)

setup()
