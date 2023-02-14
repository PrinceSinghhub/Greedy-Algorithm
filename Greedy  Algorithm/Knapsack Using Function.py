item = 4
profit = [9,8,7,6]
waight = [10,2,8,16]
MaxProfit = 0
W = 10

def find_ratio_set_in_Dic(item):
    ratio_data = {}
    for i in range(item):
        r = profit[i] / waight[i]
        ratio_data[r] = profit[i], waight[i]
    return ratio_data

def sort_ratio():
    sortRatio = find_ratio_set_in_Dic(item)
    ratio = []
    for key, value in sortRatio.items():
        ratio.append(key)
    ratio.sort()
    return ratio

def dataSet_AccordingTo_Ratio():
    ratio = sort_ratio()
    sortRatio = find_ratio_set_in_Dic(item)
    dic_data = {}
    for i in range(len(ratio) - 1, -1, -1):
        for key, value in sortRatio.items():
            if ratio[i] == key:
                dic_data[key] = value

    return dic_data

def findMax_Profit(MaxProfit,W):

    dic_data = dataSet_AccordingTo_Ratio()

    for key, value in dic_data.items():

        if W > 0 and dic_data[key][1] <= W:

            MaxProfit = MaxProfit + dic_data[key][0]
            W = int(W - dic_data[key][1])



        else:
            if W > 0 and dic_data[key][1] > W:
                div = W / dic_data[key][1]
                Pi = dic_data[key][0]
                MaxProfit = MaxProfit + (div * Pi)
                W = int(W - (div * Pi))
    return MaxProfit

print(findMax_Profit(MaxProfit,W))