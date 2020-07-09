primes = {2, 3, 5, 7, 11}
for num in primes:
    print(num)

target = 11
search_result = False
for num in primes:
    if target == num:
        search_result = True
if search_result:
    print(target, "in primes set")
else:
    print(target, " not in primes set")
