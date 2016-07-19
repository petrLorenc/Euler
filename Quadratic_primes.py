
import math


def is_prime(number):
    if number % 2 == 0 or number <=1:
        return False
    for x in range(3, int(math.sqrt(number)), 2):
        if number % x == 0:
            return False
    return True

def euler_formula(n, a, b):
    return math.pow(n,2) + a*n + b

def test_euler_formule_for_a_b(a,b):
    counter = 0
    n = 0
    while is_prime(euler_formula(n,a,b)):
        counter += 1
        n += 1
    return counter

best_count = 0
best_a = 0
best_b = 0

if __name__ == "__main__":
    for a in range(-1001,1001,1):
        for b in range (-1001, 1001,1):
            temp_count = test_euler_formule_for_a_b(a,b)
            if(temp_count >= best_count):
                best_count = temp_count
                best_a = a
                best_b = b

    print("a:{} * b:{} = {}\n count:{}".format(best_a,best_b,best_a*best_b,best_count))








