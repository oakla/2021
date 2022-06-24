

with open('projects/advent-code/2021/2/input.txt', "r") as fp:
    input = fp.readlines()

depth = 0
pos = 0

for x in input:
    xs = x.split(' ')
    direction = xs[0]
    match direction:
        case "forward":
            pos += int(xs[1].strip())
        case "down":
            depth += int(xs[1].strip())
        case "up":
            depth -= int(xs[1].strip())

print(pos, depth)
print(pos * depth)

    
