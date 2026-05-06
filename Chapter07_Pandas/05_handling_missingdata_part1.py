###################################################################
#   Data transformation when loading excel and
#   Calculating mean , median when there is no data in few cases based on existing
#   data in other columns or Rows.
#
#####################################################################

import pandas as pd

# while reding parsing string to date
df = pd.read_csv('weather_data.csv',parse_dates=['day'])
print('Before = '+ str(df.head()))
print(type(df.day[0]))


# Lets replace Nan with zeros, Since we have mixed types of int and string we need to do this.
df.fillna({
    'temperature': 0,
    'windspeed': 0,
    'event': 'No Event'
}, inplace=True)

print('After='+ str(df.head()))

# Re load lets replace na with some meaningful value using Mean or medium.
df_reloaded = pd.read_csv('weather_data.csv',parse_dates=['day'])

# so when we see n/A we will fill with mean value of that column which is good prediction.
df_reloaded.fillna({
    'temperature': df_reloaded.temperature.mean(),
    'windspeed': df_reloaded.temperature.mean(),
    'event': 'No Event'
}, inplace=True)

print('Before = '+ str(df_reloaded.head()))


# or we can use forward fill based on previous value
# or we can use backward fill.
#########################
df_reloaded_2 = pd.read_csv('weather_data.csv',parse_dates=['day'])
# Axis column tells to copy from next column
df_reloaded_2 = df_reloaded_2.bfill(axis='columns')
print("=================================df_reloaded_2===================================")
print(df_reloaded_2)

#########################
df_reloaded_3 = pd.read_csv('weather_data.csv',parse_dates=['day'])
# Axis column tells to copy from next column
df_reloaded_3 = df_reloaded_3.ffill(axis='columns')
print("=================================df_reloaded_3===================================")
print(df_reloaded_3)


df_reloaded_4 = pd.read_csv('weather_data.csv',parse_dates=['day'])
# Interpolate uses two column values as average...
# only works on numeric values...
num_cols = df_reloaded_4.select_dtypes(include=['number']).columns
df_reloaded_4[num_cols] = df_reloaded_4[num_cols].interpolate(method='linear')

print('df_reloaded_4=\n' + str(df_reloaded_4))


# Example Drop NA rows altogether.
df_reloaded_5 = pd.read_csv('weather_data.csv',parse_dates=['day'])

#df_reloaded_5.dropna(how=all)
#Will delete at most 3 rows with N/A
df_reloaded_5 = df_reloaded_5.dropna(thresh=3)
print('df_reloaded_5\n='+ str(df_reloaded_5))