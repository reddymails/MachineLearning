#####################
# Read CSV file . Skip first row as its not the header
#
#####################


import pandas as pd

pd.set_option('display.max_columns', None)
# you can skip first row,
#df = pd.read_csv('Stock_data.csv', skiprows=1)
# or you can tell where the header is.
df = pd.read_csv('Stock_data.csv', header=1)

print(df.head(5))

# Adding custom columns
# Original :  tickers  eps  revenue price  people

df = pd.read_csv('Stock_data.csv', header=1, names=['Stock Symbol', 'Earnings per share', 'revenue', 'Price', 'CEO names'])
print(df.head(2))

# Or we can use num rows.
df = pd.read_csv('Stock_data.csv', header=1, nrows=3)
print(df)

#We can replace 'not available' to something meaning full.
# Here in EPS column when we see 'not available ' the system will print NaN
# Same in revenue column
df = pd.read_csv('Stock_data.csv', header=1, na_values={
    'eps':['not available'],
    'revenue':[-1]
})
print(df)

# Or we can list all values to be treated differently  at once.
df = pd.read_csv('Stock_data.csv', header=1, na_values={'not available',-1,'n.a.'} )
print(df)

# Creating new dervied column.
df["PE"] = df['price']/df['eps']
print(' WITH P/E=\n' + str(df))

df.to_csv('Stock_data_with_PE.csv', index=False)
