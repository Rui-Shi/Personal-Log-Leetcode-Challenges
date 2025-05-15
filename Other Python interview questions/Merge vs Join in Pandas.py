# Use merge() for column-based joins and more complex, SQL-like scenarios due to its greater flexibility.
# Use DataFrame.join() for simpler index-based joins or when joining a DataFrame's column to another DataFrame's index.

import pandas as pd

# --- Sample DataFrames ---

# Employees DataFrame
employees_data = {
    'employee_id': [101, 102, 103, 104, 105, 106],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'department_id': [1, 2, 1, 3, 2, 4] # Department 4 doesn't exist in departments_df
}
employees_df = pd.DataFrame(employees_data)
print("--- Employees DataFrame (employees_df) ---")
print(employees_df)
print("-" * 40)

# Departments DataFrame (department_id as a regular column)
departments_data_col = {
    'department_id': [1, 2, 3, 5], # Department 5 doesn't have employees
    'department_name': ['HR', 'Engineering', 'Sales', 'Marketing'],
    'location': ['New York', 'San Francisco', 'Chicago', 'Boston']
}
departments_df_col = pd.DataFrame(departments_data_col)
print("--- Departments DataFrame with Column Key (departments_df_col) ---")
print(departments_df_col)
print("-" * 40)

# Departments DataFrame (department_id as index)
departments_data_idx = {
    'department_name': ['HR', 'Engineering', 'Sales', 'Marketing'],
    'location': ['New York', 'San Francisco', 'Chicago', 'Boston']
}
# Use department_id values from departments_df_col as index
departments_df_idx = pd.DataFrame(departments_data_idx, index=pd.Index([1, 2, 3, 5], name='department_id'))
print("--- Departments DataFrame with Index Key (departments_df_idx) ---")
print(departments_df_idx)
print("-" * 40)

# Salaries DataFrame (employee_id as index)
salaries_data = {
    'salary': [70000, 85000, 72000, 90000, 65000] # Salary for employee 105 missing
}
# Use employee_id values from employees_df (excluding one) as index
salaries_df_idx = pd.DataFrame(salaries_data, index=pd.Index([101, 102, 103, 104, 106], name='employee_id'))
print("--- Salaries DataFrame with Index Key (salaries_df_idx) ---")
print(salaries_df_idx)
print("-" * 40)


# --- 1. Using merge() ---

# Scenario 1.1: Joining on a common column (most typical merge use case)
# Default join is 'inner'
print("\n>>> 1.1: merge() on common column 'department_id' (default inner join)")
merged_col_inner = pd.merge(employees_df, departments_df_col, on='department_id')
print(merged_col_inner)
# Explanation: Combines employees and departments where 'department_id' matches in both.
# Employee Frank (dept 4) and Marketing (dept 5) are excluded.

# Scenario 1.2: merge() with a 'left' join on a common column
print("\n>>> 1.2: merge() on common column 'department_id' (left join)")
merged_col_left = pd.merge(employees_df, departments_df_col, on='department_id', how='left')
print(merged_col_left)
# Explanation: All employees are kept. Frank (dept 4) has NaN for department_name/location
# because department_id 4 is not in departments_df_col.

# Scenario 1.3: merge() with a 'right' join on a common column
print("\n>>> 1.3: merge() on common column 'department_id' (right join)")
merged_col_right = pd.merge(employees_df, departments_df_col, on='department_id', how='right')
print(merged_col_right)
# Explanation: All departments from departments_df_col are kept. Marketing (dept 5)
# has NaN for employee_id/name as no employee is in department 5.

# Scenario 1.4: merge() with an 'outer' join on a common column
print("\n>>> 1.4: merge() on common column 'department_id' (outer join)")
merged_col_outer = pd.merge(employees_df, departments_df_col, on='department_id', how='outer')
print(merged_col_outer)
# Explanation: All employees and all departments are kept. NaN where no match.

# Scenario 1.5: merge() joining a DataFrame's column with another DataFrame's index
print("\n>>> 1.5: merge() employees_df (column) with departments_df_idx (index)")
merged_col_to_idx = pd.merge(employees_df, departments_df_idx,
                               left_on='department_id', right_index=True, how='left')
print(merged_col_to_idx)
# Explanation: Joins employees_df's 'department_id' column with departments_df_idx's index.
# 'right_index=True' tells merge to use the right DataFrame's index as the join key.

# Scenario 1.6: merge() joining on different column names
df_temp_dept = departments_df_col.rename(columns={'department_id': 'dept_id'})
print("\n>>> 1.6: merge() on different column names ('department_id' and 'dept_id')")
merged_diff_names = pd.merge(employees_df, df_temp_dept,
                             left_on='department_id', right_on='dept_id', how='left')
print(merged_diff_names.drop(columns=['dept_id'])) # Drop redundant key column
# Explanation: merge() handles differently named key columns easily.


# --- 2. Using DataFrame.join() ---

# Scenario 2.1: Joining on index (most typical join() use case)
# For this, let's set employee_id as index for employees_df
employees_df_indexed = employees_df.set_index('employee_id')
print("\n--- Employees DataFrame with Index (employees_df_indexed) ---")
print(employees_df_indexed)
print("-" * 40)

print("\n>>> 2.1: join() employees_df_indexed with salaries_df_idx (default left join on index)")
joined_idx = employees_df_indexed.join(salaries_df_idx)
print(joined_idx)
# Explanation: Joins on the indices of both DataFrames.
# Default is 'left', so all employees from employees_df_indexed are kept.
# Eve (employee_id 105) has NaN for salary as her ID is not in salaries_df_idx's index.

# Scenario 2.2: join() with 'inner' join on index
print("\n>>> 2.2: join() employees_df_indexed with salaries_df_idx (inner join on index)")
joined_idx_inner = employees_df_indexed.join(salaries_df_idx, how='inner')
print(joined_idx_inner)
# Explanation: Only employees present in both indices are kept. Eve is excluded.

# Scenario 2.3: join() a DataFrame's column to another DataFrame's index
# Here, employees_df's 'department_id' column will be joined with departments_df_idx's index.
# We need to tell join() which column to use from the left DataFrame using 'on'.
print("\n>>> 2.3: join() employees_df's 'department_id' column with departments_df_idx's index")
joined_col_to_idx = employees_df.join(departments_df_idx, on='department_id', how='left')
print(joined_col_to_idx)
# Explanation: This is similar to merge(..., left_on='department_id', right_index=True).
# The 'on' parameter in join() refers to a column in the *calling* (left) DataFrame.

# Scenario 2.4: join() with multiple DataFrames (they must share an index or join on the calling DF's index)
# Let's create another DataFrame indexed by department_id
dept_head_data = {'head_count': [10, 25, 15, 8]}
dept_heads_df_idx = pd.DataFrame(dept_head_data, index=pd.Index([1, 2, 3, 5], name='department_id'))

print("\n>>> 2.4: join() employees_df (on 'department_id') with multiple DFs (departments_df_idx, dept_heads_df_idx)")
# For this to work cleanly, the other DFs should be indexed appropriately if joining on the left's column.
# Or, all DFs (including the calling one) are indexed and join on index.

# Example: Joining employees_df (on 'department_id') to departments_df_idx (on its index)
# and then joining the result to dept_heads_df_idx (on its index, which matches the 'department_id' values)
# This requires chaining or a more complex setup if the join keys don't align perfectly.

# A simpler multi-join: if all are indexed by the same key type
# (Not directly applicable here without re-indexing employees_df by department_id, which is not unique)

# More common multi-join: join a list of DataFrames to the calling DataFrame if their indices align
# Let's say we have employees_df_indexed and salaries_df_idx (both indexed by employee_id)
# and another_info_df_idx also indexed by employee_id
another_info_data = {'start_year': [2020, 2019, 2021, 2018, 2022]}
another_info_df_idx = pd.DataFrame(another_info_data, index=pd.Index([101, 102, 103, 104, 106], name='employee_id'))

print("\n>>> 2.4.1: join() employees_df_indexed with a list of DFs [salaries_df_idx, another_info_df_idx] on index")
joined_multiple_on_index = employees_df_indexed.join([salaries_df_idx, another_info_df_idx], how='left')
print(joined_multiple_on_index)
# Explanation: Joins multiple DataFrames to employees_df_indexed based on their common index 'employee_id'.

# --- Key Differences Summarized ---
#
# Flexibility:
#   - merge(): Highly flexible. Can join on columns (same or different names), indices, or a mix.
#              Supports all SQL-like join types explicitly (inner, left, right, outer).
#   - join(): Primarily designed for joining on indices. Can join a DataFrame's column to another's index using 'on'.
#             Less direct for column-to-column joins with different names.
#
# Default Join Type:
#   - merge(): 'inner'
#   - join(): 'left'
#
# Syntax:
#   - merge(): `pd.merge(left_df, right_df, ...)` (function)
#   - join(): `left_df.join(right_df, ...)` (DataFrame method)
#
# Use Cases:
#   - merge(): Best for database-style operations where you need to combine DataFrames based on common fields (columns).
#              When join keys have different names.
#              When you need explicit control over all join types.
#   - join(): Convenient for quick merges when the join key is the index in one or both DataFrames.
#             Useful for adding columns from one DataFrame to another based on index alignment.
#             Can be more concise for simple index-based left joins.

