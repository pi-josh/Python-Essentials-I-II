# Converting fuel consumption
'''
A car's fuel consumption may be expressed in many different ways.
For example, in Europe, it is shown as the amount of fuel consumed per 100 kilometers.

In the USA, it is shown as the number of miles traveled by a car using one gallon of fuel.

Your task is to write a pair of functions converting l/100km into mpg, and vice versa.

The functions:

are named liters_100km_to_miles_gallon and miles_gallon_to_liters_100km respectively;
take one argument (the value corresponding to their names)
Complete the code in the editor and run it to check whether your output is the same as ours.

Here is some information to help you:

1 American mile = 1609.344 metres;
1 American gallon = 3.785411784 litres.
'''
def liters_100km_to_miles_gallon(liters):
    gallon = liters / 3.785411784
    km100 = 100 * 1000 / 1609.344
    return km100 / gallon

def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 100 / 1000 
    liters = 3.785411784
    return liters / km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

