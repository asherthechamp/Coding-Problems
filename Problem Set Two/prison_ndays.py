# Transforms a prison cells state by changig
# it to one if it is in the middle of both empty or both filled cells, and
# to zero otherwise

def prison_ndays(cells, N):
    for i in range(1, N+1):
        cells = transform(cells)
    return cells

def transform(cells):
    new_cell = cells.copy()
    new_cell [0] = new_cell[-1] = 0
    for i in range(1, len(cells) -1):
        if cells[i-1] == cells[i+1]:
            new_cell[i] = 1
        else:
            new_cell[i] = 0
    return new_cell

print (prison_ndays([0,1,0,1,1,0,0,1], 7))