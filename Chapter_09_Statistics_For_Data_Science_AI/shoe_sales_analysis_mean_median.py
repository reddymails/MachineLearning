#######################
#  Calculate Mean and Median
#
########################

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("shoe_sales.csv")
print('head=\n', df.head(100))
print('Describe =\n', df.describe())
print('Shape(shape provides both row and column) =\n',df.shape)


#We see 12.25 in 25% percentile which means 25% of total values are less than 12.25
print('Below 25 percentile=',df.sold_qty[df.sold_qty<12.25].shape)


### (1) Nike sales analysis
#Pull Nike data
df_nike = df[df.brand=="Nike"]
print('df_nike  Shape = \n',df_nike.shape)

print('df_nike.head()=\n' , df_nike.head())

print('df_nike.describe() =\n', df_nike.describe())
print('df_nike.isnull().sum() =\n', df_nike.isnull().sum())


print('df_nike[df_nike.sold_qty.isnull() =\n',df_nike[df_nike.sold_qty.isnull()])

## **Now how should we fill NA values for sold_qty? Using median is one way**
print('df_nike.sold_qty.median() = \n',df_nike.sold_qty.median())

val = 0.0
df_nike['sold_qty'] = df_nike['sold_qty'].fillna(val)
print('df_nike.sold_qty.fillna(val, inplace=True) =',df_nike['sold_qty'])

print(' df_nike.isnull = \n', df_nike.isnull)


#%%
print(' df_nike.describe()==\n', df_nike.describe())

print('df_nike.sold_qty.sum()=\n', df_nike.sold_qty.sum())

#%% md
#### Nike Shoe Sales Insights

# 1. On average we sell 20 nike shoes per day
# 2. The daily sales range is 14 to 25
# 3. In september month we sold 590 adidas shoes

df_adidas = df[df.brand=="Adidas"]
print('df_adidas.shape =\n', df_adidas.shape)

print('df_adidas.head()=\n', df_adidas.head())
print('df_adidas.describe()=\n', df_adidas.describe())

#Plot graph of Nike and Adidas.
def plot_qty():
    plt.figure(figsize=(15, 6))

    dates = df_nike['date']

    plt.plot(dates, df_nike['sold_qty'], marker='o', label='Nike', color='blue')
    plt.plot(dates, df_adidas['sold_qty'], marker='o', label='Adidas', color='red')

    plt.xlabel('Date')
    plt.ylabel('Total Qty Sold')
    plt.title('Daily Sales Qty for Nike and Adidas in September 2023')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.show()

plot_qty()


print('df_adidas["sold_qty"].describe()=\n', df_adidas["sold_qty"].describe())

#75% percentile is 15.0, We will print all the values of about 75% percentile for manual examination
print('df_adidas[df.sold_qty>15] \n', df_adidas[df.sold_qty>15])


# We can clearly see that the sold quantity on 9/12/2023 is an outlier.
# Since this is one off outlier we can manually treat it and replace it with median value. In the subsequent lectures,
# we will explore better ways of handling outliers such as using standard deviation
df_adidas["sold_qty"]  = df_adidas["sold_qty"].replace(689, 12)

print('df_adidas[df.sold_qty>15]  After Replacing = \n', df_adidas[df.sold_qty>15])


print(' df_adidas["sold_qty"].describe() = \n', df_adidas["sold_qty"].describe())
print(' df_adidas["sold_qty"].sum() = ', df_adidas["sold_qty"].sum() )
print('\n')

#%% md
#### Adidas Shoe Sales Insights
#
# 1. On an average we sell 12 adidas shoes per day
# 2. The daily sales range is 7 to 19
# 3. In september month we sold 367 adidas shoes

# Since we fixed the outlier which is 689 for adidas now the graph looks much better
plot_qty()

#### Overall Insight is that Sales of Nike shoes are higher than Adidas on any given date one we fixed the outlier.

# Sometimes instead of printing entire data set say you want to exclude 9% of values. Here is the trck using quantile.
print(' Adidas  Quantile greater than 95% =\n', df_adidas["sold_qty"].quantile(0.95))
# It printed this ====> Adidas Quantile greater than 95 % = 17.549999999999997

print('df_adidas[df_adidas["sold_qty"] > 17.54]=\n',df_adidas[df_adidas["sold_qty"] > 17.54])