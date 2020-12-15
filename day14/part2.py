with open('input') as file:
    lines = file.readlines()
    B = lines[1].strip().split(',')
    constraints = []
    N = 1
    for i, b in enumerate(B):
        if b != 'x':
            b = int(b)
            i %= b
            constraints.append(((b - i) % b, b))
            N *= b

    ans = 0
    for i, b in constraints:
        ni = N // b
        mi = y = pow(ni, -1, b)
        for_b = i * mi * ni
        ans += for_b

    ans %= N
    print(ans)
