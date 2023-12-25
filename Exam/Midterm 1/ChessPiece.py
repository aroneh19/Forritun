
NumberOfPiece = int(input())

if NumberOfPiece == 9:
    print("Queen")
elif NumberOfPiece == 5:
    print("Rook")
elif NumberOfPiece == 3:
    print("Bishop or Knight")
elif NumberOfPiece == 1:
    print("Pawn")
else:
    print("No piece")