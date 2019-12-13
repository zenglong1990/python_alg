
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    #" / "就表示 浮点数除法，返回浮点结果;" // "表示整数除法。
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__== '__main__':
    my_list = [1,3,5,7,9]
    val = binary_search(my_list,3)
    print (val)
    val = binary_search(my_list,-1)
    print (val)