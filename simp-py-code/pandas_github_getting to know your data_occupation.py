# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np

data_set = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'

# Step 3. Assign it to a variable called users and use the 'user_id' as index
users = pd.read_csv(data_set, sep='|', index_col = 'user_id')

# Step 4. See the first 25 entries
users.head(25)

# Step 5. See the last 10 entries
users.tail(10)