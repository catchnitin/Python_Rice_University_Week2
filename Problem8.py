#%%
def problem2_8(temp_list):
    temp_total = 0
    temp_high  = 0
    temp_min  = 100
    for temp in temp_list:
        temp_total = temp_total + temp
        temp_average = temp_total / len(temp_list)
        if temp > temp_high :
            temp_high = temp
        if temp < temp_min :
            temp_min = temp
        
    print("Average:",temp_average)
    print("High:",temp_high)
    print("Low:",temp_min)
    