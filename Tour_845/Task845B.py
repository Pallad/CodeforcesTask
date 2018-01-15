def Main():
    dig = 0
    n = input()
    n1 = list(map(int, list(n[:3])))
    n2 = list(map(int, list(n[3:])))
    n1 = sorted(n1)
    n2 = sorted(n2)
    delta = sum(n1) - sum(n2)

    if delta != 0:
        if delta < 0:
            n1, n2, delta = n2, n1, abs(delta)

        ind1 = 2
        ind2 = 0

        while ind1 > -1 and ind2 < 3 and delta > 0:
            if n1[ind1] >= 9 - n2[ind2]:
                delta = delta - n1[ind1]
                ind1 = ind1 - 1
                dig = dig + 1
            else:
                delta = delta - (9 - n2[ind2])
                ind2 = ind2 + 1
                dig = dig + 1

    print(dig)

if __name__ == '__main__':
    Main()