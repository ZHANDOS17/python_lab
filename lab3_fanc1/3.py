numheads = input()
numlegs = input()

def solve(numheads, numlegs):
    y = (numlegs - 2*numheads)/2
    x = numheads - y
    print(x, y)
    
solve(numheads, numlegs)


