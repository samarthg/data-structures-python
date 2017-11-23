
def quick_sort(input_list, start, end):
    if start< end:
        pivot = partition(input_list, start, end)
        quick_sort(input_list, start, pivot-1)
        quick_sort(input_list, pivot+1, end)
    return input_list

def partition(input_list, start, end):
    pivot = input_list[start]
    left = start + 1
    right = end
    done = False
    
    while not done:
        while  left <= right and input_list[left]<= pivot:
            left = left + 1
        while input_list[right] >= pivot and right>= left:
            right = right - 1
        if right < left:
            done = True
        else:
            temp = input_list[left]
            input_list[left] = input_list[right]
            input_list[right] = temp

    temp = input_list[start]
    input_list[start] = input_list[right]
    input_list[right] = temp
    return right
