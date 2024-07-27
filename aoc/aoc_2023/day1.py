# Load data
# iterate over data
# find first digit
# find last digit
# add digits
# sum digits


def main1(filename):
    total = 0
    with open(filename) as f:
        for line in f:
            for c in line:
                if c.isdigit():
                    firstdigit = c
                    break
            for d in reversed(line):
                if d.isdigit():
                    lastdigit = d
                    break
            combnum = int("".join([firstdigit, lastdigit]))
            total = total + combnum
    return total


if __name__ == "__main__":
    print(main1("inputs/2023/1.txt"))
