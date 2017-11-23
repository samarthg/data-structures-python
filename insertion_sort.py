
def insertion_sort(input_list):
    list_lenght = len(input_list)
    for i in range(1, list_lenght-1):
        hole = i
        value = input_list[hole]
        while hole > 0:
            if value < input_list[hole-1]:
                input_list[hole] = input_list[hole-1]
                input_list[hole-1] = value
            else:
                break
            hole -= 1
    print input_list

if __name__=='__main__':
    l = [5, 3, 4, 2, 1, 20, 14, 25]
    insertion_sort(l)
