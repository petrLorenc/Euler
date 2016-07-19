import itertools

def test_number_for_pandigital(multiplicand, multiplier, product):
    whole_set = set()
    whole = str(multiplicand) + str(multiplier) + str(product)
    if len(whole) != 9:
        return False
    for x in whole:
        whole_set.add(x)
    return len(whole_set) == 9 and "0" not in whole_set

# itertools is for effect of nested loop and a*b for optimizing 9999 * 1 = 9999 (product can have more than 4 digits)
results = [(a,b,a*b) for a,b in itertools.product(range(1,10000,1), range(1,10000,1)) if a*b < 10000 and test_number_for_pandigital(a,b,a*b) ]
# print(results)
# generate set where would be unique variables
results_products = {c for (a,b,c) in results}
print(sum({c for (a,b,c) in results}))

# print(test_number_for_pandigital(39,186,7254))
# print(test_number_for_pandigital(463,825,381975))



