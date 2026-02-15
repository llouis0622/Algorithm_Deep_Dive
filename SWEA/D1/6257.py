fruit = ['   apple    ', 'banana', '  melon']
A = {i.strip(): len(i.strip()) for i in fruit}
print(A)