import random


def bubble_sort(li):
    for i in range(len(li) - 1):  # 第i趟
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
        if not exchange:
            return
        # print(li)


# li = [random.randint(0, 10000) for i in range(1000)]
li = [3, 5, 6, 8, 2, 1, 9, 10]
print(li)
bubble_sort(li)
print(li)
