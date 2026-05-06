##################################################################
#
# Read and write XLS sheets
#
#################################################################

#####
# A simple method to convert different convention for US dollars
####
def standardize_currency(curr):
    if curr == 'US Dollars' or curr == '$' or curr == 'Dollars' :
        return "USD"
    return curr

import pandas as pd
from numpy.random.mtrand import standard_normal

pd.set_option('display.max_columns', None)
#df = pd.read_excel('Movies_MultiSheet.xlsx', sheet_name='Sheet1')
df_movies = pd.read_excel('Movies_MultiSheet.xlsx',sheet_name='movies')
print('head= \n'+ str(df_movies.head()))
print('#################################################################')
print('info=\n'+ str(df_movies.info()))
print('#################################################################')
print('Describe=\n'+ str(df_movies.describe()))
print('#################################################################')


df_financials = pd.read_excel('Movies_MultiSheet.xlsx',sheet_name='financials', index_col=1,
                              converters={'currency': standardize_currency})

print('Movie Financials = \n'+ str(df_financials.info()))
print('Movie Financials Header = \n'+ str(df_financials.head(20)))


# Merging two data frames using inner join.
df_merged = pd.merge(df_movies, df_financials, on='Movie_id', how='inner')

#print('Movie Financials = \n'+ str(df_merged))
df_merged.to_excel('Movies_MultiSheet_Merged.xlsx', sheet_name="merged", index=False)

df_stocks = pd.DataFrame({
  'Tickers':['GOOGL','NIVIDA','MSFT'],
  'Price':[845,65,64],
  'PE':[30.37,14.26,30.97],
  'EPS':[27.82,4.61,2.12]
})
df_stocks.to_excel('Stocks_Created_Using_DataFrame.xlsx', index=False,sheet_name="Stocks")


df_weather = pd.DataFrame({
  'Day':['1/1/2017','1/2/2017','1/3/2017'],
  'Temperature':[32,35,38],
  'Event':['Rain','Sunny','Snow']
})


###
## Lets write both data frames to one excel sheet.
###

with pd.ExcelWriter('Stocks_And_Weather_Using_DataFrame.xlsx') as writer:
    df_weather.to_excel(writer, index=False, sheet_name='Weather')
    df_stocks.to_excel(writer, index=False, sheet_name='Stocks')

