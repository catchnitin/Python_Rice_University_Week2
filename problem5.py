#%%
import random


def problem2_5():
    
    """ Simulates rolling a die 10 times."""
    
    random.seed(171)  # don't remove when you submit for grading
    for i in range(0,10):
        rnum1=random.randint(1,6)
        print(rnum1)
