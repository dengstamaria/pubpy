import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

df = pd.read_csv('course2data.csv')

#convert date column to real date format
df["Date"] = pd.to_datetime(df["Date"])

#spread out month, day and year
date_index=pd.DatetimeIndex(df['Date'])
df['month']=date_index.month
df['day']=date_index.day
df['year']=date_index.year
df['dayofyear']=date_index.dayofyear

 # remove feb 29 from dataframe
df=df[~((df.month==2) & (df.day ==29))]

#add column and convert Temp to celcius
#used *.1 instead of /10. division utilizes most of the memory.
df['temp_in_C']=df['Data_Value']*.1

#create df without 2015 data
df_data=df[~(df.year==2015)]

#create df for TMAX Elements and get max value
df_tmax = df_data[df_data.Element=='TMAX']
tmax = pd.pivot_table(df_tmax,index='dayofyear',values=['temp_in_C'],aggfunc={'temp_in_C':'max'})

#create df for TMIN Elements and get min value
df_tmin = df_data[df_data.Element=='TMIN']
tmin=pd.pivot_table(df_tmin,index='dayofyear',values=['temp_in_C'],aggfunc={'temp_in_C':'min'})

#create 2015 df and respective tmax and tmin df's
df_2015=df[(df.year==2015)]

df_2015_tmax = df_2015[df_2015.Element=='TMAX']
tmax_2015=pd.pivot_table(df_2015_tmax,index='dayofyear',values=['temp_in_C'],aggfunc={'temp_in_C':'max'})

df_2015_tmin = df_2015[df_2015.Element=='TMIN']
tmin_2015=pd.pivot_table(df_2015_tmin,index='dayofyear',values=['temp_in_C'],aggfunc={'temp_in_C':'min'})

#create df to show data values that exceed the 2005 to 2014 data
tmin_exceed=tmin_2015[tmin_2015.temp_in_C < tmin.temp_in_C.loc[:len(tmin_2015)]]

tmax_exceed=tmax_2015[tmax_2015.temp_in_C > tmax.temp_in_C.loc[:len(tmax_2015)]]

#create figure and axes
fig = plt.figure()
fig, ax = plt.subplots()
plt.plot(tmin.temp_in_C,color="white")
plt.plot(tmax.temp_in_C,color="white")
plt.plot(tmin_exceed.temp_in_C,".",color="blue")
plt.plot(tmax_exceed.temp_in_C,".",color="red")

# set y axis with degrees celcius softened label by turning to grey
ax.yaxis.set_major_formatter(plt.FuncFormatter('{:.0f}$^\circ$C'.format))
plt.yticks(alpha=0.8)

#set the range of xticks soften labels by turning to grey
plt.xticks(range(0, 366, 30), alpha=0.8)
plt.xlabel('Day of Year', alpha=0.8)

#set figure title
plt.title('Daily High and Low temperatures from 2005-2014 and record breaks of 2015 data.\n',alpha=0.8)

# fill the area between the tmax annd tmin data
plt.fill_between(range(len(tmax)),tmax.temp_in_C,tmin.temp_in_C,facecolor='blue',alpha=0.25)


# remove the frame of the chart
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# remove the ticks (both axes)
plt.tick_params(top='off', bottom='on', left='on', right='off', labelleft='on', labelbottom='on')

#set up legends
red_patch = mpatches.Patch(color='red', label='2015 high temp')
blue_patch = mpatches.Patch(color='blue', label='2015 low temp')
shade_patch = mpatches.Patch(color='blue', label='2005 to 2014 temp',alpha=0.25)
plt.legend(handles=[shade_patch,red_patch,blue_patch],loc=4,frameon=False)

plt.show()

