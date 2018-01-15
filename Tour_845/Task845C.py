def Main():
    timesheet = {}
    n = int(input())
    while n > 0:
        p = list(map(int, input().split()))
        if timesheet.get(p[0], -1) == -1:
            timesheet[p[0]] = [p[1]]
        else:
            timesheet[p[0]].append(p[1])
        n -= 1

    times = sorted(list(timesheet.keys()))

    t1, t2, res = 0, 0, "YES"

    for t in times:
        timeline = timesheet.get(t)
        for tl in timeline:
            if t1 < t or t1 == 0:
                t1 = tl
            else:
                if t2 < t or t2 == 0:
                    t2 = tl
                else:
                    res = "NO"
                    break

        if res == "NO":
            break

    print(res)

if __name__ == '__main__':
    Main()

