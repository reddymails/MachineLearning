####################################
# Data concatenation and merging.
#
####################################

import pandas as pd

india_weather= pd.DataFrame({
    "city":["Mumbai","Bangalore","Hyderabad","SriNagar"],
    "temperature":[95,80,88,60],
    "humidity":[80,60,78,65]
})

print(india_weather)

USA_weather= pd.DataFrame({
    "city":["Boston","NewYork","SFO","Chicago"],
    "temperature":[60,550,80,50],
    "humidity":[80,60,90,75]
})

print(USA_weather)

# if we specify axis =1 it will copy rows in same line rather at bottom.
df_combined = pd.concat([india_weather,USA_weather],axis=0,ignore_index=True)
print('df_combined=\n',df_combined)


# in case you want to add Keys to each file that's getting merged
# it creates as Hashmap.
df_combined_with_key = pd.concat([india_weather,USA_weather],axis=0, keys=['india_weather','USA_weather'])
print('df_combined_with_key=\n',df_combined_with_key)

print('Print india_weather Only=',df_combined_with_key.loc['india_weather'])



# by specify index we are tagging each record
temperature_df = pd.DataFrame({
    "city":["Bangalore","Hyderabad","Mumbai","SriNagar"],
    "temperature":[95,80,88,60]
}, index=[0,1,2,3])

# Now using above index , we want to link this data and we are telling to connect Mumbai to index=2 and Bangalore to index=0
# in the above records
windspeed_df = pd.DataFrame({
    "city":["Mumbai","Bangalore"],
    "windspeed":[7,12]
}, index=[2,0])


df_combined_odd_columns = pd.concat([temperature_df,windspeed_df],axis=1)
print('df_combined_odd_columns=\n',df_combined_odd_columns)


# Merging without index based on column name.
temperature_df_1 = pd.DataFrame({
    "city":["Bangalore","Hyderabad","Mumbai","SriNagar","Chicago"],
    "temperature":[95,80,88,60,50]
})
windspeed_df_1 = pd.DataFrame({
    "city":["Mumbai","Bangalore","SriNagar","Hyderabad","Boston"],
    "windspeed":[7,12,20,11,30]
})
#Beautiful it worked. since its inner join we don't see Boston or Chicago
#Inner join example
combined_by_city_name_inner_join = pd.merge(temperature_df_1,windspeed_df_1,how='inner',on=['city'])
print('combined_by_city_name_inner_join= \n',combined_by_city_name_inner_join)


#Left outer join example - So we see Chicago but not Boston
combined_by_city_name_left_outer_join = pd.merge(temperature_df_1,windspeed_df_1,how="left",on=['city'])
print('combined_by_city_name_left_outer_join= \n',combined_by_city_name_left_outer_join)

#Right outer join example - So we see Boston  but not Chicago
combined_by_city_name_right_outer_join = pd.merge(temperature_df_1,windspeed_df_1,how="right",on=['city'])
print('combined_by_city_name_right_outer_join= \n',combined_by_city_name_right_outer_join)


#Outer join example - We see both Boston and Chicago
combined_by_city_name_outer_join = pd.merge(temperature_df_1,windspeed_df_1,how="outer",on=['city'])
print('combined_by_city_name_outer_join= \n',combined_by_city_name_outer_join)
