import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random 
import pandas as pd
import csv 
df =pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()
fig= ff.create_distplot([data], ["Math Scores"], show_hist=False)
# fig.show()
mean = st.mean(data)
sd = st.stdev(data)
print("mean of the data is: ", mean)
print("Standard deviation of the data is: ", sd)
def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        randomindex = random.randint(0,len(data)-1)
        value= data[randomindex]
        dataset.append(value)
    mean=st.mean(dataset)
    return mean
meanList=[]
for i in range (0,1000):
    set_of_means = random_set_of_mean(100)
    meanList.append(set_of_means)
sd=st.stdev(meanList)
mean=st.mean(meanList)
print("mean of the data is: ", mean)
print("Standard deviation of the data is: ", sd)
fig= ff.create_distplot([meanList], ["Math Scores"], show_hist=False)
# fig.show()
df1=pd.read_csv('data1.csv')
data1=df1["Math_score"]. tolist()
mean1 = st.mean(data1)
sd1= st.stdev(data1)
zScore1= (mean1 - mean)/sd
print(zScore1)

df2=pd.read_csv('data2.csv')
data2=df2["Math_score"]. tolist()
mean2 = st.mean(data2)
sd2= st.stdev(data2)
zScore2= (mean2 - mean)/sd
print(zScore2)

df3=pd.read_csv('data3.csv')
data3=df3["Math_score"]. tolist()
mean3 = st.mean(data3)
sd3= st.stdev(data3)
zScore3= (mean3 - mean)/sd
print(zScore3)