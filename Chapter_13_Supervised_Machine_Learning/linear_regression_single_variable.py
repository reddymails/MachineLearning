 #
 # Linear Regression Single Variable Tutorial
 #

import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("home_prices.csv")
df.head()

# Create linear regression model.
model = LinearRegression()

#Let's tell X and Y axis...
#We are training the model here on our data.
model.fit(df[['area_sqr_ft']], df['price_lakhs'])

# Note the double [[]] and single []
# model.fit(
#     df[['area_sqr_ft']],   # 2D → correct for X
#     df['price_lakhs']      # 1D → correct for y
# )

# Predicts for 2000 Sq feet
value = model.predict(pd.DataFrame({'area_sqr_ft': [2000]}))
print(' For 2000 sq feet land value in lakhs =', value)

value = model.predict(pd.DataFrame({'area_sqr_ft': [2000,1500,1000]}))
print(' For 2000 ,1500,100 sq feet land value in lakhs =', value)


# price = m * area + b
# The slope formula y =mx+c
print('M the slope=',model.coef_)
print('Constant C=',model.intercept_)

#Let's use the formula and see if that matches.
price = model.coef_ * 2000 + model.intercept_

print(' For 2000 sq feet using formula y = mx _+ c ', price)


