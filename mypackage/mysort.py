##冒泡排序
"""
比较相邻的元素。如果第一个比第二个大，就交换他们两个。

对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。

针对所有的元素重复以上的步骤，除了最后一个。

持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
"""
def bubbleSort(arr,key=True):
    '''
    arr：数组类数组,key：True 升序 ;False 降序
    返回排序好的数组
    '''
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    if key==True:      #升序
        return arr  
    else:              #降序
        return arr[::-1]
##选择排序
"""
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。

再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。

重复第二步，直到所有元素均排序完毕。
"""
def selectionSort(arr,key=True):
    '''
    arr：数组类数组,key：True 升序 ;False 降序
    返回排序好的数组
    '''
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    if key==True:      #升序
        return arr  
    else:              #降序
        return arr[::-1]
#插入排序
"""
将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。

从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
"""
def insertionSort(arr,key=True):
    '''
    arr：数组,类数组,key：True 升序 ;False 降序
    返回排序好的数组
    '''
    for i in range(len(arr)):  
        preIndex = i-1      #前一位元素的索引
        current = arr[i]    # 有序序列末尾元素，现位元素
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]  #如果现位元素小于前一位，将现位元素换成前一位
            preIndex-=1
        arr[preIndex+1] = current
    if key==True:      #升序
        return arr  
    else:              #降序
        return arr[::-1]
#堆排序
"""
创建一个堆 H[0……n-1]；

把堆首（最大值）和堆尾互换；

把堆的尺寸缩小 1，并调用 shift_down(0)，目的是把新的数组顶端数据调整到相应位置；

重复步骤 2，直到堆的尺寸为 1。
"""
def buildMaxHeap(arr):##建立大根堆
    import math
    for i in range(math.floor(len(arr)/2),-1,-1):
        heapify(arr,i)

def heapify(arr, i):#下滤
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

def heapSort(arr,key=True):
    '''
    arr：数组类数组,key：True 升序 ;False 降序
    返回排序好的数组
    '''
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)
        arrLen -=1
        heapify(arr, 0)
    if key==True:      #升序
        return arr  
    else:              #降序
        return arr[::-1]
##归并排序
"""
申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；

设定两个指针，最初位置分别为两个已经排序序列的起始位置；

比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；

重复步骤 3 直到某一指针达到序列尾；

将另一序列剩下的所有元素直接复制到合并序列尾。
"""
def mergeSort(arr,key=True):#原数组未变，返回副本。
    '''
    arr：数组类数组,key：True 升序 ;False 降序
    返回排序好的数组
    '''
    import math
    if(len(arr)<2):
        return arr
    middle = math.floor(len(arr)/2)#从上到下的递归
    left, right = arr[0:middle], arr[middle:]
    if key==True:      #升序
        return merge(mergeSort(left), mergeSort(right))  
    else:              #降序
        return merge(mergeSort(left), mergeSort(right))[::-1]
    
###归并操作
def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result
#快速排序
'''
从数列中挑出一个元素，称为 "基准"（pivot）;

重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；

递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；
一般都把区的第一个数当作基准
'''
    
def quickSort(arr,right=None,left=None,key=True):
    left = 0 if not isinstance(left,(int, float)) else left
    right = len(arr)-1 if not isinstance(right,(int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right) # 分区并得到基准（分区“中间”）位置
        quickSort(arr, left, partitionIndex-1)  #对小于基准的序列继续分区
        quickSort(arr, partitionIndex+1, right) #对大于基准的序列继续分区
    if key==True:      #升序
        return arr  
    else:              #降序
        return arr[::-1] 

def partition(arr, left, right):
    pivot = left      #原基准的索引
    index = pivot+1   #基准右边靠小序列末位元素的索引（不在小序列内）
    i = index         #基准外依次向后的索引
    while  i <= right: #遍历分出小和大两边
        if arr[i] < arr[pivot]: #小于基准的依次放在基准右边，叫小序列
            swap(arr, i, index) 
            index+=1
        i+=1
    swap(arr,pivot,index-1) #是基准与小序列末位元素交换，完成分区
    return index-1 #返回分区后基准索引。
#希尔排序
'''
选择一个增量序列 t1，t2，……，tk，其中 ti > tj, tk = 1；增量是对原序列而言

按增量序列个数 k，对序列进行 k 趟排序；

每趟排序，根据对应的增量 ti，将待排序列分割成若干长度为 m 的子序列，m=n/ti分别对各子表进行直接插入排序。
仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。每个子序列由间隔为m的元素组成。
'''
def shellSort(arr,key=True):
    import math
    gap=1
    while(gap < len(arr)/3): #设置初始增量约为原序列长度三分之一
        gap = gap*3+1     #式一
    while gap > 0:
        for i in range(gap,len(arr)): #并非一次对一组进行完全插入排序而是，一组每次一个。
            temp = arr[i]  #组中的有序序列的末尾元素，需插入元素
            j = i-gap   #中的有序序列的元素
            while j >=0 and arr[j] > temp: #当需插入元素大于三分后元素，交换其位置
                arr[j+gap]=arr[j]
                j-=gap
            arr[j+gap] = temp
        gap = math.floor(gap/3) #结合式一，保证增量减小直至1
    if key==True:      #升序
        return arr  
    else:              #降序
        return arr[::-1]

