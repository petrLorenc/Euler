

maxValue = 1000000
# maxValue = 1000

def dec_to_bin(x):
    return bin(int(x))[2:]

sumValues = 0


for num in range(1,maxValue,1):
    if(str(num) == str(num)[::-1] and str(dec_to_bin(num)) == str(dec_to_bin(num))[::-1]):
        # print(str(num) + " " + dec_to_bin(num))
        sumValues += num



print( sumValues )













