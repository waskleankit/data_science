# # import pandas as pd
# #
# # data = {
# #     "calories": [420, 380, 390],
# #     "duration": [50, 40, 45]
# # }
# #
# # #load data into a DataFrame object:
# # df = pd.DataFrame(data)
# #
# # print(df)
# #
# # #refer to the row index:
# # print(df.loc[0])
# #
# # #use a list of indexes:
# # print(df.loc[[0, 1]])
#
# import pandas as pd
#
# data = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45]
# }
#
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
#
# print(df)
#
# #refer to the named index:
# print(df.loc["day2"])

import pandas as pd

df = pd.read_csv('..\\csv\\data.csv')

print(df)