list=[10,20,30,40,50]

def cal_list(list):
    sum = 0
    for i in list:
        sum=sum+i
    print(list)
    print("Sum of the list is:",sum)
cal_list(list)