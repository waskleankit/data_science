# # # # # # # # # # # # # # # import numpy
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # arr = numpy.array([1, 2, 3, 4, 5])
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # print(arr)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # import numpy as np
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # arr = np.array([1, 2, 3, 4, 5])
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(arr)
# # # # # # # # # # # # # import numpy as np
# # # # # # # # # # # # #
# # # # # # # # # # # # # print(np.__version__)
# # # # # # # # # # # # import numpy as np
# # # # # # # # # # # #
# # # # # # # # # # # # arr = np.array([1, 2, 3, 4, 5])
# # # # # # # # # # # #
# # # # # # # # # # # # print(arr)
# # # # # # # # # # # #
# # # # # # # # # # # # print(type(arr))
# # # # # # # # # # # import numpy as np
# # # # # # # # # # #
# # # # # # # # # # # arr = np.array((1, 2, 3, 4, 5))
# # # # # # # # # # #
# # # # # # # # # # # print(arr)
# # # # # # # # # #
# # # # # # # # # # import numpy as np
# # # # # # # # # #
# # # # # # # # # # arr = np.array(42)
# # # # # # # # # #
# # # # # # # # # # print(arr)
# # # # # # # # #
# # # # # # # # # import numpy as np
# # # # # # # # #
# # # # # # # # # arr = np.array([1, 2, 3, 4, 5])
# # # # # # # # #
# # # # # # # # # print(arr)
# # # # # # # #
# # # # # # # # import numpy as np
# # # # # # # #
# # # # # # # # arr = np.array([[1, 2, 3], [4, 5, 6]])
# # # # # # # #
# # # # # # # # print(arr)
# # # # # # # import numpy as np
# # # # # # #
# # # # # # # arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# # # # # # #
# # # # # # # print(arr)
# # # # # #
# # # # # #
# # # # # # import numpy as np
# # # # # #
# # # # # # a = np.array(42)
# # # # # # b = np.array([1, 2, 3, 4, 5])
# # # # # # c = np.array([[1, 2, 3], [4, 5, 6]])
# # # # # # d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# # # # # #
# # # # # # print(a.ndim)
# # # # # # print(b.ndim)
# # # # # # print(c.ndim)
# # # # # # print(d.ndim)
# # # # #
# # # # # import numpy as np
# # # # #
# # # # # arr = np.array([1, 2, 3, 4], ndmin=5)
# # # # #
# # # # # print(arr)
# # # # # print('number of dimensions :', arr.ndim)
# # # #
# # # # import numpy as np
# # # #
# # # # arr = np.array([1, 2, 3, 4])
# # # #
# # # # print(arr[0])
# # # # print(arr[1])
# # # # print(arr[2] + arr[3])
# # # #
# # # # import numpy as np
# # # #
# # # # arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# # # #
# # # # print('2nd element on 1st row: ', arr[0, 1])
# # # #
# # # #
# # # # import numpy as np
# # # #
# # # # arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# # # #
# # # # print('5th element on 2nd row: ', arr[1, 4])
# # # #
# # # #
# # # # import numpy as np
# # # #
# # # # arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# # # #
# # # # print(arr[0, 1, 2])
# # #
# # #
# # # import numpy as np
# # #
# # # arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# # #
# # # print('Last element from 2nd dim: ', arr[1, -1])
# # #
# # # import numpy as np
# # #
# # # arr = np.array([1, 2, 3, 4, 5, 6, 7])
# # #
# # # print(arr[1:5])
# # #
# # #
# # #
# # # import numpy as np
# # #
# # # arr = np.array([1, 2, 3, 4, 5, 6, 7])
# # #
# # # print(arr[4:])
# # #
# # #
# # # import numpy as np
# # #
# # # arr = np.array([1, 2, 3, 4, 5, 6, 7])
# # #
# # # print(arr[:4])
# # #
# # #
# # # import numpy as np
# # #
# # # arr = np.array([1, 2, 3, 4, 5, 6, 7])
# # #
# # # print(arr[-3:-1])
# # #
# # #
# # # import numpy as np
# # #
# # # arr = np.array([1, 2, 3, 4, 5, 6, 7])
# # #
# # # print(arr[1:5:2])
# # #
# # # import numpy as np
# # #
# # # arr = np.array([1, 2, 3, 4, 5, 6, 7])
# # #
# # # print(arr[::2])
# #
# #
# # import numpy as np
# #
# # arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# #
# # print(arr[1, 1:4])
#
#
# import numpy as np
#
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#
# print(arr[0:2, 2])
#
#
# import numpy as np
#
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#
# print(arr[0:2, 1:4])