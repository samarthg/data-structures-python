def linear_search(input_list, item_to_search):
    position = 0
    is_found = False
    while position < len(input_list) and not is_found:
        if input_list[position] == item_to_search:
            is_found = True
            break
        position += 1
        
    return is_found

if __name__=='__main__':
    l = [1, 2, 3, 4, 5, 6]
    isfound = linear_search(l, 5)
    print (isfound)
    
