import random as r
import itertools # standard library containing permutations function

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

def totalDistance(origin, route, mat):
    total = 0
    current = origin

    for next in route:
        total += mat[current][next]
        current = next
    
    return total + mat[current][origin]



def naiveTSP(mat):
    n = len(mat)
    origin = 0
    otherCities = [x for x in range(1,n)]
    
    minDistance = float('inf')
    bestRoute = []

    for route in itertools.permutations(otherCities):
        currentDistance = totalDistance(origin, route, mat)
        
        if currentDistance < minDistance:
            minDistance = currentDistance
            bestRoute = list(route)
            bestRoute.insert(origin, 0)
    
    return bestRoute
    


best = naiveTSP(sample) # test function
print(f"The best route is {best}, which costs ${totalDistance(0, best, sample)-sample[best[-1]][0]}")