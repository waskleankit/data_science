# # import pandas as pd
# #
# # df = pd.read_json('data.json')
# #
# # print(df.to_string())
# import pandas as pd
#
# df = pd.read_csv('data.csv')
#
# print(df.head(10))
import pandas as pd

df = pd.read_csv('data.csv')

print(df.head())
print(df.tail())

print(df.info()) 