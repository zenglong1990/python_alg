def quickSort(array):
    if len(array) < 2:#基线条件，为空或只包含一个元素的数组是有序的
        return array
    else:
        pivot = array[0]#递归条件
        less = [i for i in array[1:] if i <= pivot]#由所有小于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i > pivot]#由所有大于基准值的元素组成的子数组
        return quickSort(less) + [pivot] + quickSort(greater)

arr = [10,5,6,9,3,2,7,4,8,1]
last_arr = quickSort(arr)
print (last_arr)
