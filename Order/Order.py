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

#希尔排序 希尔排序时间复杂度是 O(n^(1.3-2))，空间复杂度为常数阶 O(1)
# 希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。
# 希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序。
# 算法步骤
# 选择一个增量序列 t1，t2，……，tk，其中 ti > tj, tk = 1；
# 按增量序列个数 k，对序列进行 k 趟排序；
# 每趟排序，根据对应的增量 ti，将待排序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
def shellSort(arr):
    import math
    gap=1
    while(gap < len(arr)/3):
        gap = gap*3+1
    while gap > 0:
        for i in range(gap,len(arr)):
            temp = arr[i]
            j = i-gap
            while j >=0 and arr[j] > temp:
                arr[j+gap]=arr[j]
                j-=gap
            arr[j+gap] = temp
        gap = math.floor(gap/3)
    return arr

#归并排序
# 算法步骤
# 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
# 设定两个指针，最初位置分别为两个已经排序序列的起始位置；
# 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
# 重复步骤 3 直到某一指针达到序列尾；
# 将另一序列剩下的所有元素直接复制到合并序列尾。
def mergeSort(arr):
    import math
    if(len(arr)<2):
        return arr
    middle = math.floor(len(arr)/2)
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0));
        else:
            result.append(right.pop(0));
    while left:
        result.append(left.pop(0));
    while right:
        result.append(right.pop(0));
    return result



# 快速排序 O( nlgn)-O(n²)
# 最优的情况下空间复杂度为：O(logn) ；每一次都平分数组的情况
# 最差的情况下空间复杂度为：O( n ) ；退化为冒泡排序的情况
# 快速排序又是一种分而治之思想在排序算法上的典型应用。本质上来看，快速排序应该算是在冒泡排序基础上的递归分治法。
# 1. 算法步骤
# 从数列中挑出一个元素，称为 “基准”（pivot）
# 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
# 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；
# 递归的最底部情形，是数列的大小是零或一，也就是永远都已经被排序好了。虽然一直递归下去，但是这个算法总会退出，因为在每次的迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。

def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left,(int, float)) else left
    right = len(arr)-1 if not isinstance(right,(int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr

def partition(arr, left, right):
    pivot = left
    index = pivot+1
    i = index
    while  i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index+=1
        i+=1
    swap(arr,pivot,index-1)
    return index-1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]






# 堆排序  堆排序是不稳定的排序，空间复杂度为O(1),平均的时间复杂度为O(nlogn),最坏情况下也稳定在O(nlogn)
# 堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：
# 即子结点的键值或索引总是小于（或者大于）它的父节点。堆排序可以说是一种利用堆的概念来排序的选择排序。分为两种方法：
# 大顶堆：每个节点的值都大于或等于其子节点的值，在堆排序算法中用于升序排列；
# 小顶堆：每个节点的值都小于或等于其子节点的值，在堆排序算法中用于降序排列；
# 算法步骤
# 将待排序序列构建成一个堆 H[0……n-1]，根据（升序降序需求）选择大顶堆或小顶堆；
# 把堆首（最大值）和堆尾互换；
# 把堆的尺寸缩小 1，并调用 shift_down(0)，目的是把新的数组顶端数据调整到相应位置；
# 重复步骤 2，直到堆的尺寸为 1。
def buildMaxHeap(arr):
    import math
    for i in range(math.floor(len(arr)/2),-1,-1):
        heapify(arr,i)

def heapify(arr, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)
        arrLen -=1
        heapify(arr, 0)
    return arr

# 计数排序
# 计数排序(Count Sort)是一个非基于比较的排序算法
# 它的优势在于在对一定范围内的整数排序时，它的复杂度为Ο(n+k)（长度加元素数），快于任何比较排序算法。空间复杂度O(k)
#1.当数列最大最小值差距过大时，并不适用于计数排序2.当数列元素不是整数时，并不适用于计数排序
# 计数排序的思想是在给定的一组序列中，先找出该序列中的最大值和最小值，从而确定需要开辟多大的辅助空间，每一个数在对应的辅助空间中都有唯一的下标。
# 找出序列中最大值和最小值，开辟Max-Min+1的辅助空间
# 最小的数对应下标为0的位置，遇到一个数就给对应下标处的值+1,。
# 遍历一遍辅助空间，就可以得到有序的一组序列
def countingSort(arr, maxValue):
    bucketLen = maxValue+1
    bucket = [0]*bucketLen
    sortedIndex =0
    arrLen = len(arr)
    for i in range(arrLen):
        if not bucket[arr[i]]:
            bucket[arr[i]]=0
        bucket[arr[i]]+=1
    for j in range(bucketLen):
        while bucket[j]>0:
            arr[sortedIndex] = j
            sortedIndex+=1
            bucket[j]-=1
    return arr

# 桶排序是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。为了使桶排序更加高效，我们需要做到这两点：
# 在额外空间充足的情况下，尽量增大桶的数量
# 使用的映射函数能够将输入的 N 个数据均匀的分配到 K 个桶中
# 同时，对于桶中元素的排序，选择何种比较排序算法对于性能的影响至关重要。
#当输入的数据可以均匀的分配到每一个桶中最快，当输入的数据被分配到了同一个桶中最慢
def bucket_sort(array):
    min_num, max_num = min(array), max(array)
    bucket_num = (max_num-min_num)//3 + 1
    buckets = [[] for _ in range(int(bucket_num))]
    for num in array:
        buckets[int((num-min_num)//3)].append(num)
    new_array = list()
    for i in buckets:
        for j in sorted(i):
            new_array.append(j)
    return new_array

# 基数排序
# 基数排序是一种非比较型整数排序算法，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。
# 由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。
# 1. 基数排序 vs 计数排序 vs 桶排序
# 基数排序有两种方法：
# 这三种排序算法都利用了桶的概念，但对桶的使用方法上有明显差异案例看大家发的：
# 基数排序：根据键值的每位数字来分配桶；
# 计数排序：每个桶只存储单一键值；
# 桶排序：每个桶存储一定范围的数值；
def radix(arr):
    digit = 0
    max_digit = 1
    max_value = max(arr)
    # 找出列表中最大的位数
    while 10 ** max_digit < max_value:
        max_digit = max_digit + 1

    while digit < max_digit:
        temp = [[] for i in range(10)]
        for i in arr:
            # 求出每一个元素的个、十、百位的值
            t = int((i / 10 ** digit) % 10)
            temp[t].append(i)

        coll = []
        for bucket in temp:
            for i in bucket:
                coll.append(i)

        arr = coll
        digit = digit + 1

    return arr



if __name__ == '__main__':
    print("")