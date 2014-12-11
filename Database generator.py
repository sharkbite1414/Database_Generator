import random
from statistics import median
import json
#import csv


data_values = []


def random_data(n, minimum, maximun):
  for x in random.sample(range(minimum,maximun),n):
    data_values.append(x)
  return data_values

def trending_data(n, minimum, maximun):
  i = n
  data_values.append(minimum)
  while i > 0:
    k = n-i
    data_values.append(data_values[k] + random.randint(-2,5)) #TO_DO randint should be tied to maximun and minimum
    i -= 1
  return data_values

def normal_data(n, mu, sigma):
  i = n
  while i > 0:
    data_values.append(random.normalvariate(mu, sigma))
    i -= 1
  return data_values


print ("shark's database generator v0.002")

n = int(input ("Number of samples (n) = "))
print ("n =",n)

data_points = list(range(1,n+1))
print (data_points)

data_type = input ("Choose data type: (R)andom, (T)rending, (N)ormal.")
if data_type == "R" or data_type == "r":
  minimum = int(input("Choose minimum data value: "))
  maximun = int(input("Choose maximun data value: "))
  random_data(n, minimum, maximun)
elif data_type == "T" or data_type == "t":
  minimum = int(input("Choose minimum data value: "))
  maximun = int(input("Choose maximun data value: "))
  trending_data(n, minimum, maximun)
elif data_type == "N" or data_type == "n":
  mu = int(input("Choose mean: "))
  sigma = int(input("Choose std dev: "))
  normal_data(n, mu, sigma)


else:
  print ("Sorry, selection unknown.")

print (data_values)

database = dict(zip(data_points, data_values))
print (database)

with open("output.json","w") as json_file:
  json_file.write(json.dumps(database))

#with open("output.csv", "w", newline="") as csvfile:
  #csv_file = csv.writer(csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
  #csv_file.writerow(database.keys())
  #csv_file.writerow(database.values())

print ("Data has been exported to output.json")
input("Press Enter to close")
