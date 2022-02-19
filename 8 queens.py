
def print_chessboard(col_val):
    for y in range(8):
        thisarray = ["x","x","x","x","x","x","x","x"]
        thisarray[col_val[y]] = "0"
        print(thisarray)

def is_valid(col_val):
    for x in range(7):
        for y in range(x+1,8):
            if col_val[x] == col_val[y]:
                return "same column"
            if x-y == col_val[x]-col_val[y] or x-y == col_val[y]-col_val[x]:
                return "diagonal"
    return "valid board"



column_val = [0,0,7,0,5,0,0,0]  #each position on list represents a row
counter = 0

for a in range(8):
    for b in range(8):
        for c in range(8):
            for d in range(8):
                for e in range(8):
                    for f in range(8):
                        for g in range(8):
                            for h in range(8):
                                column_val = [a,b,c,d,e,f,g,h]
                                response = is_valid(column_val)
                                if response == "valid board":
                                    counter +=1
                                    print("\nSolution",counter,":",column_val)
                                    print_chessboard(column_val)
                                    
print(counter,"solutions found")
