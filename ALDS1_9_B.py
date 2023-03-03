def heap_left(i: int):
    return int(2*i)

def heap_right(i: int):
    return int(2*i + 1)

def max_heapify(a: list, i: int):
    l = heap_left(i)
    r = heap_right(i)
    if l <= h and a[i] < a[l]:
        largest = l
    else:
        largest = i
    if r <= h and a[largest] < a[r]:
        largest = r

    if largest == i:
        return

    tmp = a[i]
    a[i] = a[largest]
    a[largest] = tmp
    max_heapify(a, largest)

def build_max_heap(a: list):
    for i in reversed(range(1,int(h/2)+1)):
            max_heapify(a, i)

h = int(input())
a = [None] + [int(x) for x in input().split()]

build_max_heap(a)
print(' ', end='')
print(*a[1:])
