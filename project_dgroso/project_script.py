#!/usr/bin/env python

import pandas as pd 

data1 = 'Covid_6.16.csv'
data2 = 'Covid_6.5.csv'
d1handle = open(data1, 'r')
d2handle = open(data2, 'r')

# create 2 dataframes 
df1=pd.read_csv(d1handle, usecols=[5,32])
df2=pd.read_csv(d2handle, usecols=[32])
full = pd.concat([df1, df2], axis=1)
full['rate'] = full['Tpositive_6.16'] - full['Tpositive_6.5']
    
# create function 1 
def highest_change():
    max_rate = full.max()[3]
    
    for i, row in full.iterrows():
        c = row[0]
        r = row[3]
        ####format the date and change as a string, store in variable statement
        statement = "County with the highest rate of positive cases: {0}     Increase in positive Covid-19 cases: {1}".format(c, r)
        ####if the change is the max value, return date and change as formatted in statement 
        if r == max_rate: 
            return statement
            print(statement)
def lowest_change():
    min_rate = full.min()[3]
    
    for i, row in full.iterrows():
        c = row[0]
        r = row[3]
        ####format the date and change as a string, store in variable statement
        statement = "County with the lowest rate of positive cases: {0}     Increase in positive Covid-19 cases: {1}".format(c, r)
        ####if the change is the max value, return date and change as formatted in statement 
        if r == min_rate: 
            return statement
            print(statement)
    
   
print(highest_change(),'\n',lowest_change())


with open("covidrates.txt", "w") as file1:
    file1.write(highest_change())
    file1.write("\n")
    file1.write(lowest_change())

