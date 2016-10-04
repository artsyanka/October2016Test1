#Write a function flip that simulates flipping n fair coins. 
#It should return a list representing the result of each flip as a 1 or 0
#To generate randomness, you can use the function random.random() to get
#a number between 0 or 1. Checking if it's less than 0.5 can help your 
#transform it to be 0 or 1

import random
from math import sqrt
from plotting import *

def mean(data):
    #print(float(sum(data))/len(data))
    return float(sum(data))/len(data)

def variance(data):
    mu=mean(data)
    return sum([(x-mu)**2 for x in data])/len(data)

def stddev(data):
    return sqrt(variance(data))
    

def flip(N):
    #Insert your code here
    flipsList=[]
    for i in range(N):
        if random.random() < 0.5:
         flipsList.append(0)
        else:
         flipsList.append(1)                    
    return flipsList

def sample(N):
    #Insert your code here
    meansList=[]
    for i in range(N):
        meansList.append(mean(flip(N)))
    return meansList





N=1000
outcomes=sample(N)
histplot(outcomes,nbins=30)

print(mean(outcomes))
print(stddev(outcomes))

