from math import isqrt
import statistics
import plotly.figure_factory as pf
import plotly.graph_objects as go
import csv
import numpy as np
import seaborn as sb
import pandas as pd
import plotly.express as pe
import random 

df = pd.read_csv("data.csv")

with open("data.csv") as f:
    a = csv.reader(f)
    savings_data = list(a)

savings_data.pop(0)

All_savings = []

for i in savings_data:
    All_savings.append(float(i[0]))

mean = statistics.mean(All_savings)
median = statistics.median(All_savings)
mode = statistics.mode(All_savings)
std_dev = statistics.stdev(All_savings)

reminded_savings = []
not_reminded_savings = []

for i in savings_data:
    if int(i[2]) == 1:
        reminded_savings.append(float(i[0]))

    else:
        not_reminded_savings.append(float(i[0]))


mean_not_rem = statistics.mean(not_reminded_savings)
mean_rem = statistics.mean(reminded_savings)
std_dev_not_rem = statistics.stdev(not_reminded_savings)

std1start = mean_not_rem-std_dev_not_rem
std1end = mean_not_rem+std_dev_not_rem

std2start = mean-(2 * std_dev)
std2end = mean+(2 * std_dev)


std3start = mean-(3 * std_dev)
std3end = mean+(3 * std_dev)

q1 = df["quant_saved"].quantile(0.25)
q3 = df["quant_saved"].quantile(0.75)

iqr = q3-q1

lower_whisker = q1 - (1.5*iqr)
upper_whisker = q3 + (1.5*iqr)

newDf = df[ df["quant_saved"] < upper_whisker ]

print("Q1: ", q1)
print("Q3: ", q3)
print("IQR: ", iqr)
print("Lower Whisker: ", lower_whisker)
print("Upper Whisker: ", upper_whisker)
print("first start: ", std1start)
print("first end: ", std1start)
print("second start: ", std2start)
print("second end: ", std2start)
print("third start: ", std3start)
print("third end: ", std3start)
print("Z-score: ", (mean_rem - mean_not_rem)/std_dev_not_rem)
