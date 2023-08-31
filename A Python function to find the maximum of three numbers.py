Write a Python function to find the maximum of three numbers.

_1st_num = 54
_2nd_num = 46
_3rd_num = 65

def max_two_num(x,y):
    if x>y:
        return x
    else:
        return y
#print(max_two_num(5,10))

def max_three_num(x,y,z):
    return max_two_num(x,max_two_num(y,z))
print(max_three_num(_1st_num, _2nd_num, _3rd_num))
