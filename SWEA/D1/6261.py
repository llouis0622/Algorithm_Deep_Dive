beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}
print(beer)
S = {i: j * 1.05 for i, j in beer.items()}
print(S)