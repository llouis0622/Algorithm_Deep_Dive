T = int(input())
for i in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    val = 1


    def inorder(idx):
        global val
        if idx > N:
            return
        inorder(idx * 2)
        tree[idx] = val
        val += 1
        inorder(idx * 2 + 1)


    inorder(1)
    print(f"#{i} {tree[1]} {tree[N // 2]}")