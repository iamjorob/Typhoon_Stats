import math
import numpy as np
import pandas as pd


def getCumPr(red_var,grouping):

	cumpr=math.exp(-math.exp(-red_var)) # cumpr but based on grouped data
	#print(" the reduced variate input=  " +str(red_var))
	#print(" the cumulative pr is = " + str(cumpr))
	retper1yr=1.0/(1.0-(cumpr**(1.0/grouping)  )    ) #get the true 1 year value for return period
	truepr=1.0 -1.0/(retper1yr)   # trup cumulative probability for 1 year interval
	return retper1yr, truepr


#mypath="peakwindoutputfile.txt"
#mypath="Subset_highest_in_2.txt"
mypath="Subset_highest_in_4.txt"
grouping=4    # this is a parameter used to determine the 1 year return period
				# based on the grouping of the source data. 
				# if its subsampled for a peak wind in every 2 years this value should be 2.
				# if subsampling is the highest in every 4 years then this is 4.

def readFloats(pathToFile):  # this reads in the vector of values from a file.

    with open(pathToFile) as f:
        #a = [int(x) for x in f.read().split()]
        a = [float(x) for x in f.read().split()]
    return a


mylist= []
doaklist=[]
cumpr= []
reduced_var=[]

mylist = readFloats(mypath)  # reads in the file of numbers into a list called mylist
#print (mylist)

doaklist=mylist
doaklist.sort(reverse=False)
#print(doaklist)
n=len(doaklist)

for idx, val in enumerate(doaklist):
    #print(idx, val)
    thispr=float(idx+1)/float(n+1)
    cumpr.append(float(thispr))
    rvar=-math.log((-math.log(thispr)))
    reduced_var.append(rvar)

#print(cumpr)	
#print(reduced_var)
#-----------------------------------------------------
import matplotlib.pyplot as plt

x_data = doaklist
y_data = reduced_var

#================================================================
# this fits the data to a linear model.The response variable is the transformed
# cumulative probability by taking the double logarithm.

from scipy import stats
slope, intercept, r_value, p_value, std_err = stats.linregress(x_data,y_data)

#print("slope  =" , slope)
#print("intercept = ", intercept)

minx=min(x_data)
maxx=max(x_data)
miny=slope*minx + intercept
maxy=slope*maxx + intercept
abline_values = [slope * i + intercept for i in x_data]
plt.scatter(x_data, y_data, s=5,c='g', label='data')
plt.grid(True)
plt.xlabel('x Peak annual wind speed KTs subsampled 4 years')
plt.ylabel('y=  -Ln(-Ln(CumPr))')
plt.title('Peak windspeed versus reduced variable =-Ln(-Ln(Cum pr.))  ')
plt.legend()
outslope=round(slope,3)
outintercept=round(intercept,3)
outstring="Y= " + str(outslope) + " * WindSpeed  " +str(outintercept) 

plt.text(0.5, 0.2, outstring, fontsize=8, transform=plt.gcf().transFigure)
plt.plot(x_data, abline_values, 'b')
plt.show()
#====================================================================

#===============================================================
# section for the chart of wind speeds versus recurrent intervals or return periods.

import matplotlib.pyplot as plt3
wspd_data=[]    # define the empty lists
rec_int=[]
for i in range(30,155,10):   #load data into the lists for a range of wind speeds.
	wspd_data.append(float(i))
	yval=slope*float(i) +intercept          # this is the reduced variate

	a,b=getCumPr(yval,grouping)
	rec_int.append(round(a,2))  # a is the return period

#next blend the 2 lists into a dataframe.
#print(wspd_data)
#print(rec_int)

# Python 3 to get list of tuples from two lists
data_tuples = list(zip(wspd_data,rec_int))

# loads the data into a dataframe.
mydataframe=pd.DataFrame(data_tuples, columns=['Wind Speed Kts','Return Period in years'])

fig, ax = plt3.subplots()
newdf=mydataframe
ax.table(cellText=newdf.values, colLabels=newdf.columns, loc='center')
fig.tight_layout()
plt3.gca().axes.get_yaxis().set_visible(False)
plt3.axis('off')
plt3.title('Recurrence interval of peak annual Tropical cyclone winds for Guam')
plt3.show()