S = 'ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC'
A = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
num = 0
for i in S:
    if i in A:
        num += A[i]
print(num)