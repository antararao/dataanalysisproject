import pandas as pd 
import csv 
import plotly.graph_objects as go 

df = pd.read_csv("dataanalysis.csv")
student_df = df.loc[df['student_id']== 'TRL_abc']
print(df.groupby("level")["attempt"].mean())
fig = go.Figure(go.Scatter(x = student_df.groupby("level")["attempt"].mean(),y = ['level1','level2', 'level3', 'level4'], orientation = 'h'))

fig.show()
