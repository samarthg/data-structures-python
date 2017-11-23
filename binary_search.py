
def binary_search(input_list, item_to_be_found):
    found = False
    bottom = 0
    top = len(input_list) -1
    while bottom <= top and not found:
        middle = (bottom + top)//2
        if input_list[middle]==item_to_be_found:
            found = True
            break
        elif input_list[middle] > item_to_be_found:
            top = middle - 1
        elif input_list[middle] < item_to_be_found:
            bottom = middle + 1
    return found


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8 ,9]  
