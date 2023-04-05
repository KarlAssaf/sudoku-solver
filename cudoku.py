from math import floor
import tkinter as tk
#board1 = [[".",".",".","8",".","1",".",".","."],[".",".",".",".",".",".",".","4","3"],["5",".",".",".",".",".",".","." ,"."],[".",".",".",".","7",".","8",".","."],[".",".",".",".",".",".","1",".","."],[".", "2", ".", ".", "3", ".", ".", ".", "."], ["6",".", ".",".",".",".",".","7","5"],[".",".","3","4",".",".",".",".","."],[".",".",".","2",".",".","6",".","."]]
board1 = []
def get_user_input():
    global n
    global board1
    for i in range(0, 9):
        div = []
        for j in range(0, 9):
            div.append("".join(globals()["sq"+str(i)+str(j)].get(1.0, "end-1c").split(" ")))
        board1.append(div)
    print(board1)
    prep(board1)
    do(board1, cols1, cars1)
    if CFU(board1) != True:
       for i in board1:
           print(i)
    else:
      while (CFU(board1) == True):
         n += 1
         globals()["i" + str(n)] = 0
         result = recursive()
         if len(result) == 9:
            for i in result:
                print(i)
         elif result == "impossible":
            print(result)
n = 1
i1 = 0
root = tk.Tk()
root.geometry("900x900")
frame = tk.Frame(root)
frame.pack()
for i in range(0, 9):
    for j in range(0, 9):
        color = "red" if (i < 3 and j < 3) else "blue" if (i < 3 and j < 6) else "yellow" if (i < 3 and j < 9) else "green" if (i < 6 and j < 3) else "pink" if (i <6  and j < 6) else "white" if (i < 6 and j < 9) else "cyan" if (i < 9 and j < 3) else "orange" if (i < 9 and j < 6) else "lime"
        globals()["sq"+str(i)+str(j)] = tk.Text(frame, height=1, width=2, bg=color, font=("Arial", 35))
        globals()["sq"+str(i)+str(j)].tag_configure("center", justify='center')
        globals()["sq"+str(i)+str(j)].insert(1.0, " ")
        globals()["sq"+str(i)+str(j)].tag_add("center", "1.0", "end")
        globals()["sq"+str(i)+str(j)].grid(row=i, column=j)
btn = tk.Button(root, command=get_user_input, text="begin solving")
btn.pack()

cols1 = [["0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0"]]
cars1 = [["0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0"],["0", "0", "0", "0", "0", "0", "0", "0", "0"]]
acceptables = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def copyarr(copi):
    nc = []
    for i in copi:
        nc.append(i.copy())
    return nc

def prep(b):
            for row in b:
                missing = []
                for n in acceptables:
                    if n not in row:
                        missing.append(n)
                for i, j in enumerate(row):
                    if j not in acceptables:
                        row[i] = "/".join(missing)


def map_rows(b, c, d):
 for rowi, row in enumerate(b):
  for coli, j in enumerate(row):
   c[coli][rowi] = j
   d[floor(rowi/3) + floor(coli/3)*3][coli%3 + (rowi%3)*3] = j


def map_cols(b, c, d):
 for coli, col in enumerate(c):
  for rowi, j in enumerate(col):
   b[rowi][coli] = j
   d[floor(rowi/3)*3 + floor(coli/3)][(rowi%3)*3 + coli%3] = j

def map_squares(b, c, d):
 for cind, car in enumerate(d):
  for iind, j in enumerate(car):
   b[floor(cind/3)*3 + floor(iind/3)][(cind%3)*3 + iind%3] = j
   c[(cind%3)*3 + iind%3][floor(cind/3)*3 + floor(iind/3)] = j

def remove_uncertainties(b):
 for row in b:
  for ind, case in enumerate(row):
   if len(case) > 1:
    x = case.split("/")
    for i in x:
     if i in row:
      x.remove(i)
    row[ind] = "/".join(x)


def CFU(b):
    if b == "impossible":
        return False
    for i in b:
        for j in i:
            if len(j) > 1:
               return True 
    return False

def getsmallest(b):
    smallest = ["1/2/3/4/5/6/7/8/9", 8, 8]
    for ind, i in enumerate(b):
        for jnd, j in enumerate(i):
            if len(j) > 1 and len(j) < len(smallest[0]):
               smallest[0] = j
               smallest[1] = ind
               smallest[2] = jnd
            if len(smallest[0].split("/")) == 2:
               return smallest
    return smallest



def CFD(b):
    for i in b:
        for jnd, j in enumerate(i):
            if len(j) == 1 and j == i[jnd - 1]:
               return True               
    return False

def CFD(b):
    for i in b:
        for jnd, j in enumerate(i):
            for knd, k in enumerate(i):
                if jnd != knd and i[jnd] == i[knd] and len(j) == 1:
                   return True               
    return False

def do(b, c, d):
 for n in range(0, 3):
  map_rows(b, c, d)
  remove_uncertainties(c)
  map_cols(b, c, d)
  remove_uncertainties(d)
  map_squares(b,c,d)
  remove_uncertainties(b)


def recursive():
    global n
    global board1
    if (n != 1):
        globals()["board" + str(n)] = copyarr(globals()["board" + str(n-1)])
        globals()["cols" + str(n)] = copyarr(globals()["cols" + str(n-1)])
        globals()["cars" + str(n)] = copyarr(globals()["cars" + str(n-1)])
        among = getsmallest(globals()["board" + str(n)])
        globals()["sm" + str(n)] = among[0]
        if (globals()["i" + str(n)] < len(globals()["sm" + str(n)].split("/"))):
            globals()["board" + str(n)][getsmallest(globals()["board" + str(n)])[1]][getsmallest(globals()["board" + str(n)])[2]] = globals()["sm" + str(n)].split("/")[globals()["i" + str(n)]]
            do(globals()["board" + str(n)], globals()["cols" + str(n)], globals()["cars" + str(n)])
            if CFD(globals()["board" + str(n)]) or CFD(globals()["cols" + str(n)]) or CFD(globals()["cars" + str(n)]):
                globals()["i" + str(n)] = globals()["i" + str(n)] + 1
                return recursive()
            else:                    
                if CFU(globals()["board" + str(n)]):
                   return "X"
                else:
                    board1 = globals()["board" + str(n)]
                    cols1 = globals()["cols" + str(n)]
                    cars1 = globals()["cars" + str(n)]

                    return board1
        else: 
            n -= 1
            globals()["i" + str(n)] = globals()["i" + str(n)] + 1
            return recursive()
    else:
        board1 = "impossible"
        return "impossible"

root.mainloop()

