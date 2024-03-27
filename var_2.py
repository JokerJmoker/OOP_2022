import time

from random import *
"""
    n=randint(3,5)
    m=randint(3,5)
    """
def pr(mat):
    for n in mat:
        print(" ".join(map(str, n)))

    """
    m=3
    n=3
    mat=[[1,1,1],[0,1,0],[1,1,0]]
    """


def check(i,j):
    return 0 <= i < len(mat) and 0 <= j < len(mat[0])

res=0
tryy=0
while res == 0 :

    m=4
    n=4

    print("common")
    print("\n")

    mat=[[randint(0,1) for _ in range(n)] for _ in range(m) ]
   
    #записать одну 2 в матрицу

    pos_i=randint(0, m -1)
    pos_j=randint(0, n -1)
    
    mat[pos_i][pos_j]=2

    print("\n")

    pr(mat)

    print("\n")
 
    
    cntr=0
    while True:

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                
                if mat[i][j]==2:
                    
                    if  check(i+1,j) == True and mat[i+1][j]==1:
                        mat[i+1][j]=2
                        
                    if  check(i-1,j) == True and mat[i-1][j]==1: 
                        mat[i-1][j]=2
                        
                    if  check(i,j+1) == True and mat[i][j+1]==1:
                        mat[i][j+1]=2
                        
                    if  check(i,j-1) == True and mat[i][j-1]==1:
                        mat[i][j-1]=2
                        
                    time.sleep(0.2)
        cntr+=1
        print("\n")
        print("new \n")
        pr(mat)

        count_of_two = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 2:
                    count_of_two += 1
        
        count_of_one = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    count_of_one += 1


        cntr_no_1_around_for_2 = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j]==2:
                    if  (check(i+1,j) == False or mat[i+1][j]!=1) and (check(i-1,j) == False or mat[i-1][j]!=1) and (check(i,j+1) == False or mat[i][j+1]!=1) and (check(i,j-1) == False or mat[i][j-1]!=1):
                        cntr_no_1_around_for_2 += 1
        """
        print("\n")
        print(count_of_two)
        print(cntr_no_1_around_for_2)
        print("1",count_of_one)
        """
        if  count_of_two == cntr_no_1_around_for_2 and count_of_one == 0:
            res=cntr
            print( "\n" ,"time for mat  ===", res ,"\n" )
            break
            
        if  count_of_two == cntr_no_1_around_for_2  and count_of_one !=0:
            
            print( "\n" ,"-1","\n" )
            break
    tryy+=1

    if res != 0:
        print("time for try", tryy)