import pandas as pd
import statistics
import plotly.express as px

#Plotting the graph
df = pd.read_csv("savings_data_final.csv")
fig = px.scatter(df, y="quant_saved", color="rem_any")
fig.show()


import csv

with open('savings_data_final.csv', newline="") as f:
  reader = csv.reader(f)
  savings_data = list(reader)

savings_data.pop(0)

#Finding total number of people and number of people who were reminded
total_entries = len(savings_data)
total_people_given_reminder = 0
for data in savings_data:
  if int(data[3]) == 1:
    total_people_given_reminder += 1

import plotly.graph_objects as go

fig = go.Figure(go.Bar(x=["Reminded", "Not Reminded"], y=[total_people_given_reminder, (total_entries - total_people_given_reminder)]))

fig.show()

reminded_savings = []
not_reminded_savings = []
for data in savings_data:
    if int(data[3]) == 1:
        reminded_savings.append(float(data[0]))
    else:
        not_reminded_savings.append(float(data[0]))

        print("results for prople who were reminded to save ")
        print(f"mean of savings-{statistics.mean(reminded_savings)}")
        print(f"mode of savings-{statistics.mode(reminded_savings)}")
        print(f"median of savings-{statistics.median(reminded_savings)}")

        print("\n\n")
print("Results for people who were not reminded to save")
print(f"Mean of savings - {statistics.mean(not_reminded_savings)}")
print(f"mode of savings - {statistics.mode(not_reminded_savings)}")
print(f("median of savings - {statistics.median(not_reminded_saving)}"))