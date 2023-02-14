def printJobSequencing(arr, t):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if (arr[j][2] < arr[j + 1][2]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    result = [False] * t
    job = ['-1'] * t
    for i in range(len(arr)):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if (result[j] is False):
                result[j] = True
                job[j] = arr[i][0]
                break
    print(job)


arr = [['j1', 5, 200],
       ['j2', 3, 180],
       ['j3', 3, 190],
       ['j4', 2, 300],
       ['j5', 4, 120],
       ['j6', 2, 100]]

print("Following is the maximum profit sequence of jobs")
printJobSequencing(arr, 5)