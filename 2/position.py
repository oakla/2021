

with open('projects/advent-code/2021/2/input.txt', "r") as fp:
    input = fp.readlines()

aim = 0
pos = 0
depth = 0

for line in input:
    xs = line.split(' ')
    direction = xs[0]
    x = int(xs[1].strip())
    match direction:
        case "forward":
            pos += x
            depth += aim * x
        case "down":
            aim += x
        case "up":
            aim -= x

print(pos, depth)
print(pos * depth)

    
