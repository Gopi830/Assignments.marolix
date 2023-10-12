list=[1587,9887,8754,1087,7654]

def cal_maxlist(list):
    max = list[0]
    for i in range(len(list)):
        if list[i]>max:
            max = list[i]
    print("This is a Maximum Number of list:",max)
cal_maxlist(list)
'''
n = [10,20,30,40]

def maxlist(n):
    max=n[0]
    for i in range(len(n)):
        if n[i]>max:
            max=n[i]
    print("this is a maximum number",max)
maxlist(n)'''
