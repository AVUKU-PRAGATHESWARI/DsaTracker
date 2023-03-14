class solution(object):
    def setzeroes(self,matrix):
        r=len(matrix)
        c=len(matrix[0])
        rows,cols=set(),set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    rows.add(i)
                    cols.add(j)
        for i in range(r):
            for j in range(c):
                if i in rows or j in cols:
                    matrix[i][j]=0
obj1=solution()
matrix=[[1,2,3],[4,0,6],[1,3,1]]
obj1.setzeroes(matrix)
for i in range(3):
    for j in range(3):
        print(matrix[i][j],end=" ")
    print()

