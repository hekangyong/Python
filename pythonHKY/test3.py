import sys
def moon_weight():
    print("Please enter your cirremt Eartj weight")
    weight = int(sys.stdin.readline())
    print("Please enter the amount your weight might increase each year")
    every = float(sys.stdin.readline())
    print("Please enter the number of years")
    over = int(sys.stdin.readline())
    for i in range(0,over):
        weight += every
        zl = weight * 0.165
    return zl
    
print(moon_weight())
