import math
#  This program takes a file of numbers the represent the peak value in  a year and
#  converts or subsamples this to give the peak value in 2 years.
#  Its used when it appears the sampling doesnt get values in the tail of the 
#  Extreme distribution.
#
#

#mypath="peakwindoutputfile.txt" # this will take original dataconvert in the subsampled 2
mypath="Subset_highest_in_2.txt" # Source file of data to convert in the subsampled 4
def readFloats(pathToFile):

    with open(pathToFile) as f:
        #a = [int(x) for x in f.read().split()]
        a = [float(x) for x in f.read().split()]
    return a

# declare lists to be used
mylist= []
doaklist=[]
cumpr= []
reduced_var=[]
sublist=[]

# reads in the file of numbers into a list called mylist
mylist = readFloats(mypath)  
print (mylist)

doaklist=mylist

n=len(doaklist)
print("n= " +str(n))

step=2
start=step-1
global maxnum
for i in range(start,n,step):
	if(mylist[i]>mylist[i-1]): # this takes a pair of numbers, finds the highest one.
		maxnum=mylist[i]
	else:
		maxnum=mylist[i-1]

	sublist.append(maxnum)

	print ( i , " value=" , str(mylist[i]) , maxnum  ) 

print(sublist)
n=len(sublist)
print(" number in the sublist = " +str(n))

# myfile = open("Subset_highest_in_2.txt","w")


with open('Subset_highest_in_4.txt', 'w') as f:
    for item in sublist:
        f.write("%s\n" % item)
print("done")