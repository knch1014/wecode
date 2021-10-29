def Get_Even_Numver(num):
    result=[]
    for i in num:
        if i > 0 and i <50 and i%2 ==0:
            result.append(i)
    return result
