




th_values = [1,10,100,1000,10000,100000,1000000]


limit = 1000000
# limit = 20
decimalFraction = ""
counter = 1

while len(decimalFraction) < limit:
    decimalFraction += str(counter)
    counter += 1

result = 1
for x in th_values:
    print(int(decimalFraction[x-1]))
    result *= int(decimalFraction[x-1])

for x in range(1, 101):
    print("{}th is {}".format(x, decimalFraction[x-1]))

print(result)

