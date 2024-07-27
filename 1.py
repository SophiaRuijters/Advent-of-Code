# Load data
# with open('1.txt') as f: 
#     lines = f.readlines()
#     print(lines)


# iterate over data

# find first digit

# find last digit

# add digits

# sum digits







### Improvement

# Load data
total = 0

with open('1.txt') as f: 
    for line in f:
        for c in line: 
            if c.isdigit(): 
                firstdigit = c
                break
        for d in reversed(line): 
            if d.isdigit():
                lastdigit = d
                break
        combnum = int(''.join([firstdigit, lastdigit]))
        total = total + combnum
        print(total)
        








