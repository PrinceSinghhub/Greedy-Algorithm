item = 6
profit = [20,15,7,5,9,3]
waight = [10,5,6,3,7,9]
ratio_data = {}
W = 20

# item = 4
# profit = [9,8,7,6]
# waight = [10,2,8,16]
# ratio_data = {}
# W = 10
MaxProfit = 0

# todo find a ratio b/w profit/waight and set value with 0 = profit 1 = weight in dic
for i in range(item):
    r = profit[i]/waight[i]
    ratio_data[r] = profit[i],waight[i]

print(ratio_data)
# todo sort ratio
ratio = []
for key,value in ratio_data.items():
    ratio.append(key)
ratio.sort()

# todo final data set according to increasing ratio order
dic_data = {}
for i in range(len(ratio)-1,-1,-1):
    for key, value in ratio_data.items():
        if ratio[i]==key:
            dic_data[key] = value

# todo for find MAX OR OPTIMAL MaxProfit
for key, value in dic_data.items():

    if W>0 and dic_data[key][1]<=W:

        MaxProfit = MaxProfit + dic_data[key][0]
        W = int(W-dic_data[key][1])



    else:
        if W > 0 and dic_data[key][1] > W:

            div = W / dic_data[key][1]
            Pi = dic_data[key][0]
            MaxProfit = MaxProfit + (div * Pi)
            W = int(W - (div * Pi))

print(MaxProfit)
print(dic_data)