def merge_sort(alist):
    length = len(alist)
    if lenght>1:
        mid = length//2
        aleftlist = alist[:mid]
        arightlist = alist[mid:]
        merge_sort(aleftlist)
        merge_sort(arightlist)

        i = j = k = 0

        while i < len(aleftlist) and j < len(arightlist):
            if aleftlist[i] < arightlist[j]:
                alist[k] = aleftlist[i]
                k +=1
                i +=1
            else:
                alist[k] = arightlist[j]
                k +=1
                j +=1

        while i < len(aleftlist):
            alist[k] = aleftlist[i]
            i +=1
            k +=1

        while j < len(arightlist):
            alist[k] = arightlist[j]
            j +=1
            k +=1
