# todo this code not pass every case right now
# jobList = ["j1","j2","j3","j4"]
# Profit = [50,15,10,25]
# Dedline = [2,1,2,1]

jobList = ["j1","j2","j3","j4","j5","j6","j7"]
Profit = [35,30,25,20,15,12,5]
Dedline = [3,4,4,2,3,1,2]


def setInDic(jobList):
    JPD = {}
    # todo 0 = profile 1 = Dedline
    for i in range(len(jobList)):
        JPD[jobList[i]] = Profit[i], Dedline[i]

    return JPD

# todo sort profit,deadline and jobList acsending order
def sortProft():
    JPD = setInDic(jobList)
    JobP = []
    for key, values in JPD.items():
        JobP.append(JPD[key][0])
    JobP.sort()
    return JobP

def FinalDicForJob():
    JPD = setInDic(jobList)
    JobP = sortProft()
    FinalDic_Job = {}
    for i in range(len(JobP) - 1, -1, -1):
        for key, values in JPD.items():
            if JobP[i] == JPD[key][0]:
                FinalDic_Job[key] = values
    return FinalDic_Job

# todo create a max list for dedline
def MaxDedline(Max):
    MaxDeadline = []
    for i in range(Max):
        MaxDeadline.append(None)

    return MaxDeadline



# todo sedule job that given deadline and final answer
def FinalMaxProfit():
    FinalDic_Job = FinalDicForJob()
    MaxDeadline = MaxDedline(max(Dedline))
    for key, values in FinalDic_Job.items():
        Position = (FinalDic_Job[key][1]) - 1
        if MaxDeadline[Position] == None:
            MaxDeadline[Position] = FinalDic_Job[key][0]

        else:
            for i in range(Position - 1, -1, -1):
                if MaxDeadline[i] == None:
                    MaxDeadline[i] = FinalDic_Job[key][0]
                    break

    return sum(MaxDeadline)

print(FinalMaxProfit())