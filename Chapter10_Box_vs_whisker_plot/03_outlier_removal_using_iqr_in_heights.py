#########################################################
#  Outlier removal using
# Box plot and IQR ()
#
# The Interquartile Range (IQR) is a measure of statistical dispersion that represents the spread of the middle 50% of a dataset.
# It is calculated by subtracting the first quartile ( 25th percentile) from the third quartile ( 75th percentile), giving the formula:
# IQR = Q3 - Q1
#
# Outlier Detection: The formula 1.5 * IQR  is used to determine if data points are outliers.
########################################################
import pandas as pd
df = pd.read_csv("heights.csv")
df.head()

#Calcualte  first and third Quartile.
Q1, Q3 = df.height.quantile([0.25,0.75])
IQR = Q3-Q1

print('IQR=',IQR)

#Outlier Detection: The formula 1.5 * IQR
lower = Q1-1.5 * IQR
upper = Q3+1.5 * IQR


print('df_before_cleaning=',df)
#Data frame with outliers removed.
df_clean = df[(df.height>lower)&(df.height<upper)]
print('df_clean=',df_clean)

