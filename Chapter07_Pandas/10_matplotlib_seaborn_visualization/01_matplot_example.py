#########################
#
#
#
########################

import pandas as pd
from matplotlib import pyplot as plt

df_sales = pd.read_excel("linechart.xlsx")
print(df_sales.head())

# Specify the size of the graph and , x,y, axis data.
plt.figure(figsize=(12,4))
plt.plot(df_sales["Quarter"], df_sales["Fridge"], color="blue", label="Fridge")
plt.plot(df_sales["Quarter"], df_sales["Dishwasher"], color="orange", label="Dishwasher")
plt.plot(df_sales["Quarter"], df_sales["Washing Machine"], color="green", label="Washing Machine")
plt.title("Product Sales")
plt.xlabel("Quarter")
plt.ylabel("Million $")

# Prints legen on top
plt.legend()

plt.show()


# total sales.
total_sales = df_sales[["Fridge","Dishwasher","Washing Machine"]].sum()
print('total_sales=\n',total_sales)
# Will print Fridge,Dishwasher etc.
print('total_sales.index=\n',total_sales.index)

# Pie chart
# shadow=True  <== Gives that 3d effect
plt.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%', startangle=140, explode=(0.1,0,0), shadow=True)
plt.show()


# Bar chart
df_sales.plot(kind="bar", x="Quarter")
plt.xticks(rotation=45)
plt.show()

#To use Quarters as X axis, we can set them as an index on a dataframe and then use plot function
df_sales_2 = df_sales.set_index("Quarter")
print('df_sales_2=\n',df_sales_2)

df_sales_2.plot(kind="bar")
plt.xticks(rotation=45)
plt.show()

df_sales_2.plot(kind="barh")
plt.show()

df_score = pd.read_excel("histograms.xlsx")
print(df_score.head())

plt.hist(df_score["Exam_Score"], density=True)
#without this it will not even display
plt.show()


#Using seaborn for histogram which has much better appeal.
import seaborn as sns
# KDE - Kernal Density Estimator will draw a line on top of the bars.
sns.histplot(df_score["Exam_Score"], kde=True)
plt.xlabel("Score")
plt.ylabel("Count")
plt.title("Exam Scores")
plt.show()


#Scatter Plot puts dots on screen
df = pd.read_excel("scatter_plot.xlsx")
sns.scatterplot(data=df, x="area_square_ft", y="price")
plt.show()


