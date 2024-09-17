import pandas as pd
import matplotlib.pyplot as plt
# Load the Open Food Facts dataset from a TSV file
df_food = pd.read_csv('en.openfoodfacts.org.products.tsv', sep='\t', low_memory=False)

# Get all the columns in the DataFrame
all_columns = df_food.columns
df_food['product_name'].fillna('', inplace=True)
columns = ['product_name','generic_name','quantity','packaging','brands','categories_en','countries_en','ingredients_text','traces','additives','main_category_en','energy_100g','fat_100g','saturated-fat_100g','carbohydrates_100g','sugars_100g','fiber_100g','proteins_100g','salt_100g','cocoa_100g','trans-fat_100g','manufacturing_places','image_small_url']

organic = df_food[df_food['categories_en'].str.contains('organic', case=False, na=False)][columns]


# Filter out rows with missing 'main_category_en' values
#filtered = organic.dropna(subset=['main_category_en'])

"""
# Count occurrences of each category
category_counts = filtered['main_category_en'].value_counts()

# Plotting the pie chart without labels
plt.figure(figsize=(8, 8))
plt.pie(category_counts, autopct='', startangle=140)
plt.title('Distribution of Organic Food Categories')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Add legend
plt.legend(category_counts.index, loc='best')

plt.show()
"""
"""
plt.hist(organic['carbohydrates_100g'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Carbohydrates Percentages in Organic Foods')
plt.xlabel('Carbs Percentage')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()

"""

# Count rows for each country where dark chocolate products are sold
split = organic.assign(countries_en=organic['countries_en'].str.split(','))
exploded = split.explode('countries_en')
country_counts = exploded['countries_en'].value_counts()

# Plot the distribution of dark chocolate products by country
#plt.figure(figsize=(15, 8))
country_counts.plot(kind='bar', color='skyblue')
plt.title('Distribution of Organic Products Sold in each Country')
plt.xlabel('Country')
plt.ylabel('Number of Organic Products')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()