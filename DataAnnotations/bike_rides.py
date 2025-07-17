import pandas as pd

# A
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# A. Read the CSV file into a DataFrame
df_a = pd.read_csv('DataAnnotations/6XWX_bike_rides.csv')
# B. Load the CSV file to check its contents
file_name = 'DataAnnotations/6XWX_bike_rides.csv'
df_b = pd.read_csv(file_name)

# A. Display the first 5 rows
print(df_a.head().to_markdown(index=False, numalign="left", stralign="left"))
# A. Print the column names and their data types
print(df_a.info())
# B. Display the first few rows of the dataframe and the column names
df_b.head(), df_b.columns

# A. Convert `date` to datetime
df_a['date'] = pd.to_datetime(df_a['date'])
print(df_a['date'])
# B. Convert `date` to datetime
df_b["date"] = pd.to_datetime(df_b["date"], format="%d/%m/%Y", errors="coerce")
# df_b['date'] = pd.to_datetime(df_a['date'])
print(df_b['date'])


# A. Filter data by year 2022
df_2022_a = df_a[df_a['date'].dt.year == 2022]
# B. Filter data by year 2022
df_2022_b = df_b[df_b["date"].dt.year == 2022]

# A. Compute and print average `group_size` in 2022
avg_group_size_2022 = df_2022_a['group_size'].mean()
print(f"A. The average group size for rides in 2022 was: {avg_group_size_2022:.2f}")
# B. Compute and print average `group_size` in 2022
avg_group_size_2022 = df_2022_b["group_size"].mean()
print(f"B. {avg_group_size_2022:.2f}")
