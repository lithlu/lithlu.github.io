# Author:Lithlu
date = {
    "北京":{
        "昌平":{
            "沙河":["oldboy","test"],
            "天通苑":["链家电产","我爱我家"]
        },
        "朝阳":{
            "望京":["奔驰","陌陌"],
            "国贸":["CICC","HP"],
            "东直门":["Advent","飞信"]
        },
        "海淀":{

        }
    },
    "山东":{
        "济南":{},
        "青岛":{},
        "德州":{}
    },
    "广东":{
        "东莞":{},
        "常熟":{},
        "佛山":{}
    }
}
exit_flag = False
while not exit_flag:
    for i in date:
        print(i)
    choice = input("选择进入1：")
    if choice in date:
        while not exit_flag:
            for i2 in date[choice]:
                print("\t",i2)
            choice2 = input("选择进:2：")
            if choice2 in date[choice]:
                while not exit_flag:
                    for i3 in date[choice][choice2]:
                        print("\t\t",i3)
                    choice3 = input("选择进入3：")
                    if choice3 in date[choice][choice2]:
                        for i4 in date[choice][choice2][choice3]:
                            print("\t\t\t",i4)
                        choice4 = input("最后一层，按q返回顶层，按b返回上一层：")
                        if choice4 == "b":
                            pass
                        elif choice4 == 'q':
                            exit_flag = True
                        else:
                            print("您的输入有误！请重新输入：")
                            choise4 = input("最后一层，按q返回顶层，按b返回上一层：")
                    else:
                        print("你输入的菜单不存在！请重新输入：")
                        
                        choice3 = input("选择进入3：")

                    if choice3 == "b":
                        break
                    elif choice3 == 'q':
                        exit_flag = True
            else:
                print("你输入的菜单不存在！请重新输入：")

                choice2 = input("选择进入2：")

            if choice2 =="b":
                break
            elif choice2 == 'q':
                exit_flag = True
    else:
        print("你输入的菜单有误，请重新输入：")
        choice = input("选择进入1：")



