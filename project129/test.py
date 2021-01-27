import csv

data = []

with open('class130d1.csv', 'r') as f:
    csvReader = csv.reader(f)
    
    for row in csvReader:
        data.append(row)

Headers = data[0]
planetData = data[1:]

for data_point in planetData:
    data_point[2] = data_point[2].lower()

planetData.sort(key=lambda planet_Data: planet_Data[2]) 



with open('datasetfinal.csv','w') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(Headers)
    csvWriter.writerows(planetData)