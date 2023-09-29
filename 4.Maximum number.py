list=[1587,9887,8754,1087,7654]

def cal_maxlist(list):
    max = list[0]
    for i in range(len(list)):
        if list[i]>max:
            max = list[i]
    print("This is a Maximum Number of list:",max)
cal_maxlist(list)
