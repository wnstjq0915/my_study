"""
numpy method, 예제 모음
"""

"""
1. ndarray.ndim: 배열의 차원 수를 반환합니다.
예를 들어, 2차원 배열은 행(row)과 열(column)
두 개의 차원이 있으므로 ndim 값은 2입니다.
"""
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6]])
print(arr.ndim) # 2


"""
2. ndarray.size: 배열의 총 요소 수를 반환합니다.
이 값은 배열의 각 차원에 저장된 요소 수를 곱한 값과 같습니다. 
"""
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6]])
print(arr.size) # 6

"""
3. ndarray.shape: 배열의 차원 크기를 반환합니다.
예를 들어, (2, 3) 배열은 2행 3열의 배열이므로
shape 값은 (2, 3)입니다. 
"""
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6]])
print(arr.shape) # (3, 2)

"""
4. np.zeros: 모든 요소가 0인 배열을 생성합니다.
이 함수는 주로 초기화 용도로 사용됩니다.
"""
import numpy as np

arr = np.zeros((2, 3))
print(arr)

"""
5. np.ones: 모든 요소가 1인 배열을 생성합니다.
이 함수도 주로 초기화 용도로 사용됩니다. 
"""
import numpy as np

arr = np.ones((2, 3))
print(arr)

"""
6. np.arange: 지정된 범위 내의
일정한 간격으로 배열을 생성합니다. 
"""
import numpy as np

arr = np.arange(10, 20, 2)
print(arr)

"""
7. np.linspace: 지정된 범위 내에서 균등한 간격으로 배열을 생성합니다.
"""
import numpy as np

arr = np.linspace(0, 1, 5)
print(arr)


"""
8. numpy.clip(a, a_min, a_max, out=None) : 배열 내의 값을 지정한 범위
내에서만 사용하고,범위 밖 값은
지정한 최솟값 또는 최댓값으로 대체합니다.
"""

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
clipped_arr = np.clip(arr, 2, 4)
print(clipped_arr)


"""
9. numpy.concatenate((a1, a2, ...), axis=0, out=None) : 배열을 연결(concatenate)하여
새로운 배열을 만듭니다.
"""
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated_arr = np.concatenate((arr1, arr2))
print(concatenated_arr)

"""
10. numpy.sort(a, axis=-1, kind=None, order=None) : 배열을 정렬합니다.
(kind는 선택적 파라미터로,quicksort, mergesort, heapsort 중 하나를 선택할 수 있습니다.)
"""
import numpy as np
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5])
sorted_arr = np.sort(arr)
print(sorted_arr)

"""
11. numpy.random.rand(): 0부터 1 사이의 균일 분포에서
무작위로 추출된 값을 가지는 ndarray 배열 생성
"""
import numpy as np

# 2x2 무작위 ndarray 배열 생성
arr = np.random.rand(2, 2)
print(arr)

"""
12. numpy.eye(): 단위 행렬 생성
"""
import numpy as np

# 3x3 단위 행렬 생성
arr = np.eye(3)
print(arr)

"""
13. numpy.concatenate(): 두 개 이상의 배열을
연결하여 하나의 배열로 만듦
"""
import numpy as np

# 1x3 크기의 ndarray 배열 생성
arr1 = np.array([1, 2, 3])

# 1x4 크기의 ndarray 배열 생성
arr2 = np.array([4, 5, 6, 7])

# 두 배열을 연결하여 1x7 크기의 ndarray 배열 생성
arr3 = np.concatenate((arr1, arr2))
print(arr3)

"""
14. numpy.reshape(): 배열의 차원을 재구성
"""
import numpy as np

# 1차원 ndarray 배열 생성
arr1 = np.array([1, 2, 3, 4, 5, 6])

# 2x3 크기의 ndarray 배열로 재구성
arr2 = arr1.reshape(2, 3)
print(arr2)

"""
15. numpy.transpose(): 행과 열을 바꾼 ndarray 배열 생성
"""
import numpy as np

# 2x3 크기의 ndarray 배열 생성
arr1 = np.array([[1, 2, 3], [4, 5, 6]])

# 3x2 크기의 ndarray 배열로 재구성
arr2 = np.transpose(arr1)
print(arr2)
