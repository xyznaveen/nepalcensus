import os
dirs = os.listdir('/Users/naveen/Documents/nepal_census/data_repo/districts')
data = []
for dir in dirs:
    d = dir.replace('.geojson', '')
    data.append(f"{d}")

print(data)