

import math





def is_sum_powers(number):
    str_number = str(number)
    sum_digids = 0
    for x in str_number:
        sum_digids += int(math.pow(int(x),5))
    if sum_digids == number:
        return True
    return False

# umela zarazka ale 9**5 = 59049 a napriklad 7*(9**5)=413343 takze to je limit protoze by muselo byt cislo 7 ciferne ale
# stale mensi nez 413343
a = [x for x in range(2,413343,1) if is_sum_powers(x)]
print(a)
print(sum(a))





