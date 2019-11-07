#%%
import random

def problem2_6():
    """ Simulates rolling 2 dice 100 times """
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier. 431
    
    random.seed(431)  # don't remove when you submit for grading
    for i in range(0,100):
        rnum1=random.randint(1,6)
        rnum2=random.randint(1,6)
        rnum_sum = rnum1 + rnum2
        print(rnum_sum)
