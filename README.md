"# Typhoon_Stats" 
This project contains code to derive statistics used for extreme event analysis for tropical cyclones.
The topic is tropical cyclones of the Northern West Pacific ocean and the technique determines
the return period also know as recurrence interval of peak winds.  We start with a dataset of tropical
cyclone tracks for a historically large time frame from 1945 to 2014.   The data was in  6 hourly intervals
where we needed to interpolate it to hourly estimates. The data is loaded into a sqlite database. After the 
data is loaded we included a wind profile model used to estimatewind speed only knowing the maxumum wind,
the radius of maximum wind, here assumed to be 12.5 nautical miles and the distance from the center of the 
tropical cyclone.  This allows us to translate the bext track data into an estimate ofwinds experienced at a
user selected point.

A python 
program is used to derive the peak winds by year for a user selected point using latitude and longitude.
The output is a small file that is used as input into the routine to calculate the relative probability and 
its corresponding return period of a particulare threshold of wind speed. Charts are produced to illustrate
the fit of the model. The png files uploaded show the resultant charts I generated.

The source file was over 25mb that was used to popuate the sqlite3 database but it is included as a zipped file to this repository.
This can be applied to Atlantic hurricanes but i recommend caution as you may need to sample over periods longer than
one year so as to ensure you have extreme values in the upper tail of the distribution.
Best regards

John Rupp
