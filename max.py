def max(num_list):
    max_num = num_list[0]
    for num in num_list:
        if num > max_num:
            max_num = num
    return max_num
    """
    주어진 배열에서 제일 큰 숫자를 반환하는 함수를 작성하시오.
    단 배열은 항상 최소 1개의 원소를 가지며, 
    모든 원소는 0 이상의 정수라고 가정하라.
    """
    return -1


print(max([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max([9, 4, 7, 5, 6, 2, 1, 0, 3, 8]))
print(max([2, 6, 8, 4, 9, 9, 8, 8, 8, 7]))
print(max([1]))

""" 수행예:
9
9
9
1
"""
