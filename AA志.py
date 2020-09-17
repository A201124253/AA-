def cal_money():
    # input the name and the money
    # num = int(input("please input the number: "))
    num = int(input("请输入聚餐人数: "))
    print("请输入名字和钱数\n 如: 张三 20\n")

    p_m = {}
    s = 0
    for i in range(num):
        p, m = input().split()
        p_m[p] = float(m)
        # print(p,m)
        
        # calculate the average number 
        s = s + float(m)
        ave = s/(i+1)
    print('-'*18)
    print("我们一共吃了{}\n平均每人{:.2f}".format(s, ave))
    print('-'*15)
    for p, m in p_m.items():
        # print(p_m[p_m_a])
        p_m[p] = ave - m
        print(p , ':' , "%.2f"%p_m[p])
    #print(p_m)


if __name__ =="__main__":
    cal_money()
