import sys
import math

def merge_sort(a, left, right):
    mid = (left+right)//2
    if mid < left+1: return 0

    cnt_inv  = merge_sort(a, left, mid)
    cnt_inv += merge_sort(a, mid, right)

    num_left = mid - left
    l = a[left:mid] + [math.inf]
    r = a[mid:right] + [math.inf]
    i, j = 0, 0
    for k in range(left,right):
        if l[i] < r[j]:
            a[k] = l[i]
            i += 1
            num_left -= 1
            continue
        a[k] = r[j]
        j += 1
        cnt_inv += num_left
    return cnt_inv

n = int(sys.stdin.readline())
a = [int(w) for w in sys.stdin.readline().split()]

print(merge_sort(a,0,n))
