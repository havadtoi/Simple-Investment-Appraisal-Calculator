#Investment Appraisal Calculator v0.1 built 8 May 2020

#importing necessary packages
import numpy as np

#set parameters for calculation
#discount rate
r = 0.095
#cost of revenue
cogs = 0.25
#tax rate
t = 0.28
#initial investment at year 0
i = -1000000
#cashflow as numpy array, starting from year 1
cf = np.array([300000, 500000, 600000, 600000, 600000])

#calculate net cash flows
cf = cf * (1 - cogs) * (1 - t)

#calculate project IRR
cfAll = np.append(i, cf)
irr = round(np.irr(cfAll)*100, 2)

#calculate net present value of cashflows
for x in range(len(cf)): cf[x] = round(cf[x]/(1+r)**(x+1), 2)
#calculate project NPV
npv = round(np.sum(cf) + i, 2)

#calculate payback period
pbp = -1
for x in range(len(cfAll)):
    if (np.sum(cfAll[:x]) < 0) and (np.sum(cfAll[:x+1]) >= 0) == True:
        pbp = round( x + ( - np.sum(cfAll[:x+1]) / cfAll[x+1] ) , 2)

#Reporting results
print('IRR of the project is ' + str(irr) + '%')
print('NPV of the project is £' + str(npv))
if pbp >=0:
    print('Payback period of the project is ' + str(pbp) + ' years')
else: print('Project does not payback.')
