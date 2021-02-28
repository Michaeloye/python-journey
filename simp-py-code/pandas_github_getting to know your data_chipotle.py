import pandas as pd
import numpy as np
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'   
chipo = pd.read_csv(url, sep = '\t')
chipo.head(10)
chipo.shape[0]
chipo.shape[1]
chipo.columns
chipo.index

# Step 9. Which was the most-ordered item?
result = chipo.groupby('item_name').quantity.sum()
sorted_results = result.sort_values()
print(sorted_results)

# Step 11. What was the most ordered item in the choice_description column?
result = chipo.groupby('choice_description').quantity.sum()
sorted_results = result.sort_values()
print(result)

# Step 12. How many items were orderd in total
total_number_of_items = chipo.quantity.sum()
print(total_number_of_items)

# Step 13. Turn the item price into a float
dollarizer = lambda b: float(b[1:])
chipo.item_price = chipo.item_price.apply(dollarizer) # to make it reflect in the original dataframe
print(chipo.item_price)
chipo.item_price.dtype

# Step 14. How much was the revenue for the period in the dataset?
revenue = (chipo.quantity * chipo.item_price).sum() # sum is to add each revenue for each item
print(revenue)

# Step 15. How many orders were made in the period?
chipo.order_id.value_counts().count()