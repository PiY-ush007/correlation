import pandas as pd
import numpy as np
import csv

def getData(data_path):
    marks=[]
    attendence=[]
    with open(data_path) as f:
        csvInfo = csv.DictReader(f)
        for row in csvInfo:
            marks.append(float(row["Marks In Percentage"]))
            attendence.append(
                float(row["Days Present"]))
    return {'x': marks, 'y': attendence }

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])
    print(correlation[0, 1])

def setup():
    data_path: './data/Marks In Percentage,Days Present.csv'
    data_source = getData(data_path)
    findCorrelation(data_source)


setup()

     