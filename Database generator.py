import random
import json
import csv

print ("shark's database generator v0.001")

n = input ("Number of samples (n) = ")
n = int(n)
print ("n =",n)

data_points = list(range(1,n+1))
print (data_points)

minimum = int(input("Choose minimum data value: "))
maximun = int(input("Choose maximun data value: "))

data_values = random.sample(range(minimum,maximun),n)
print (data_values)

database = dict(zip(data_points, data_values))
print (database)

with open("output.json","w") as json_file:
  json_file.write(json.dumps(database))

#with open("output.csv", "w", newline="") as csvfile:
  #csv_file = csv.writer(csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
  #csv_file.writerow(database.keys())
  #csv_file.writerow(database.values())
