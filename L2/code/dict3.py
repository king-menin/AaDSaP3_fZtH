A = {'ab': 'ba', 'aa': 'aa', 'bb': 'bb', 'ba': 'ab'}

key = 'ac'
if A.get(key) is not None:
    del A[key]

try:
    del A[key]
except KeyError:
    print('There is no element with key "' + key + '" in dict')
print(A)
