# Python 3
import random
from statistics import median
import json
import csv

#Intitial variables
data_values = []

#Functions
def random_data(n, minimum, maximum):
    for x in range(0, n):
        r = random.uniform(minimum, maximum)
        data_values.append(r)
    return data_values

def trending_data(n, minimum, maximum):
    i = n
    data_values.append(minimum)
    #real_plus and real_minus are to add variation to the data with the aim of making it look more realistic.
    real_plus = float((maximum - minimum) / (n * 0.2))
    real_minus = float((-1 * real_plus) * 0.20)
    while i > 0:
        k = n-i
        r = random.uniform(real_minus, real_plus)
        if (data_values[k] + r >= minimum ) and (data_values[k] + r <= maximum) and i > 0:
            data_values.append(data_values[k] + r)
            r = random.uniform(real_minus, real_plus) #To stop the loop completing using the same value for r every time.
            i -= 1

    return r
    return i
    return data_values

def normal_data(n, mu, sigma):
    i = n
    while i > 0:
        data_values.append(random.normalvariate(mu, sigma))
        i -= 1
    return data_values

#Start
print ("sharkbite1414's database generator v0.010")

n = int(input ("Number of samples (n) = "))

data_points = list(range(1,n+1))

data_type = input ("Choose data type: (R)andom, (T)rending, (N)ormal: ")
if data_type == "R" or data_type == "r":
    minimum = float(input("Choose minimum data value: "))
    maximum = float(input("Choose maximum data value: "))
    random_data(n, minimum, maximum)
elif data_type == "T" or data_type == "t":
    minimum = float(input("Choose minimum data value: "))
    maximum = float(input("Choose maximum data value: "))
    trending_data(n, minimum, maximum)
elif data_type == "N" or data_type == "n":
    mu = float(input("Choose mean: "))
    sigma = float(input("Choose std dev: "))
    normal_data(n, mu, sigma)


else:
    print ("Sorry, selection unknown.")

print (data_values)

database = dict(zip(data_points, data_values))
print (database)

with open("output.json","w") as json_file:
    json_file.write(json.dumps(database))

with open("output.csv", "w") as csv_file:
    w = csv.writer(csv_file)
    w.writerows(database.items())


print ("Data has been exported to output.json and output.csv")
