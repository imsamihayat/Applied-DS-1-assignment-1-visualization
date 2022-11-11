#importing the required libraries
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None, 'display.max_columns', None)

#importing the csv file
df = pd.read_csv('Cleaned_Laptop_data.csv')

df.head()

df.info()

df.isna().sum()

df.dropna(inplace=True)

df.head()

df_brands = df[df['processor_brand'].isin(['Intel', 'AMD', 'Apple'])]

def line_plot_brands(brand_names, data):
  
#The function is created which takes the input of processor brands names in the form of list and shows the line plot of each brand with distinct line between the number of reviews and ratings.
  df_brands = data[data['processor_brand'].isin(brand_names)]
  df_brands.groupby('processor_brand')['ratings'].mean().sort_values().plot(kind='line', label='Ratings')
  df_brands.groupby('processor_brand')['reviews'].mean().sort_values().plot(kind='line', label='Reviews')
  plt.legend()
  plt.title('Average Ratings VS Reviews in brands')
  plt.show()

line_plot_brands(['Intel', 'AMD', 'Apple'], df)

def bar_plot(brand_names, data):
  
  #This function will give us the bar plot of star ratings column
  df_brands = data[data['processor_brand'].isin(brand_names)]
  df_brands.groupby('processor_brand')['star_rating'].mean().plot(kind='bar')
  plt.title('Bar plot of  Ratings')
  plt.show()

bar_plot(['Intel', 'AMD', 'Apple'], df)

def scatter_plot(col1, col2, data):
  #This function will plot the scatter plot of two given columns in the dataset to show the linearity between them
  plt.scatter(x=data[col1], y=data[col2])
  plt.title('Scatter plot showing the relationship between {} and {}'.format(col1,col2))
  plt.xlabel('Ratings')
  plt.ylabel('Reviews')
  plt.show()

scatter_plot('ratings', 'reviews',df)

