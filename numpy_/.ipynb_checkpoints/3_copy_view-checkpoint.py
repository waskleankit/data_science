# # # # # # # # # import numpy as np
# # # # # # # # #
# # # # # # # # # arr = np.array([1, 2, 3, 4, 5])
# # # # # # # # # x = arr.copy()
# # # # # # # # # arr[0] = 42
# # # # # # # # #
# # # # # # # # # print(arr)
# # # # # # # # # print(x)
# # # # # # # # import numpy as np
# # # # # # # #
# # # # # # # # arr = np.array([1, 2, 3, 4, 5])
# # # # # # # # x = arr.view()
# # # # # # # # arr[0] = 42
# # # # # # # #
# # # # # # # # print(arr)
# # # # # # # # print(x)
# # # # # # #
# # # # # # # import numpy as np
# # # # # # #
# # # # # # # arr = np.array([1, 2, 3, 4, 5])
# # # # # # # x = arr.view()
# # # # # # # x[0] = 31
# # # # # # #
# # # # # # # print(arr)
# # # # # # # print(x)
# # # # # # import numpy as np
# # # # # #
# # # # # # arr = np.array([1, 2, 3, 4, 5])
# # # # # #
# # # # # # x = arr.copy()
# # # # # # y = arr.view()
# # # # # #
# # # # # # print(x.base)
# # # # # # print(y.base)
# # # # # import numpy as np
# # # # #
# # # # # arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# # # # #
# # # # # print(arr.shape)
# # # # #
# # # # # import numpy as np
# # # # #
# # # # # arr = np.array([1, 2, 3, 4], ndmin=5)
# # # # #
# # # # # print(arr)
# # # # # print('shape of array :', arr.shape)
# # # #
# # # # import numpy as np
# # # #
# # # # arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# # # #
# # # # newarr = arr.reshape(4, 3)
# # # #
# # # # print(newarr)
# # # import numpy as np
# # #
# # # arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# # #
# # # newarr = arr.reshape(2, 3, 2)
# # #
# # # print(newarr)
# #
# # import numpy as np
# #
# # arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# #
# # print(arr.reshape(2, 4).base)
#
# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
#
# newarr = arr.reshape(2, 2, -1)
#
# print(newarr)

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)