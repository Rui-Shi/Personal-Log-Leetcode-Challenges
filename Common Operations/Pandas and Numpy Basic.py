import numpy as np
import pandas as pd
import os # Needed for file cleanup example

# --- NumPy Common Operations ---

# --- 1. Creating Arrays ---
# From a Python list
list_a = [1, 2, 3, 4, 5]
np_array_a = np.array(list_a)
# np_array_a: array([1, 2, 3, 4, 5])
# type(np_array_a): <class 'numpy.ndarray'>

# Array of zeros
zeros_array = np.zeros((2, 3)) # Shape (2 rows, 3 columns)
# zeros_array:
# array([[0., 0., 0.],
#        [0., 0., 0.]])

# Array of ones
ones_array = np.ones((3, 2), dtype=int) # Specify data type
# ones_array:
# array([[1, 1],
#        [1, 1],
#        [1, 1]])

# Array with a range of values (like Python's range)
range_array = np.arange(0, 10, 2) # Start, Stop (exclusive), Step
# range_array: array([0, 2, 4, 6, 8])

# Array with evenly spaced values
linspace_array = np.linspace(0, 1, 5) # Start, Stop (inclusive), Number of points
# linspace_array: array([0.  , 0.25, 0.5 , 0.75, 1.  ])

# Random array (uniform distribution between 0 and 1)
random_array = np.random.rand(2, 2)
# random_array: e.g., array([[0.123, 0.456], [0.789, 0.012]]) # Values will vary

# Random array (standard normal distribution)
randn_array = np.random.randn(2, 2)
# randn_array: e.g., array([[ 0.5, -1.2], [ 1.8,  0.1]]) # Values will vary

# Random integers
randint_array = np.random.randint(1, 100, size=(2, 3)) # Low (inclusive), High (exclusive), Size
# randint_array: e.g., array([[45, 12, 88], [23, 91, 5 ]]) # Values will vary


# --- 2. Inspecting Array Properties ---
data = np.array([[1, 2, 3], [4, 5, 6]])
# data: array([[1, 2, 3], [4, 5, 6]])
data_shape = data.shape # (2, 3) -> 2 rows, 3 columns
data_ndim = data.ndim   # 2 -> Number of dimensions
data_dtype = data.dtype # dtype('int64') or dtype('int32') depending on system
data_size = data.size   # 6 -> Total number of elements


# --- 3. Indexing and Slicing ---
arr = np.arange(10, 20)
# arr: array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

# Get a single element (index starts at 0)
element_3 = arr[3] # 13

# Slice: Get elements from index 2 up to (not including) index 5
slice_2_5 = arr[2:5] # array([12, 13, 14])

# Slice from the beginning up to index 4
slice_to_4 = arr[:4] # array([10, 11, 12, 13])

# Slice from index 5 to the end
slice_from_5 = arr[5:] # array([15, 16, 17, 18, 19])

# Multi-dimensional array indexing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# arr2d:
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])

# Get element at row 1, column 2
element_1_2 = arr2d[1, 2] # 6
element_1_2_alt = arr2d[1][2] # 6

# Get a slice of rows and columns
# Rows 0 and 1, Columns 1 and 2
slice_2d = arr2d[0:2, 1:3]
# slice_2d:
# array([[2, 3],
#        [5, 6]])

# Get a specific row
row_1 = arr2d[1, :] # array([4, 5, 6])
row_1_alt = arr2d[1] # array([4, 5, 6])


# --- 4. Boolean Indexing ---
arr_bool = np.array([10, 5, 25, 15, 30])
# arr_bool: array([10,  5, 25, 15, 30])

# Create a boolean mask
mask = arr_bool > 15 # array([False, False,  True, False,  True])

# Apply the mask to select elements
elements_gt_15 = arr_bool[mask] # array([25, 30])

# Combine conditions (& for AND, | for OR)
mask_combined = (arr_bool > 10) & (arr_bool < 30) # array([False, False,  True,  True, False])
elements_combined = arr_bool[mask_combined] # array([25, 15])


# --- 5. Mathematical Operations ---
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# arr1: array([1, 2, 3])
# arr2: array([4, 5, 6])

# Element-wise addition
add_result = arr1 + arr2 # array([5, 7, 9])

# Element-wise subtraction
sub_result = arr1 - arr2 # array([-3, -3, -3])

# Element-wise multiplication
mul_result = arr1 * arr2 # array([ 4, 10, 18])

# Element-wise division
div_result = arr1 / arr2 # array([0.25, 0.4 , 0.5 ])

# Scalar operations (broadcasted)
scalar_mul_result = arr1 * 3 # array([3, 6, 9])

# Universal Functions (ufuncs)
sqrt_result = np.sqrt(arr1) # array([1.        , 1.41421356, 1.73205081])
exp_result = np.exp(arr1)   # array([ 2.71828183,  7.3890561 , 20.08553692])
sin_result = np.sin(arr1)   # array([0.84147098, 0.90929743, 0.14112001])


# --- 6. Aggregation Functions ---
arr_agg = np.array([[1, 2, 3], [4, 5, 6]])
# arr_agg: array([[1, 2, 3], [4, 5, 6]])

sum_all = np.sum(arr_agg) # 21
mean_all = np.mean(arr_agg) # 3.5
min_val = np.min(arr_agg) # 1
max_val = np.max(arr_agg) # 6
std_dev = np.std(arr_agg) # 1.707825127659933

# Aggregation along axes
# axis=0: Aggregate along columns (collapse rows)
sum_axis0 = np.sum(arr_agg, axis=0) # array([5, 7, 9])
# axis=1: Aggregate along rows (collapse columns)
mean_axis1 = np.mean(arr_agg, axis=1) # array([2., 5.])


# --- 7. Reshaping Arrays ---
arr_reshape = np.arange(1, 13) # 1 to 12
# arr_reshape: array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])

# Reshape to a 3x4 matrix
reshaped_arr = arr_reshape.reshape((3, 4))
# reshaped_arr:
# array([[ 1,  2,  3,  4],
#        [ 5,  6,  7,  8],
#        [ 9, 10, 11, 12]])

# Reshape to a 4x3 matrix
reshaped_arr_2 = arr_reshape.reshape((4, 3))
# reshaped_arr_2:
# array([[ 1,  2,  3],
#        [ 4,  5,  6],
#        [ 7,  8,  9],
#        [10, 11, 12]])

# Flatten the array (back to 1D)
flattened_arr = reshaped_arr.flatten()
# flattened_arr: array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
# raveled_arr = reshaped_arr.ravel() # Similar to flatten


# --- 8. Combining Arrays ---
arr_comb1 = np.array([[1, 2], [3, 4]])
arr_comb2 = np.array([[5, 6], [7, 8]])
# arr_comb1: array([[1, 2], [3, 4]])
# arr_comb2: array([[5, 6], [7, 8]])

# Concatenate along rows (axis=0)
vstacked = np.vstack((arr_comb1, arr_comb2))
# vstacked:
# array([[1, 2],
#        [3, 4],
#        [5, 6],
#        [7, 8]])
concatenated_axis0 = np.concatenate((arr_comb1, arr_comb2), axis=0) # Equivalent

# Concatenate along columns (axis=1)
hstacked = np.hstack((arr_comb1, arr_comb2))
# hstacked:
# array([[1, 2, 5, 6],
#        [3, 4, 7, 8]])
concatenated_axis1 = np.concatenate((arr_comb1, arr_comb2), axis=1) # Equivalent


# --- Pandas Common Operations ---

# --- 1. Creating Series and DataFrames ---
# Creating a Series from a list (index defaults to 0, 1, 2...)
s = pd.Series([10, 20, 30, 40], name='MyNumbers')
# s:
# 0    10
# 1    20
# 2    30
# 3    40
# Name: MyNumbers, dtype: int64

# Creating a Series with a custom index
s_custom_index = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
# s_custom_index:
# a    10
# b    20
# c    30
# dtype: int64

# Creating a DataFrame from a dictionary of lists
data_dict = {'col1': [1, 2, 3, 4],
             'col2': ['A', 'B', 'C', 'D'],
             'col3': [True, False, True, False]}
df = pd.DataFrame(data_dict)
# df:
#    col1 col2   col3
# 0     1    A   True
# 1     2    B  False
# 2     3    C   True
# 3     4    D  False

# Creating a DataFrame with a custom index
df_custom_index = pd.DataFrame(data_dict, index=['row1', 'row2', 'row3', 'row4'])
# df_custom_index:
#       col1 col2   col3
# row1     1    A   True
# row2     2    B  False
# row3     3    C   True
# row4     4    D  False

# Creating a DataFrame from a NumPy array
np_data = np.random.randint(0, 10, size=(3, 4))
df_from_np = pd.DataFrame(np_data, columns=['W', 'X', 'Y', 'Z'])
# df_from_np: e.g.
#    W  X  Y  Z
# 0  5  8  7  3
# 1  6  5  0  1
# 2  5  9  8  4


# --- 2. Reading and Writing Data ---
# Example: Create dummy data
data_to_write = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df_write_example = pd.DataFrame(data_to_write)

# Writing to CSV (creates 'output.csv')
# df_write_example.to_csv('output.csv', index=False) # Command to write to CSV

# Reading from CSV (reads 'output.csv')
# df_read = pd.read_csv('output.csv') # Command to read from CSV
# df_read would contain the data from 'output.csv'

# Writing to Excel (requires 'openpyxl')
# df_write_example.to_excel('output.xlsx', sheet_name='Sheet1', index=False) # Command to write to Excel

# Reading from Excel
# df_read_excel = pd.read_excel('output.xlsx', sheet_name='Sheet1') # Command to read from Excel
# df_read_excel would contain the data from 'output.xlsx' Sheet1

# Clean up example files if they were created
try: os.remove('output.csv')
except FileNotFoundError: pass
try: os.remove('output.xlsx')
except FileNotFoundError: pass


# --- 3. Inspecting Data ---
# Recreate a sample DataFrame
data_inspect = {'colA': np.random.rand(5),
                'colB': ['X', 'Y', 'X', 'Z', 'Y'],
                'colC': np.random.randint(1, 10, 5),
                'colD': [np.nan, 1.0, 2.5, np.nan, 3.0]} # Add some missing data
df_inspect = pd.DataFrame(data_inspect)
# df_inspect: Contains random floats, strings, ints, and NaNs

# View top rows (default 5)
top_3_rows = df_inspect.head(3) # DataFrame containing first 3 rows

# View bottom rows (default 5)
bottom_2_rows = df_inspect.tail(2) # DataFrame containing last 2 rows

# Get concise summary (index, columns, non-null counts, dtypes, memory usage)
# df_inspect.info() # Prints a summary to console - no direct variable assignment

# Get descriptive statistics for numerical columns
desc_stats = df_inspect.describe() # DataFrame with count, mean, std, min, max, etc. for numeric columns

# Get dimensions (rows, columns)
df_shape = df_inspect.shape # Tuple (e.g., (5, 4))

# Get column names
df_columns = df_inspect.columns # Index(['colA', 'colB', 'colC', 'colD'], dtype='object')

# Get index labels
df_index = df_inspect.index # RangeIndex(start=0, stop=5, step=1)

# Get data types of columns
df_dtypes = df_inspect.dtypes
# df_dtypes:
# colA    float64
# colB     object
# colC      int64 or int32
# colD    float64
# dtype: object


# --- 4. Selection and Indexing ---
# Use the df_inspect DataFrame

# Select a single column (returns a Series)
colB_series = df_inspect['colB'] # Series containing values from 'colB'

# Select multiple columns (returns a DataFrame)
cols_A_C_df = df_inspect[['colA', 'colC']] # DataFrame with only 'colA' and 'colC'

# --- Row Selection ---
# Select row(s) by label (index name) using .loc
row_label_2 = df_inspect.loc[2] # Series representing row with index label 2
rows_label_1_3 = df_inspect.loc[[1, 3]] # DataFrame with rows labeled 1 and 3

# Select row(s) by integer position using .iloc
row_pos_0 = df_inspect.iloc[0] # Series representing row at position 0
rows_pos_0_1 = df_inspect.iloc[0:2] # DataFrame with rows at position 0 and 1

# --- Selecting Rows and Columns Simultaneously ---
# Using .loc (labels for both row and column)
subset_loc = df_inspect.loc[[1, 3], ['colB', 'colD']] # DataFrame slice using labels

# Using .iloc (integer positions for both row and column)
# Rows at position 0, 2 and Columns at position 1, 3
subset_iloc = df_inspect.iloc[[0, 2], [1, 3]] # DataFrame slice using integer positions

# --- Conditional Selection (Boolean Indexing) ---
rows_C_gt_5 = df_inspect[df_inspect['colC'] > 5] # DataFrame where 'colC' > 5
rows_B_is_Y = df_inspect[df_inspect['colB'] == 'Y'] # DataFrame where 'colB' is 'Y'

# Combine conditions
rows_B_Y_C_lt_8 = df_inspect[(df_inspect['colB'] == 'Y') & (df_inspect['colC'] < 8)]


# --- 5. Data Cleaning ---
# Use df_inspect which has NaN values in 'colD'

# Check for missing values (returns boolean DataFrame)
is_null_df = df_inspect.isnull() # DataFrame of True/False indicating NaNs

# Count missing values per column
nan_counts = df_inspect.isnull().sum()
# nan_counts:
# colA    0
# colB    0
# colC    0
# colD    2
# dtype: int64

# Drop rows containing any NaN values
df_dropped_rows = df_inspect.dropna() # Returns DataFrame with rows containing NaNs removed

# Drop columns containing any NaN values
df_dropped_cols = df_inspect.dropna(axis=1) # Returns DataFrame with columns containing NaNs removed ('colD' would be dropped)

# Fill NaN values with a specific value (e.g., 0 or the mean)
mean_colD = df_inspect['colD'].mean() # Calculate mean of 'colD' ignoring NaNs
df_filled = df_inspect.fillna(value={'colD': mean_colD}) # Fill only NaNs in colD with calculated mean

# Rename columns
df_renamed = df_inspect.rename(columns={'colA': 'Alpha', 'colB': 'Beta'}) # Returns DataFrame with 'colA'/'colB' renamed

# Drop columns/rows by label
df_dropped_specific_col = df_inspect.drop('colA', axis=1) # Drop column 'colA'
df_dropped_specific_rows = df_inspect.drop([0, 2], axis=0) # Drop rows with index 0 and 2


# --- 6. Data Manipulation ---
# Use the cleaned df_filled DataFrame (where NaNs in colD were filled)

# Add a new column calculated from existing ones
df_filled['colE'] = df_filled['colC'] * 10 # Adds 'colE' to df_filled

# Apply a function to a column (e.g., square values in 'colC')
df_filled['colC_squared'] = df_filled['colC'].apply(lambda x: x**2) # Adds 'colC_squared'

# Get unique values in a column
unique_colB = df_filled['colB'].unique() # Numpy array of unique values in 'colB' (e.g., array(['X', 'Y', 'Z'], dtype=object))

# Count unique values in a column
value_counts_colB = df_filled['colB'].value_counts()
# value_counts_colB: Series mapping unique values to their counts
# e.g.,
# X    2
# Y    2
# Z    1
# Name: colB, dtype: int64

# Sort DataFrame by values in a column
df_sorted_by_C = df_filled.sort_values(by='colC', ascending=False) # Sorts rows based on 'colC' values

# Sort DataFrame by index
df_sorted_by_index = df_filled.sort_index(ascending=False) # Sorts rows based on index labels


# --- 7. Grouping and Aggregation (`groupby`) ---
# Use the df_filled DataFrame

# Group by 'colB' and calculate the mean of other numerical columns for each group
grouped_mean = df_filled.groupby('colB').mean(numeric_only=True)
# grouped_mean: DataFrame where index is unique 'colB' values, columns are original numeric cols, values are means per group

# Group by 'colB' and calculate the sum
grouped_sum = df_filled.groupby('colB').sum(numeric_only=True)
# grouped_sum: DataFrame similar to mean, but values are sums per group

# Group by 'colB' and count occurrences in each group (size includes NaNs, count excludes)
grouped_count = df_filled.groupby('colB').size() # Series where index is unique 'colB' values, values are counts per group
# grouped_count_nonan = df_filled.groupby('colB').count() # DataFrame of counts per original column for each group

# Group by 'colB' and apply multiple aggregation functions
grouped_agg = df_filled.groupby('colB').agg(
    {'colA': ['mean', 'std'], 'colC': ['min', 'max', 'sum']} # Specify aggregations per column
)
# grouped_agg: DataFrame with multi-level columns representing the specified aggregations per group


# --- 8. Merging, Joining, and Concatenating ---
# Sample DataFrames for combining
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                    'B': ['B0', 'B1', 'B2'],
                    'key': ['K0', 'K1', 'K2']})

df2 = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                    'D': ['D0', 'D1', 'D2'],
                    'key': ['K0', 'K1', 'K3']}) # Note K3 doesn't match df1

df3 = pd.DataFrame({'A': ['A3', 'A4', 'A5'],
                    'B': ['B3', 'B4', 'B5'],
                    'key': ['K3', 'K4', 'K5']})

# Concatenation (stacking DataFrames vertically or horizontally)
# Stacking vertically (default axis=0)
concatenated_df = pd.concat([df1, df3], ignore_index=True) # ignore_index resets the index
# concatenated_df: df1 stacked on top of df3

# Merging (SQL-style joins based on common columns or indices)
# Inner join (only keep matching keys: K0, K1)
merged_inner = pd.merge(df1, df2, on='key', how='inner')
# merged_inner: Contains combined columns for rows where 'key' exists in both df1 and df2

# Left join (keep all keys from df1: K0, K1, K2; match from df2 where possible)
merged_left = pd.merge(df1, df2, on='key', how='left')
# merged_left: Contains all rows from df1, with matched data from df2 (NaNs where no match for 'key')

# Right join (keep all keys from df2: K0, K1, K3; match from df1 where possible)
merged_right = pd.merge(df1, df2, on='key', how='right')
# merged_right: Contains all rows from df2, with matched data from df1 (NaNs where no match for 'key')

# Outer join (keep all keys from both: K0, K1, K2, K3)
merged_outer = pd.merge(df1, df2, on='key', how='outer')
# merged_outer: Contains all rows from both df1 and df2, with NaNs where keys don't exist in the other DataFrame

# Joining (convenience method for merging based on indices)
# Set index first for a meaningful join example
df_left = pd.DataFrame({'X': ['X0', 'X1'], 'Y': ['Y0', 'Y1']}, index=['idx0', 'idx1'])
df_right = pd.DataFrame({'Z': ['Z0', 'Z2']}, index=['idx0', 'idx2'])

# Outer join on index (keeps idx0, idx1, idx2)
joined_df = df_left.join(df_right, how='outer')
# joined_df: Contains columns from both, aligned by index labels, using an outer join strategy