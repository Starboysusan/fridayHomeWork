#Print Chess board (alternate black and white squares)
#print('\u25A0') - will print white Square. You can use "B" to print black squares

size = 8  # Size of the chessboard

for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 0:
            print('\u25A0', end=' ')  # White square
        else:
            print('B', end=' ')       # Black square
    print()  # Move to the next row

