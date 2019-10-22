
puzzle = []

def initialize():
    i=1
    for j in range(3):
        row = []
        for i in range(3):
            item = [[i,i,i],[i,i,i],[i,i,i]]
            row.append(item)
            i+=1
        else:
            puzzle.append(row)

def mapperxy(x,y,z=-1):                     #x for row and y for column
    if z!=-1 and z>0 and z<=9 :
        puzzle[int(x/3)][int(y/3)][x%3 - 1][y%3 - 1] = z;
        return True
    return puzzle[int(x/3)][int(y/3)][x%3 - 1][y%3 - 1]

def mapperx(x,z=-1):
    if z==-1 and x>8 and x<90:
        return mapperxy(int(x/9),int(x%9))

def getbestvalue(x):
    row = 1

initialize()
print(mapperx(81))
print(puzzle)
