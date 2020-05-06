'''
    冒泡排序
1. 算法步骤

比较相邻的元素。如果第一个比第二个大，就交换他们两个。

对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。

针对所有的元素重复以上的步骤，除了最后一个。

持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

'''

import  time

def buublesort(arr):
    starttime = time.process_time()
    for i in range(1, len(arr)):
        for j in range(len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    endtime = time.process_time()
    return arr, endtime-starttime

if __name__ == '__main__':
    arr = [100,99,8,7,5,2,6,9,5,5,56,9,9,5,55,5,2,2,2,2,2,2,55,5,5,5,5,5,55,5,5,54,5,64,464,6545,454,545,4,5,65,464,646,46,464,64,6,685]*100

    result,time1 = buublesort(arr)

    print(result,'\n', time1)
