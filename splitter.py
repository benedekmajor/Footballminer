import io
import os
import sys
from tqdm import tqdm

filename = "odds_series.csv"

f = open("dataset/" + filename)
lines = f.readlines()
f.close()

t = 0
list = []

for i in tqdm(range(1, len(lines))):
    list.append(lines[i])
    if i % 3107 == 0:
        f = open("split_data/" + str(t) + ".csv", "w")
        f.write(lines[0])
        for item in list:
            f.write(item)
        f.close()
        list = []
        t = t + 1
