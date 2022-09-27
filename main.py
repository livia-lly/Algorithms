# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# 冒泡排序  O(n²)
# 1. 算法步骤
# 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
# 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
# 针对所有的元素重复以上的步骤，除了最后一个。
# 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 选择排序  O(n²)
# 1. 算法步骤
# 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
# 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
# 重复第二步，直到所有元素均排序完毕。
def selectionSort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

# 插入排序 O(n²)
# 1. 算法步骤
# 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
# 外层循环对除了第一个元素之外的所有元素，内层循环对当前元素前面有序表进行待插入位置查找，并进行移动。
# 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex-=1
        arr[preIndex+1] = current
    return arr

#希尔排序  O(n1+§)) 排序，§ 是介于 0 和 1 之间的常数。
# 希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。
# 希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序。
# 算法步骤
# 选择一个增量序列 t1，t2，……，tk，其中 ti > tj, tk = 1；
# 按增量序列个数 k，对序列进行 k 趟排序；
# 每趟排序，根据对应的增量 ti，将待排序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("")