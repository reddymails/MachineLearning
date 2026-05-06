###################################################################
#
# Group by Examples.
#
#####################################################################
import numpy as np
import pandas as pd


df = pd.read_csv("weather_data_city.csv")
df_ny_max_temp = df[df.city == "new york"].temperature.max()
print('df_ny_max_temp='+ str(df_ny_max_temp))

df_mumbai_max_temp = df[df.city == "mumbai"].temperature.max()
print('df_mumbai_max_temp='+ str(df_mumbai_max_temp))

# Creates a map with City name and rest of records as Value. with 1:N

grouped_by_City = df.groupby("city")
print('grouped_by_City='+ str(grouped_by_City))

for city, data  in grouped_by_City:
    print('city='+ str(city))
    print('data.temperature.mean()='+ str(data.temperature.mean()))
    print('data after grouping by City=\n'+ str(data))

print('min temperature= \n '+ str(grouped_by_City.min()))

print('grouped_by_City=\n'+ str(grouped_by_City.describe()))
print(' Size (Tells how many records were group by under each group )=\n'+ str(grouped_by_City.size()))

# idx tells which row we are looking at and col tells which column.
def groupByTemp(df, idx, col) :
    if 80<= df[col].loc[idx] <= 100:
          return '80-100'
    elif 50<= df[col].loc[idx] <= 60:
          return '50-60'
    else:
          return 'others'


#Custom functions for Group by
df_group_by_temp = df.groupby(lambda x: groupByTemp(df,x,'temperature'))
print('df_group_by_temp='+ str(df_group_by_temp.describe()))

for key,value in df_group_by_temp:
     print('Key=',key)
     print('Value=\n', value)

df_80_100_range = df_group_by_temp.get_group('80-100')
print('df_80_100_range \n=',df_80_100_range)