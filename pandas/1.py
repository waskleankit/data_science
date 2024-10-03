# # # import pandas
# # #
# # # mydataset = {
# # #     'cars': ["BMW", "Volvo", "Ford"],
# # #     'passings': [3, 7, 2]
# # # }
# # #
# # # myvar = pandas.DataFrame(mydataset)
# # #
# # # print(myvar)
# # import pandas as pd
# #
# # mydataset = {
# #     'cars': ["BMW", "Volvo", "Ford"],
# #     'passings': [3, 7, 2]
# # }
# #
# # myvar = pd.DataFrame(mydataset)
# #
# # print(myvar)
# #
# # print(pd.__version__)
# import pandas as pd
#
# a = [1, 7, 2]
#
# myvar = pd.Series(a)
#
# print(myvar)
#
# print(myvar[0])
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)