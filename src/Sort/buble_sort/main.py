

def bubble_sort(arr):
    """ Cортировка пузырьком """
    l = len(arr)-1
    for i in range(l):
        for j in range(l-i):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp

    for i in arr:
        print(i, end=' ')



if __name__ == '__main__':
    bubble_sort([3, 2, 1, -1, -2, -3])

