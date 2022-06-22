
with open("./1/input.txt") as f:
    lines = f.readlines()

def how_many_increases(input, window_size=1):
    """
    Counts the number of increases from one window from the previous.

    This function compates the sum of values in a sliding window to the sum of
    values in the window in its previous postion.
    
    Arguments
    ---------
    input - a list of integer strings
    window_size - the size of overlapping windows to compare

    Returns
    -------
    The number of increases.
    """
    
    heights = [int(x) for x in input]

    count = 0
    offset = window_size

    for i in range(offset,len(heights)):
        if(heights[i-offset] < heights[i]):
            count += 1
    
    return count

rslt = how_many_increases(lines)

print(rslt)

rslt_2 = how_many_increases(lines, 3)

print(rslt_2)
print("hello")