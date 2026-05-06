#
# Linear Regression Multiple  Variable Tutorial
#
#  y= m1 * x1 + m2 * x2 + C
#
#

import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("home_prices_with_bedrooms.csv")
print( df.sample(5) )
print( df.size )

print('df[["area_sqr_ft"]]=', df[["area_sqr_ft"]])
print('df["price_lakhs"]=', df["price_lakhs"])

model = LinearRegression()
#Note  the first argument is 2d array and second argument is one dimensional array.
# Train the model.
model.fit(df[["area_sqr_ft","bedrooms"]], df["price_lakhs"])

value = model.predict(pd.DataFrame({'area_sqr_ft': [2000] , 'bedrooms': [4]}))
print('2000 sq feet home with 4 beds =',value)

value = model.predict(pd.DataFrame({'area_sqr_ft': [1000] , 'bedrooms': [3]}))
print('1000 sq feet home with 3 beds =',value)


#y= m1 * x1 + m2 * x2 + C
# price = m1 * area + m2 * bedrooms + C
print('M1 the slope=',model.coef_[0])
print('M2 the slope=',model.coef_[1])
print('Constant C=',model.intercept_)

# 1000 sq feet home with 3 bedrooms.
price  = model.coef_[0]  * 1000 +  model.coef_[1] * 3 + model.intercept_
print('1000 sq feet home with 3 beds  using  price = m1 * area + m2 * bedrooms + C =',value)
