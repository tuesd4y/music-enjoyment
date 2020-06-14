import pandas as pd
import numpy as np
import glob
import os

sampling_rate = 20
window = 15 * sampling_rate
files = sorted(glob.glob(os.path.join('data', '**/Shape Of you.csv'), recursive=True))

shape_of_you = []
for file in files:
    dance = pd.read_csv(str(file), skiprows=3)
    dance['time'] = dance.reset_index().index * sampling_rate
    dance.fillna(value=0.0)
    temp = []

    try:
        x = (dance['Linear_Acceleration_Sensor.x'])

        i = 0
        while i < len(x):
            temp.append(np.average(x[i:i + window]))
            i += window

        shape_of_you.append(temp)

    except Exception as e:
        print(str(file) + ' has exception: ' + str(e))

a = list(zip(*shape_of_you))

for i in range(0, len(a)):
    avg = np.average(a[i])
    for x in a[i]:
        if x > avg:
            print(f'person {files[ a[i].index(x)]} tanzt energisch')
