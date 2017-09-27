import pandas as pd
import numpy
import math
import scipy
import pylatex

#The Incomplete beta function, for cumulative distribution functions
def IncBeta(f, alpha, beta):
    integrand = lambda t: (t**(alpha-1))*((1-t)**(beta-1))
    numerator, err = scipy.integrate.quad(integrand, 0, k)
    denominator, err = scipy.integrate.quad(integrand, 0, 1)
    return numerator/denominator;

	#the chi squared cumulative distribution function
def chicdf(x, a):
    a = v/2
    integrand = lambda t: (t**(a-1))*exp(-t)
    numerator = scipy.integrate.quad(integrand, 0, x/2)
    denominator = scipy.integrate.quad(integrand, 0, inf)
    return numerator/denominator


#read a csv file
file = input("Enter the name of the data file: ")
data = pd.read_csv(file, header=0)

#show the user the variables in the dataset
print(data.columns.values)

#isolating the variablews of interest
categories = data['Sex'].unique().tolist()
malePopulation = data.loc[data.Sex == categories[0]]
femalePopulation = data.loc[data.Sex == categories[1]]

#sampling
sampleSize = 20
maleSample = malePopulation['Length'].sample(sampleSize)
femaleSample = femalePopulation['Length'].sample(sampleSize)

#testing for equality of variances
maleVar = numpy.var(maleSample)
femaleVar = numpy.var(femaleSample)
F_EqVar = maleVar/femaleVar
print(F_EqVar)