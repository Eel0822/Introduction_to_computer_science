#H24126094 統計116 李繕安
def candyCrush(board):
    def mark_crushable(board):
        rows, cols = len(board), len(board[0])
        crush = set()
        
        # Mark crushable candies horizontally
        for r in range(rows):
            for c in range(cols - 2):
                if board[r][c] != 0 and board[r][c] == board[r][c + 1] == board[r][c + 2]:
                    crush.update([(r, c), (r, c + 1), (r, c + 2)])
        
        # Mark crushable candies vertically
        for r in range(rows - 2):
            for c in range(cols):
                if board[r][c] != 0 and board[r][c] == board[r + 1][c] == board[r + 2][c]:
                    crush.update([(r, c), (r + 1][c), (r + 2)[c]])
        
        return crush

    def drop_candies(board):
        rows, cols = len(board), len(board[0])
        for c in range(cols):
            wr = rows - 1
            for r in range(rows - 1, -1, -1):
                if board[r][c] != 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for wr in range(wr, -1, -1):
                board[wr][c] = 0
    
    while True:
        crush = mark_crushable(board)
        if not crush:
            break
        for r, c in crush:
            board[r][c] = 0
        drop_candies(board)
    
    return board

print("Original Board:")
for row in board:
    print(row)

result = candyCrush(board)

print("\nStable Board:")
for row in result:
    print(row)