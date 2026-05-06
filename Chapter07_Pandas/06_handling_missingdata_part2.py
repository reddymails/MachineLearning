###################################################################
#   Data transformation when loading excel and
#  More replace options for unwanted data - Data Translation.
#
#
#####################################################################
import numpy as np
import pandas as pd

pd.set_option('display.max_columns',None)
df = pd.read_csv("weather_data_2.csv")

print('df=\n'+ str(df))
# Will replace all -99999 to 0.
df_temp = df.replace(-99999, 0)
print(' Replacing -99999 with 0=\n'+ str(df_temp))


df_temp = df.replace([-99999,-88888], value=np.nan)
print('Replacing -99999 and -88888 with nan=\n'+ str(df_temp))


df_temp = df.replace({
    'temperature':-99999,
    'windspeed':[-99999,-88888],
    'event':'no event'
    }, np.nan)
print('Replacing Defaults By listing  columns and values with  nan=\n'+ str(df_temp))


df_temp = df.replace({
    -99999: np.nan,
    -88888:np.nan,
    'no event':'sunnyyyyyyyyyyyy'
    })
print('Replacing Defaults By listing  Just values with  nan=\n'+ str(df_temp))



# Let's Create a DataFrame.
df_student = pd.DataFrame({
    'Score' : ['Grade-A','Grade-B','Grade-C','Grade-A','Grade-A','Grade-A'],
    'Student' : ['Joe','Jefferson','Mr R','Ram','Raj','Rob']
})

print('df_student=\n'+ str(df_student))

df_student_temp = df_student.replace(['Grade-A','Grade-B','Grade-C'], [100,90,80])

print('df_student Grades to Marks =\n'+ str(df_student_temp))


df.to_csv('student_data.csv',index=False)

print(" Saved  Student data to student_data")