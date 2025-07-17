from pandas import DataFrame
data = {
    "A": [5, 6, 8, 9, 7],
    "B": ["Flamingo", "Zebra", "Cart", "Bucket", "Samantha"],
    "C": ["Some", "Alex", "Apple", 5, "Art"]
}

df = DataFrame(data)

'''Which of the following lines of code sets max_value to the maximum value from column "A" of the
    DataFrame df above for rows where the string length in column "B" is more than 4 characters
    and the string in column "C" starts with "A"?
'''
# Prints 7 which should be the correct answer
max_value = df[df["B"].str.len() > 4 & df["C"].str.startswith("A")]["A"].max()
print(max_value)
# Prints 'Zebra' which is not from 'A'
max_value = df[(df["B"].str.len() > 4) & (df["C"].str.startswith("A"))].max()
print(max_value)
# Prints 'Art' which is not from 'A'
max_value = df[(df["B"].str.len() > 4) & (df["C"].str.startswith("A"))]["A"].max()
print(max_value)
# D - This line fails to run because it does not convert df["B"] to a str before using len()
# max_value = df[(df["B"].len() > 4) & (df["C"].startswith("A"))]["A"].max()
# print(max_value)

'''Suppose we've already initialized a pandas DataFrame called df that contains the columns
    "Team", "Player" and "Score". The "Score" column holds only numeric values—the scores that
    each player has achieved in a game. Each value in the "Player" column is unique.
'''

data = {
    "Team": ['Packers', 'Giants', 'Texans', 'Ravens', 'Raiders'],
    "Player": ['J. Love', 'J. Winston', 'C.J. Stroud', 'L. Jackson', 'M. Crosby'],
    "Score": [86, 77, 82, 94, 99]
}
df = DataFrame(data)
result = df.groupby("Team")["Score"].apply(lambda x: (x > 85).sum())
print(result)


data = {
    "Receipt ID": ["124DC", "4442A", "222BZ", None, "5421T"],
    "Waiter/Waitress Name": ["Todd", None, "Lenny", "Jennifer", "Yazmin"],
    "Tip Amount": [12, 4, 3, 44, 29]
}
df = DataFrame(data)
'''Given the DataFrame df above, which of the following lines of code would modify df by
    filling in instances of None in the "Receipt ID" column with "Unknown" without modifying
    any other columns? The original DataFrame should be modified, rather than creating a new
    DataFrame without modifying the original one.
'''
# this one will fill in all 'None' with 'Unknown'
# df.fillna("Unknown", inplace=True)
# print(df)
# This is the winner
df["Receipt ID"] = df["Receipt ID"].fillna("Unknown")
print(df)
# This one doesn't work
# df.fillna({"Receipt ID": "Unknown"})
# print(df)
# Invalid syntax
# df = df.fillna("Receipt ID": "Unknown")
