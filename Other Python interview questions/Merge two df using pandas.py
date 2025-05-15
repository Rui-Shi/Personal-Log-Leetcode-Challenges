# Given two tables : Bob 50  |  Bob 5000 how to make it as Bob | 5000 as one table using pandas.

import pandas as pd

# Assume your two pieces of data can be represented as DataFrames.
# Let's say:
# Table 1 might also have other entries
data1 = {'Name': ['Alice', 'Bob'], 'Value': [100, 50]}
df1 = pd.DataFrame(data1)

# Table 2 contains the overriding value for Bob and potentially other entries
data2 = {'Name': ['Bob', 'Charlie'], 'Value': [5000, 200]}
df2 = pd.DataFrame(data2)

print("DataFrame 1 (df1):")
print(df1)
print("\nDataFrame 2 (df2):")
print(df2)

# --- Method: Concatenate and Drop Duplicates ---
# This method is straightforward if the column names are the same
# and you want the values from the second DataFrame to take precedence
# for common keys.

# 1. Concatenate the two DataFrames.
# df2 is appended to df1.
combined_df = pd.concat([df1, df2], ignore_index=True)
print("\nCombined DataFrame (before dropping duplicates):")
print(combined_df)

# 2. Drop duplicates based on the 'Name' column.
# 'keep="last"' ensures that if there are duplicate 'Name' entries (like 'Bob'),
# the one from the DataFrame that was last in the concatenation (df2) is kept.
result_df = combined_df.drop_duplicates(subset=['Name'], keep='last')
print("\nFinal Resulting DataFrame:")
print(result_df)

# Specifically for the "Bob | 5000" case:
# If df1 was just {'Name': ['Bob'], 'Value': [50]}
# and df2 was {'Name': ['Bob'], 'Value': [5000]}
# The result_df would correctly be:
#   Name  Value
# 0  Bob   5000

# --- Alternative: Merge and Combine (more flexible for different column names) ---
# If the value columns had different names, or for more complex logic,
# you might use a merge.

# Resetting df1 and df2 for this example
df1 = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Value_StoreA': [100, 50]})
df2 = pd.DataFrame({'Name': ['Bob', 'Charlie'], 'Value_StoreB': [5000, 200]})

# left merge to keep all names from left DataFrames
merged_df = pd.merge(df1, df2, on='Name', how='left')
print("\nleft Merge:")
print(merged_df)

# right merge to keep all names from right DataFrames
merged_df = pd.merge(df1, df2, on='Name', how='right')
print("\nright Merge:")
print(merged_df)

# inner merge to keep the names from both DataFrames
merged_df = pd.merge(df1, df2, on='Name', how='inner')
print("\ninner Merge::")
print(merged_df)

# Outer merge to keep all names from both DataFrames
merged_df = pd.merge(df1, df2, on='Name', how='outer')
print("\nouter Merge::")
print(merged_df)

# Combine the value columns, giving preference to Value_StoreB (from df2)
# .combine_first() fills NaN values in 'Value_StoreB' with values from 'Value_StoreA'
merged_df['FinalValue'] = merged_df['Value_StoreB'].combine_first(merged_df['Value_StoreA'])

result_alternative_df = merged_df[['Name', 'FinalValue']]
print("\nFinal Resulting DataFrame (alternative method):")
print(result_alternative_df)
# This would give:
#       Name  FinalValue
# 0    Alice       100.0
# 1      Bob      5000.0
# 2  Charlie       200.0
# Which for the specific case of Bob, yields Bob | 5000.0

