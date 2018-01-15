
def Main():
    n = int(input())
    a = sorted(map(int, input().split()))

    if a[n-1] < a[n]:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    Main()