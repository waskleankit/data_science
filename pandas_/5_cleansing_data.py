# # # # # # #import pandas as pd
# # # # # # #df = pd.read_csv('..//csv//Book1.csv')
# # # # # # #new_df = df.dropna()
# # # # # # #print(new_df.to_string())
# # # # # # #
# # # # # # # import pandas as pd
# # # # # # #
# # # # # # # df = pd.read_csv('data.csv')
# # # # # # #
# # # # # # # df.dropna(inplace = True)
# # # # # # #
# # # # # # # print(df.to_string())
# # # # # #
# # # # # # import pandas as pd
# # # # # #
# # # # # # df = pd.read_csv('data.csv')
# # # # # #
# # # # # # df.fillna(130, inplace = True)
# # # # # # print(df.to_string())
# # # # # import pandas as pd
# # # # #
# # # # # df = pd.read_csv('data.csv')
# # # # #
# # # # # df["Calories"].fillna(130, inplace = True)
# # # # #
# # # # # print(df.to_string())
# # # # import pandas as pd
# # # #
# # # # df = pd.read_csv('data.csv')
# # # #
# # # # x = df["Calories"].mean()
# # # #
# # # # df["Calories"].fillna(x, inplace = True)
# # #
# # import pandas as pd
# #
# # df = pd.read_csv('data.csv')
# #
# # x = df["Calories"].median()
# #
# # df["Calories"].fillna(x, inplace = True)
# #
# # print(df.to_string())
# #
# # import pandas as pd
# #
# # df = pd.read_csv('data.csv')
# #
# # x = df["Calories"].mode()[0]
# #
# # df["Calories"].fillna(x, inplace = True)
#
#
import pandas as pd

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])
df.dropna(subset=['Date'], inplace = True)
print(df.to_string())

df.loc[7, 'Duration'] = 45