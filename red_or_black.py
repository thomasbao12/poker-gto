memo = {}
def f(r, b):
    if memo.get((r,b)):
        return memo.get((r,b))
    if r == 0:
        memo[(r,b)] = 0
        return 0
    elif b == 0:
        memo[(r,b)] = 1
        return 1
    bet_now = float(r) / (r + b)
    bet_later = ( f(r - 1, b) + f(r, b -1) ) / 2.0
    result = max(bet_now, bet_later)
    memo[(r,b)] = result
    return result

red = 2
black = 2
print( f(red, black) )

for r in range(1, red + 1):
    line = []
    for b in range(1, black + 1):
        line.append(str(memo[(r,b)]))
    print(" ".join(line))
