jobList = ["j1","j2","j3","j4","j5","j6"]
Profit = [200,180,190,300,120,100]
Dedline = [5,3,3,2,4,2]
# jobList = ["j1","j2","j3","j4"]
# Profit = [50,15,10,25]
# Dedline = [2,1,2,1]
JPD = {}

# todo 0 = profile 1 = Dedline
for i in range(len(jobList)):
    JPD[jobList[i]] = Profit[i],Dedline[i]
print(JPD)

# todo sort profit,deadline and jobList acsending order
JobP = []
for key,values in JPD.items():
    JobP.append(JPD[key][0])
JobP.sort()
print(JobP)

# todo final dic according to dessinding order of Profit
FinalDic_Job = {}
for i in range(len(JobP)-1,-1,-1):
    for key, values in JPD.items():
        if JobP[i]==JPD[key][0]:
            FinalDic_Job[key] = values

print(FinalDic_Job)

# todo create a max list for dedline
MaxDedline = []
for i in range(max(Dedline)):
    MaxDedline.append(None)

# todo sedule job that given deadline and final answer

for key, values in FinalDic_Job.items():
    Position = (FinalDic_Job[key][1]) - 1
    if MaxDedline[Position]==None:
        MaxDedline[Position] = FinalDic_Job[key][0]

    else:
        for i in range(Position-1,-1,-1):
            if MaxDedline[i] == None:
                MaxDedline[i] = FinalDic_Job[key][0]
                break


print(sum(MaxDedline))
print(MaxDedline)