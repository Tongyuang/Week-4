
board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


def flood_fill(input_board, old: str, new: str, x: int, y: int):
    """
    Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    # Implement your code here.
    if len(input_board) <= 0 :
        return
    output_board = [list(input_board[i]) for i in range(len(input_board))]
    m,n = len(output_board),len(output_board[0])
    assert input_board[x][y] == old
    fill_queue = []
    fill_queue.append((x,y))
    while(len(fill_queue)>0):
        k = len(fill_queue)
        for i in range(k):
            (xx,yy) = fill_queue.pop(0)
            output_board[xx][yy] = new
            # check
            for (aa,bb) in [(xx,yy-1),(xx,yy+1),(xx+1,yy),(xx-1,yy)]:
                if (aa>=0 and aa<m) and (bb>=0 and bb<n) and (output_board[aa][bb]==old):
                    fill_queue.append((aa,bb))
    
    return ["".join(output_board[i]) for i in range(m)]

modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....