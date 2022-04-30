# original code: https://qiita.com/nakasan/items/f32a63bd48494b1c822f
N = int(input())
A = [int(input()) for _ in range(N) ]

def insertion_sort(A, N, step):
    count = 0
    for i in range(step,N):
        v = A[i]
        j = i - step
        while j >= 0 and A[j]>v:
            A[j+step] = A[j]
            j -= step
            count += 1
        A[j+step] = v
    return count

m = int.bit_length(N)
print(m)
G = [N//(2**i) for i in range(m) ]
print(*G)
print(sum(insertion_sort(A, N, G[i]) for i in range(m)))
print(*A, sep="\n")
