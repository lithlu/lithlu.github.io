# Author:Lithlu
product_list = [
    ("Iphone",8700),
    ("Ipad",7811),
    ("ThinkPad",14500),
    ("Iwatch",6000),
    ("Kingdle",4560)
]
shopping_list = []
salary = input("请输入你的工资：")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index ,item in enumerate(product_list):
            print(index,item)#导出商品和编号
        user_choice = input("请选择你要购买的商品：")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:
                    #买得起
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Add %s into the shopping cart ,and your salary is \033[41;1m%s\033[0m"%(p_item,salary))
                else:
                    print("\033[41;1m您的余额只剩[%s]\033[0m"%salary)
            else:
                print("抱歉，您输入的%s商品不存在！"%user_choice)
        elif user_choice == 'q'or user_choice =='Q':
            print("-------shopping_list--------")
            for p in shopping_list:
                print(p)
            print("your balance is :",salary)
            print("----------------------------")
            exit()
        else :
            print("invalid option")
else:
    print("你输入的工资有误！")


