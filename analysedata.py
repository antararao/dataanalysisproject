import pandas as pd 
import csv 
import plotly.express as go 

df = pd.read_csv("dataanalysis.csv")
mean = df.groupby(['student_id', "level"],as_index = False ) ['attempt'].mean()
# print(df.groupby("student_id")["level"].mean())
fig = go.scatter(mean, x = "student_id", y = "level", color = "attempt")

fig.show()
