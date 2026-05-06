##############################
#
# Mean, Median and Mode calculations.
# If we have   40,40,40,50,60,80,90
#
#  Mean = Sum of all/ number of elements
#       = 400/7= 57.14
#  Mode = most appearing element here its 40
#  Median = Middle element , in this case its 50.
#  However if you have even number of elements, take the average of the two middle elements
#  divide them by 2.
#
################################
import pandas as pd

df_movies = pd.read_excel("movies_stats1.xlsx", sheet_name="financials")
print(df_movies.head())
df_movies['revenue']
