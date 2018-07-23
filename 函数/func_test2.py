# Author:Lithlu
import time

def logger():
    time_format ="%Y-%m-%d-%X"
    time_current = time.strftime(time_format)
    with open("a.txt","a+") as f:
        f.write("%s end action. \n"% time_current)
def func1():
    print("in the test1")
    logger()
def func2():
    print("in the test2")
    logger()
def func3():
    print("in the func3")
    logger()
func1()
func2()
func3()
