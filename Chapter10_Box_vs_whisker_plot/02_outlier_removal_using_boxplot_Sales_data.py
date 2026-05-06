################################################################
#  Outlier removal using Boxplot
#
#
#################################################################
import pandas as pd
import matplotlib.pyplot as plt

# make sure to install openpyxl using "pip install openpyxl" before running below code
df = pd.read_excel("region_wise_sales.xlsx")
print('df.head()= \n ',df.head())
#print('df= \n',df)

df_apac = df[df.Region=="APAC"]
df_europe = df[df.Region=="Europe"]
df_americas = df[df.Region=="Americas"]

# we can call this method for each region
def get_lower_upper(data):
    Q1, Q3 = data.Sales.quantile([0.25,0.75])
    IQR = Q3-Q1
    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR
    return lower, upper

lower_apac, upper_apac = get_lower_upper(df_apac)
lower_europe, upper_europe = get_lower_upper(df_europe)
lower_americas , upper_americas = get_lower_upper(df_americas)

print('df_europe.Sales.describe()=\n',df_europe.Sales.describe())
print('upper_europe= \n',upper_europe)

print('df_apac greater than upper_apac = \n',df_apac[df_apac.Sales > upper_apac])
print('df_europe greater than upper_europe = \n',df_europe[df_europe.Sales > upper_europe])
print('df_americas greater than upper_americas = \n',df_americas[df_americas.Sales > upper_americas])


labels = df['Region'].unique()
print('Region labels = \n',labels)

# You can basically extract Sale data for each Region from below line.
plot_data = [ df['Sales'] [df['Region'] == label].values for label in labels ]

#print(plot_data)
# BOX plot  Code...
plt.figure(figsize=(12, 8))
plt.boxplot(plot_data, tick_labels=labels, vert=True, patch_artist=True)
plt.title('Box plot of Sales by Region and Year')
plt.ylabel('Sales')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()


