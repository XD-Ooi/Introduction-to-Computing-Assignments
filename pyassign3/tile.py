"""
Author: 黄新迪 1700094621 元培学院
Python作业 Assign3 (Dec/4/2018)

tile.py: This module provides a function to calculate the possible combination 
of tiling tiles with dimension a & b on a wall with dimension m & n. If the 
possible tiling combination is more than 0, the function will continue to 
prompt the user to select a method to visualize the output on turtle.
"""
import turtle

def wall(m,n):
    """
    m: length of wall, n: width of wall,
    i: row index of each 1 unit sq area of the wall,
    j: column index of each 1 unit sq area of the wall.
    
    The function outputs a dictionary of wall identity(k) for each 1 unit sq 
    of the wall with its respective i and j values."""
    wall = {}
    for i in range(n):
        for j in range(m):
            k = i * m + j
            wall[k] = i,j
    return wall

def tiling(m,a,b,x,y,matrix,combi):
    """
    m: length of wall, 
    a: length of tile, b: width of tile,
    x: first i index of the tile, y: first j index of the tile,
    i: row index of each 1 unit sq area of the wall,
    j: column index of each 1 unit sq area of the wall,
    matrix: status of the wall on being tiled,
    combi: list of combination of tiles that covers the wall completely.
    
    The function outputs the combination of tiles that covers the wall 
    completely in terms of wall identity(k)"""
    tile = [i*m + j for i in range(x,x+b) for j in range(y,y+a)]
    for k in tile:
        matrix[k] = 1
    combi.append(tuple(tile))

def tile_check(m,n,a,b,x,y,matrix):
    """
    m: length of wall, n: width of wall,
    a: length of tile, b: width of tile,
    x: first i index of the tile, y: first j index of the tile,
    i: row index of each 1 unit sq area of the wall,
    j: column index of each 1 unit sq area of the wall,
    matrix: status of the wall on being tiled.
    
    The function checks in the matrix if the wall have space to place
    a tile and returns false if there is no space, true is there is."""
    if x + b > n or y + a > m:
        return False
    else:
        for i in range(x,x+b):
            for j in range(y,y+a):
                k = i*m + j
                if matrix[k] == 1:
                    return False
        return True

def tile_combi(m,n,a,b,wall_identity,matrix,all_ans,combi,x=0,y=0):
    """
    m: length of wall, n: width of wall,
    a: length of tile, b: width of tile,
    x: first i index of the tile, y: first j index of the tile,
    i: row index of each 1 unit sq area of the wall,
    j: column index of each 1 unit sq area of the wall,
    matrix: status of the wall on being tiled,
    all_ans: the final output of all the possible combination,
    combi: list of combination of tiles that covers the wall completely.
    
    The function outputs all the possible combition of tiling the wall."""
    #for the case where the tile is square
    if a == b:
        if tile_check(m,n,a,b,x,y,matrix):
            tiling(m,a,b,x,y,matrix,combi)
            if 0 not in matrix:
                all_ans.append(combi)
            else:
                k = matrix.index(0)
                i,j = wall_identity.get(k)
                tile_combi(m,n,a,b,wall_identity,matrix,all_ans,combi,i,j)
               
    
    #for the case where the tile is not square
    else:
        #if there is space to put the tiles horizontally and vertically
        if tile_check(m,n,a,b,x,y,matrix) and tile_check(m,n,b,a,x,y,matrix):
            combi2 = combi[:]
            matrix2 = matrix[:]
            
            #placing the tile horizontally
            tiling(m,a,b,x,y,matrix,combi)
            if 0 not in matrix:
                all_ans.append(combi)
            else:   
                k = matrix.index(0)
                i,j = wall_identity.get(k)
                tile_combi(m,n,a,b,wall_identity,matrix,all_ans,combi,i,j)
    
            #placing the tile vertically
            tiling(m,b,a,x,y,matrix2,combi2)
            if 0 not in matrix2:
                all_ans.append(combi2)
            else:
                k2 = matrix2.index(0)
                i2,j2 = wall_identity.get(k2)
                tile_combi(m,n,a,b,wall_identity,matrix2,all_ans,combi2,i2,j2)              
        
        #if there is only space to put the tile horizontally
        elif tile_check(m,n,a,b,x,y,matrix):
            tiling(m,a,b,x,y,matrix,combi)
            if 0 not in matrix:
                all_ans.append(combi)
            else:
                k = matrix.index(0)
                i,j = wall_identity.get(k)
                tile_combi(m,n,a,b,wall_identity,matrix,all_ans,combi,i,j)
        
        #if there is only space to put the tile vertically
        elif tile_check(m,n,b,a,x,y,matrix):
            tiling(m,b,a,x,y,matrix,combi)
            if 0 not in matrix:
                all_ans.append(combi)
            else:
                k = matrix.index(0)
                i,j = wall_identity.get(k)
                tile_combi(m,n,a,b,wall_identity,matrix,all_ans,combi,i,j)               
            
    return all_ans

def wall_draw(m,n,combi,wall_identity):
    """
    m: length of wall, n: width of wall
    combi: selected list of tiles combination that covers the wall completely.
    
    The function outputs a graphic of the selected method of tiling that covers
    the wall completely. The recommended values of m & n are less than 25 for 
    optimum visualization.
    """
    x = m*100
    y = n*100
    
    t = turtle.Turtle()
    t.speed(0)
    t.ht()
    t.shape("blank")
    turtle.screensize(1000,1000)
    if m <= 5 or n <= 5:
        turtle.setworldcoordinates(-x,-y,x,y)
    elif m <= 10 or n <= 10:
        turtle.setworldcoordinates(-x+100,-y+100,x-100,y-100)
    else:
        turtle.setworldcoordinates(-x+400,-y+400,x-400,y-400)
    
    #outline of the wall
    t.pu()
    t.setpos(-x/2,y/2)
    t.pd()
    for p in range(2):
       t.fd(x)
       t.right(90)
       t.fd(y)
       t.right(90)
    
    #separate the wall into n rows and m columns
    for q in range(1,m):
        separation = x/m * q
        t.pu()
        t.setpos(-x/2 + separation,y/2)
        t.setheading(270)
        t.pd()
        t.fd(y)
    
    for r in range(1,n):
        separation = y/n * r
        t.pu()
        t.setpos(-x/2,y/2 - separation)
        t.setheading(0)
        t.pd()
        t.fd(x)
    
    #write the wall identity(k) on the wall
    t.pu()
    for i in range(n):
        if m > 5 or n > 5:
            t.sety(y/2 - (y/n)/2 - 20 - (y/n)*i)
        else:
            t.sety(y/2 - (y/n)/2 - (y/n)*i)
        for j in range(m):
            t.pu()
            t.setx(-x/2 + (x/m)/2 + (x/m)*j)
            if m > 15 or n > 15:
                t.write(str(i*m + j), align = "center", font = ("Arial",6,"normal"))
            else:
                t.write(str(i*m + j), align = "center", font = ("Arial",8,"normal"))
    t.ht()
    
    #draw the combination of tiles on the wall
    u = turtle.Turtle()
    u.speed(0)
    u.shape("classic")
    u.pensize(2)
    u.color("blue")
    u.pu()
    u.st()
    for tile in combi:
        smallest = min(tile)
        largest = max(tile)
        i_small, j_small = wall_identity.get(smallest)
        i_large, j_large = wall_identity.get(largest)
        u.setpos(-x/2 + x/m * j_small, y/2 - y/n * i_small)
        u.setheading(0)
        u.pd()
        for p in range(2):
            u.fd(x/m + (x/m * (j_large - j_small)))
            u.right(90)
            u.fd(y/n + (y/n * (i_large - i_small)))
            u.right(90)
        u.pu()
        
    turtle.done()                

def main():
    """
    The function runs the calculation part of tile.py to output the possible
    combination of complete tiling patterns from user's dimension inputs, then 
    prompt the user to select a method of tiling and display it graphically.
    """
    m = int(input("length of wall:"))
    n = int(input("width of wall:"))
    a = int(input("length of tile:"))
    b = int(input("width of tile:"))   
    
    if m*n % a*b != 0:
        error1 = "Wall cannot be covered completely by given tile dimension." + "\n" + "Unable to perform calculation."
        print(error1)
        return error1
    elif m == n == a == b:
        error2 = "The tile is the size of the wall. No need for any calculations."
        print(error2)
        return error2
    else:
        matrix = [0]*(m*n)
        wall_identity = wall(m,n)
        final = tile_combi(m,n,a,b,wall_identity,matrix,[],[])
        num = len(final)
        for p in range(num):
            print(final[p],"\n")
        print("Total number of possible combination:{0}".format(num))
        max_num = num - 1
        choice = int(turtle.numinput("How to tile the wall?","Select a tiling method from 0 - " + str(max_num), None, 0, max_num))
        method = final[choice]
        wall_draw(m,n,method,wall_identity)
        
if __name__ == "__main__":
    main()
