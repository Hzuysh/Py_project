def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:  # 侯选区有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:  # 待查找的值在mid左边
            right = mid - 1
        else:  # li[mid] < val
            left = mid + 1
    else:
        return None


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
find = binary_search(li, 3)
print(find)
