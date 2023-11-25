'''
给定一个n*m的网格，在网格中每次在不超过边界的情况下可以选择向上、向下、向左、向右移动一格。网格中的一些格子上放置有障碍物，放有障碍物的格子不能到
达，求从（x0,y0）到（x1,y1）的最短距离

输入案例：
5 5 #表示n m（行数与边数）
1 1 5 5 #x0,y0,x1,y1（这里的x0,y0按照数组的访问顺序）
.....
****.
.....
**.**
.....
（其中.表示没有障碍，*表示存在障碍）

'''

import sys


s = input()
L = s.split()
n,m = int(L[0]),int(L[1])
L2 = input().split()
s = []
x0,y0,x1,y1 = int(L2[0])-1,int(L2[1])-1,int(L2[2])-1,int(L2[3])-1
#print("x0 y0 x1 y1: ",x0,y0,x1,y1)


#initialize the map according to the input

def InitializeMap(n,m):
    for i in range(0,n):
        line=list(input())
        newline = []
        for j in range(0,m):
            if(line[j] == '*'):
                newline.append(0)
            else:
                newline.append(1)
        s.append(newline)



def SearchMap(x1,y1,x2,y2,n,m):
    #initialize
    directionx = [0,0,1,-1]
    directiony = [1,-1,0,0]
    distance = [[0 for i in range(m)] for i in range(n)]
    visited = [[0 for i in range(m)] for i in range(n)]
    queue = []
    queue.append([x1,y1])
    distance[x1][y1] = 0
    visited[x1][y1] = 0
    while(queue):
        q = queue.pop(0)
        x_o,y_o = q[0],q[1]
        for i in range(4):
            x = x_o+directionx[i]
            y = y_o+directiony[i]
            if(x<0 or x>=n or y<0 or y>=m):
                continue
            if(s[x][y]==0):
                continue
            if(0<=x<n and 0<=y<m):
                if(visited[x][y]==0):
                    visited[x][y] = 1
                    distance[x][y] = distance[x_o][y_o]+1
                    queue.append([x,y])
    return distance

#queue = [1,2,3,1,2,4]
#print(queue)
#print(s[0][1])
#distance = SearchMap(x0,y0,x1,y1,n,m)
#print(distance)
InitializeMap(n,m)
#print(s)

distance = SearchMap(x0,y0,x1,y1,n,m)
#print(s)
#print(distance)
if(s[x1][y1] == 0 or distance[x1][y1] == 0):
    print("-1")
else:
    print(distance[x1][y1])
