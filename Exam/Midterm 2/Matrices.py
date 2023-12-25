
def main():
    A = matrixA()
    B = matrixB()
    C = matrixC(A, B)
    print(A)
    print(B)
    print(C)

def matrixA(): # Build a matrix A
    
    A = []

    for i in range(2):
        row = []
        for j in range(3):
            num = int(input())
            row.append(num)
        A.append(row)
    return A

def matrixB(): # Build a matrix B
    
    B = []

    for i in range(2):
        row = []
        for j in range(3):
            num = int(input())
            row.append(num)
        B.append(row)
    return B

def matrixC(A, B): # Combine matrices A and B
    
    C = []

    for i in range(2):
        row = []
        for j in range(3):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C    

if __name__ == "__main__":
    main()