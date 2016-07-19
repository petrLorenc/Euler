
def divide(n, divider, residuals):
    if(n % divider == 0):
        # print(str_rest)
        return 0
    if n < divider:
        n *= 10
    divider_factor = int(n/divider)
    n = n - divider_factor*divider
    try:
        position_of_repeat = residuals.index(n)
    except ValueError as a:
        position_of_repeat = -1
    if position_of_repeat != -1:
        return len(residuals) - position_of_repeat
    else:
        residuals.append(n)
        return divide(n,divider, residuals)

global_max = 0
global_num = 0
for x in range(1,1001,1):
    temp = divide(1,x, [])
    if(temp > global_max):
        global_max = temp
        global_num = x

print("Number {} has reciprocal cycle with length of {}".format(global_num,global_max))











