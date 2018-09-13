# readfrom the database but calculate the distancesto the best track.
import sqlite3
import sys
import math
from array import array
daray=array('d',[5 for i in range(300)]) # populatesarray with default value of 5.

daray[ 20]=      20.175780
daray[ 21]=      20.175780
daray[ 22]=      20.175780
daray[ 23]=      22.285160
daray[ 24]=      23.691410
daray[ 25]=      25.097660
daray[ 26]=      26.152340
daray[ 27]=      27.207030
daray[ 28]=      28.261720
daray[ 29]=      29.316410
daray[ 30]=      30.371090
daray[ 31]=      31.425780
daray[ 32]=      32.480470
daray[ 33]=      33.535160
daray[ 34]=      34.238280
daray[ 35]=      35.292970
daray[ 36]=      36.347660
daray[ 37]=      37.050780
daray[ 38]=      38.105470
daray[ 39]=      38.808590
daray[ 40]=      39.863280
daray[ 41]=      40.917970
daray[ 42]=      41.621090
daray[ 43]=      42.675780
daray[ 44]=      43.378910
daray[ 45]=      44.433590
daray[ 46]=      45.136720
daray[ 47]=      46.191410
daray[ 48]=      46.894530
daray[ 49]=      47.949220
daray[ 50]=      49.003910
daray[ 51]=      49.707030
daray[ 52]=      50.761720
daray[ 53]=      51.464840
daray[ 54]=      52.519530
daray[ 55]=      53.222660
daray[ 56]=      54.277340
daray[ 57]=      55.332030
daray[ 58]=      56.035160
daray[ 59]=      57.089840
daray[ 60]=      58.144530
daray[ 61]=      58.847660
daray[ 62]=      59.902340
daray[ 63]=      60.957030
daray[ 64]=      61.660160
daray[ 65]=      62.714840
daray[ 66]=      63.769530
daray[ 67]=      64.824220
daray[ 68]=      65.527340
daray[ 69]=      66.582030
daray[ 70]=      67.636720
daray[ 71]=      68.691410
daray[ 72]=      69.746090
daray[ 73]=      70.800780
daray[ 74]=      71.855470
daray[ 75]=      72.558590
daray[ 76]=      73.613280
daray[ 77]=      74.667970
daray[ 78]=      75.722660
daray[ 79]=      76.777340
daray[ 80]=      77.832030
daray[ 81]=      78.886720
daray[ 82]=      80.292970
daray[ 83]=      81.347660
daray[ 84]=      82.402340
daray[ 85]=      83.457030
daray[ 86]=      84.511720
daray[ 87]=      85.566410
daray[ 88]=      86.621090
daray[ 89]=      88.027340
daray[ 90]=      89.082030
daray[ 91]=      90.136720
daray[ 92]=      91.191410
daray[ 93]=      92.597660
daray[ 94]=      93.652340
daray[ 95]=      94.707030
daray[ 96]=      96.113280
daray[ 97]=      97.167970
daray[ 98]=      98.222660
daray[ 99]=      99.628910
daray[100]=     100.683600
daray[101]=     102.089800
daray[102]=     103.144500
daray[103]=     104.550800
daray[104]=     105.605500
daray[105]=     107.011700
daray[106]=     108.066400
daray[107]=     109.472700
daray[108]=     110.527300
daray[109]=     111.933600
daray[110]=     112.988300
daray[111]=     114.394500
daray[112]=     115.449200
daray[113]=     116.855500
daray[114]=     117.910200
daray[115]=     118.964800
daray[116]=     120.371100
daray[117]=     121.425800
daray[118]=     122.832000
daray[119]=     123.886700
daray[120]=     125.293000
daray[121]=     126.347700
daray[122]=     127.753900
daray[123]=     128.808600
daray[124]=     129.863300
daray[125]=     131.269500
daray[126]=     132.324200
daray[127]=     133.378900
daray[128]=     134.785200
daray[129]=     135.839800
daray[130]=     136.894500
daray[131]=     137.949200
daray[132]=     139.355500
daray[133]=     140.410200
daray[134]=     141.464800
daray[135]=     142.519500
daray[136]=     143.574200
daray[137]=     144.628900
daray[138]=     145.683600
daray[139]=     146.738300
daray[140]=     147.793000
daray[141]=     148.847700
daray[142]=     149.902300
daray[143]=     150.957000
daray[144]=     152.011700
daray[145]=     152.714800
daray[146]=     153.769500
daray[147]=     154.824200
daray[148]=     155.878900
daray[149]=     156.582000
daray[150]=     157.636700
daray[151]=     158.691400
daray[152]=     159.394500
daray[153]=     160.449200
daray[154]=     161.152300
daray[155]=     162.207000
daray[156]=     162.910200
daray[157]=     163.964800
daray[158]=     164.668000
daray[159]=     165.722700
daray[160]=     166.425800
daray[161]=     167.480500
daray[162]=     168.183600
daray[163]=     168.886700
daray[164]=     169.941400
daray[165]=     170.644500
daray[166]=     171.347700
daray[167]=     172.050800
daray[168]=     172.753900
daray[169]=     173.808600
daray[170]=     174.511700
daray[171]=     175.214800
daray[172]=     175.918000
daray[173]=     176.621100
daray[174]=     177.324200
daray[175]=     178.027300
daray[176]=     178.730500
daray[177]=     179.433600
daray[178]=     180.136700
daray[179]=     180.839800
daray[180]=     181.543000
daray[181]=     182.246100
daray[182]=     182.949200
daray[183]=     183.652300
daray[184]=     184.355500
daray[185]=     185.058600
daray[186]=     185.410200
daray[187]=     186.113300
daray[188]=     186.816400
daray[189]=     187.519500
daray[190]=     188.222700
daray[191]=     188.574200
daray[192]=     189.277300
daray[193]=     189.980500
daray[194]=     190.683600
daray[195]=     191.035200
daray[196]=     191.738300
daray[197]=     192.441400
daray[198]=     192.793000
daray[199]=     193.496100
daray[200]=     193.847700
def gcdist(lat1,lon1,lat2,lon2):
	# Accept float command-line arguments x1, y1, x2, and y2: the latitude
	# and longitude, in degrees, of two points on the earth. Compute and
	# write to standard output the great circle distance (in nautical
	# miles) between those two points.
	#x1=48.87  # paris lat
	#y1=-2.33  #parislon   east is minus
	#x2= 30.27 
	#y2=97.74   # plus is west longitudes

	#'x1 = float(sys.argv[1])
	#'y1 = float(sys.argv[2])
	#'x2 = float(sys.argv[3])
	#'y2 = float(sys.argv[4])

	#  https://introcs.cs.princeton.edu/python/12types/greatcircle.py.html

	x1=float(lat1)  # not sure why lat is X and lon is Y but their formulas expect that.
	y1=float(lon1)
	x2=float(lat2)
	y2=float(lon2)

	# The following formulas assume that angles are expressed in radians.
	# So convert to radians.

	x1 = math.radians(x1)
	y1 = math.radians(y1)
	x2 = math.radians(x2)
	y2 = math.radians(y2)

	# Compute using the law of cosines.

	# Great circle distance in radians
	angle1 = math.acos(math.sin(x1) * math.sin(x2) \
	         + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

	# Convert back to degrees.
	angle1 = math.degrees(angle1)

	# Each degree on a great circle of Earth is 60 nautical miles.
	distance1 = 60.0 * angle1

	return distance1

	#print(str(distance1) + ' nautical miles')

	#-----------------------------------------------------------------------

	# Leningrad to SF

	# python greatcircle.py 59.9 -30.3 37.8 122.4
	# 4784.369673474519 nautical miles
	# 4784.369673474519 nautical miles
	#
	# Paris to Austin

	# python greatcircle.py 48.87 -2.33 30.27 97.74
	# 4423.14075970742 nautical miles
	# 4423.140759707421 nautical miles
	#
	# Nashville airport (BNA) to LAX

	# python greatcircle.py 36.12 -86.67 33.94 -118.4
	# 1557.505111036951 nautical miles
	# 1557.5051110369507 nautical miles
	#
	# Princeton to Paris

	# python greatcircle.py 40.35 74.65 48.87 -2.33
	# 3185.1779271158425 nautical miles
	# 3185.1779271158416 nautical miles

def martin(vmax, rmw, radius, lat):
		mult=3.0
		xdecay=.5

		if(radius < .02):
			radius=.02
		


		if(radius < (rmw*mult)):
			pamb=1010.
			d=1.15
			f=2.*(2.*3.1415927/(3600.*24.))*math.sin(lat*.01745329)
			ci=-.940760805+.110091407*vmax-(.000631747*vmax**2) +(.000001746*vmax**3)

			pmin=1004.033716 +(ci*3.758824509) -((ci**2)*2.716283716) - ((ci**3)*.002331002)

			b=(ci/7.)+1.1
			a=math.exp(b*math.log(rmw))
			eq1=a * b* (pamb-pmin)*377.344162
			eq2=(math.exp(-1*a/(radius**b))) /d / (radius**b)
			eq3=(radius**2) * (f**2)/4.
			eq4=radius*f/2.
			speed=.8*( (math.sqrt(eq1*eq2+eq3))-eq4)

			return speed;
		else:
			nradius=mult*rmw

			pamb=1010.
			d=1.15
			f=2.*(2.*3.1415927/(3600.*24.))*math.sin(lat*.01745329)
			ci=-.940760805+.110091407*vmax-(.000631747*vmax**2) + (.000001746*vmax**3)

			pmin=1004.033716 +(ci*3.758824509) -((ci**2)*2.716283716) - ((ci**3)*.002331002)
			b=(ci/7.)+1.1
			a=math.exp(b*math.log(rmw))
			eq1=a * b* (pamb-pmin)*377.344162
			eq2=(math.exp(-1*a/(nradius**b))) /d / (nradius**b)
			eq3=(nradius**2) * (f**2)/4.
			eq4=nradius*f/2.

			speed=.8*( (math.sqrt(eq1*eq2+eq3))-eq4)
			const=speed*((mult*rmw)**xdecay  )
			speed=const/( (radius**xdecay) )
			return speed;

#===============================================================
#===============================================================

conn = sqlite3.connect('jorob_test.db')

c= conn.cursor()  # this is your cursor.

myoutputfile=open("PeakWindOutputFile.txt", "w")

global stationlat
global stationlon
stationlat = input('Enter the station lat (ie 13.1) + for north - for south: ')
stationlon = input('Enter station longitude - for east (-144.8) + for west longitudes : ')

for year in range(1945,2015):


	thesqlstring="select * from wptracks1hr where theyear=" + str(year)

	#c.execute('select * from wptracks2 where theyear=1996')
	c.execute(thesqlstring)

	#stationlat=13.4  # coordinates for guam.
	#stationlon=-144.8
	
	global pkwindyr
	global mindist

	pkwindyr=0.
	mindist=10000.
	doaklist=[]
	for row in c:
	

		#mindist=10000.
		#print("row= ", row)

		mylat=row[4]
		mylon=row[6]
		mylatind=row[5]
		mylonind=row[7]
		tcwind=row[8]


		if tcwind<15:
			tcwind=15
		vcor=daray[int(tcwind)] # provides a corrected wind speed value for the model.
								# this ensures the radius of max wind has a value equal to the true
								# wind speed.
		#print(" --------------------- The corrected wind is = " +str(vcor))
		#find the corrected vmax value


		# need to pull the wind speed from the database.
		#then calculate the resultant wind speed at that point given the 
		# martin function and the vcorfunction.
		if (mylatind=='S'): 
			mylat=-mylat
		if (mylonind=='E'): 
			mylon=-mylon
		
		mydistance=gcdist(stationlat,stationlon,mylat,mylon)
		if (mindist>mydistance):
			mindist=mydistance
			doaklist.append(mindist) # keeps  track of theminimum distance.

		radius=mydistance
		rradius=float(radius)
		correctedspeed=vcor
		#speed= martin(120.0, 12.5, rradius, lat)
		# climatological radius  of max wind is 12.5 NM for west pacific cyclones.
		speed= martin(correctedspeed, 12.5, rradius, mylat)
		if (pkwindyr<speed):
			pkwindyr=speed # holds the peak wind for this year based on a tropical cyclone
							#modelled wind speed for this point based on the Martin Holland
							#wind model as described in the Journalof Applied Meteorology.
							# A Technique for Estimating Recurrence Intervals of Tropical Cyclone–Related High Winds in the Tropics: Results for Guam
							#John A. Rupp and Mark A. Lander. Journal of Applied Meteorology Vol. 35, No. 5 (May 1996), pp. 627-637 


		# print("my lat = " + str(mylat))
		# print("    my lon= " + str(mylon) )
		# print(" GC distanceto this point= "  + str(mydistance))
		# print(" ******************************   minimum distance=  " + str(mindist))

	#print("minimum distance= " +str(mindist) + " in year " + str(year))
	print("       The max wind =  " +str(round(pkwindyr,1))+  "  in year  " + str(year))
	myoutputfile.write(str(round(pkwindyr,1))+"\n")
myoutputfile.close()
	#print(doaklist)
	#themindist=min(doaklist)
	#print(" Year= " + str(year) + "the minimum distance was = " +str(themindist))
