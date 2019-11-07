#%%
import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    my_list = []
    random.seed(70)
    for i in range(0,10,1):
        num1=random.random()
        rnum1=random.randint(30,34)
        rnum2 = num1 + rnum1
        my_list.append(rnum2)
    print(my_list)
    