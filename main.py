import random as r

size = int(input("Enter number of cities to generate: "))
# this week was busy but I would have liked to try using pandas to implement this table
sample = [[(r.randint(1,9) if x!=y else 0) for y in range(size)] for x in range(size)] # random prices 1-9

# column headings
print(" ",end="\t")
for x in range(size):
    print(x,end=" ")
print()
# establishes one price to go either way (ex: A -> B costs $4, and B -> A also costs $4), and displays matrix
for row in range(size):
    print(row, end="\t")
    for col in range(size):
        sample[row][col] = sample[col][row] 
        print(sample[row][col],end=" ")
    print()

naiveTSP(sample)
def naiveTSP(mat):
    pass