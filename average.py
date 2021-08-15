import pandas as pd
import random
import statistics
import plotly.figure_factory as ff
import csv
import plotly.graph_objects as go

df = pd.read_csv("class110/newdata.csv")
average = df["average"].tolist()
mean = statistics.mean(average)
standardDeviation = statistics.stdev(average)

# print("Mean:",mean)
# print("Standard Deviation:",standardDeviation)

dataSet = []

for i in range(0,100):
    index = random.randint(0,len(average))
    value=average[index]
    dataSet.append(value)

mean = statistics.mean(dataSet)
standardDeviation = statistics.stdev(dataSet)

print("Mean:", mean)
print("Standard Deviation:",standardDeviation)

def random_setOf_mean(counter):
    dataSet=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(average))
        value=average[random_index]
        dataSet.append(value)

    mean = statistics.mean(dataSet)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["Average"], show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        setOfMeans = random_setOf_mean(100)
        mean_list.append(setOfMeans)
    
    show_fig(mean_list)

setup()


