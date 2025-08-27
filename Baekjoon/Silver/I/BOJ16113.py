import sys

input = sys.stdin.readline
n = int(input().strip())
s = input().strip()
w = n // 5
row = [s[i * w:(i + 1) * w] for i in range(5)]
col = [row[0][i] + row[1][i] + row[2][i] + row[3][i] + row[4][i] for i in range(w)]
temp = {
    ''.join(["###", "#.#", "#.#", "#.#", "###"]): '0',
    ''.join(["###", "..#", "###", "#..", "###"]): '2',
    ''.join(["###", "..#", "###", "..#", "###"]): '3',
    ''.join(["#.#", "#.#", "###", "..#", "..#"]): '4',
    ''.join(["###", "#..", "###", "..#", "###"]): '5',
    ''.join(["###", "#..", "###", "#.#", "###"]): '6',
    ''.join(["###", "..#", "..#", "..#", "..#"]): '7',
    ''.join(["###", "#.#", "###", "#.#", "###"]): '8',
    ''.join(["###", "#.#", "###", "..#", "###"]): '9',
}
i = 0
ans = []
while i < w:
    if col[i] == '.....':
        i += 1
        continue
    if col[i] == '#####' and (i + 1 == w or col[i + 1] == '.....'):
        ans.append('1')
        i += 1
    else:
        res = row[0][i:i + 3] + row[1][i:i + 3] + row[2][i:i + 3] + row[3][i:i + 3] + row[4][i:i + 3]
        ans.append(temp[res])
        i += 3
print(''.join(ans))