N = 8

moves = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def valid(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def is_knight_move(x1, y1, x2, y2):
    return (abs(x1 - x2), abs(y1 - y2)) in [(1,2), (2,1)]

def degree(x, y, board):
    """jumlah edge (degree) dari vertex"""
    cnt = 0
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if valid(nx, ny, board):
            cnt += 1
    return cnt

def solve(x, y, step, board, start_x, start_y, mode):
    if step == N * N:
        if mode == "open":
            return True
        return is_knight_move(x, y, start_x, start_y)

    # Warnsdorff: pilih vertex dengan degree terkecil
    next_moves = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if valid(nx, ny, board):
            next_moves.append((degree(nx, ny, board), nx, ny))

    next_moves.sort()

    for _, nx, ny in next_moves:
        board[nx][ny] = step
        if solve(nx, ny, step + 1, board, start_x, start_y, mode):
            return True
        board[nx][ny] = -1

    return False

def knights_tour(start_x, start_y, mode="open"):
    board = [[-1]*N for _ in range(N)]
    board[start_x][start_y] = 0

    if solve(start_x, start_y, 1, board, start_x, start_y, mode):
        return board
    return None

start_x, start_y = 1, 2
mode = "open"     # ganti ke closed kalau mau cycle

result = knights_tour(start_x, start_y, mode)

if result:
    print(f"\nKnight's Tour ({mode.upper()}):\n")
    for row in result:
        print(row)
else:
    print("Tidak ditemukan solusi")
