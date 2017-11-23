


def bubble_sort(inputList):
    length = len(inputList) - 1
    for i in range (0, length):
        for j in range(0, length - i):
            if inputList[j] > inputList[j+1]:
                temp = inputList[j]
                inputList[j] = inputList[j+1]
                inputList[j+1] = temp
    print inputList

if __name__ == '__main__':
    l = [5, 4, 2, 3, 1]
    bubble_sort(l)
