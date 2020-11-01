'''
棋盘覆盖问题
2^k x 2^k个方格 有一个方格与其他方格不同，则该方格为特殊方格；
用L型骨牌覆盖棋盘上除了特殊方格以外的所有方格
分治策略
'''


import tkinter as tk
import numpy as np
BUF_SIZE=2048
cnt = 0

def change_rgb(rgb):
    return "#%02x%02x%02x" % rgb

def countboard(board):
    global countbox
    n = len(board)
    n = n*n
    countbox = [-1 for x in range(n)]
    k = 0
    for i in range(len(board)):
        for j in range(len(board)):
            countbox[k] = board[i][j]
            #print(countbox[k], ' ')
            k+=1
    countbox = np.unique(countbox)
    for i in range(len(board)):
        for j in range(len(board)):
            for k in range(len(countbox)):
                if board[i][j] == countbox[k]:
                    board[i][j] = k


def drawboard(canvas1, board, startx=50, starty=50, cellwidth=50):
     width = 2 * startx + len(board) * cellwidth
     height = 2 * starty + len(board) * cellwidth
     canvas1.config(width=width, height=height)

     #showImage(board)
     global cnt
     cnt+=1
     for i in range(len(board)):
         for j in range(len(board)):
             index = board[i][j]
             # print(index, ' ')
             if index != -1:
                 if index == 0:
                    color = 'red'
                 elif index == 1:
                    color = 'orange'
                 elif index <= cnt:
                    tc = (255-index*10, 255-index*12, index*10)
                    color = change_rgb(tc)
                    board[i][j] == -1
                 else:
                    color = 'white'
             cellx = startx + i * 50
             celly = starty + j * 50
             canvas1.create_rectangle(cellx, celly, cellx + cellwidth, celly + cellwidth,
                                         fill=color, outline="black")
     print("cnt = ",cnt)
     canvas1.after(1000, drawboard, canvas1, board)
    #refresh_data()

def ChessBoard(tr, tc, dr, dc, size):
    global mark
    global Board
    mark += 1
    count = mark
    if size == 1:
        return
    s = size // 2
    # 覆盖左上角子棋盘
    if dr < tr+s and dc < tc+s:
        ChessBoard(tr, tc, dr, dc, s)
    else:
        Board[tr+s-1][tc+s-1] = count
        ChessBoard(tr, tc, tr+s-1, tc+s-1, s)
    # 覆盖右上角子棋盘
    if dr < tr+s and dc >= tc+s:
        ChessBoard(tr, tc+s, dr, dc, s)
    else:
        Board[tr+s-1][tc+s] = count
        ChessBoard(tr, tc+s, tr+s-1, tc+s, s)
    # 覆盖左下角子棋盘
    if dr >= tr+s and dc < tc+s:
        ChessBoard(tr+s, tc, dr, dc, s)
    else:
        Board[tr+s][tc+s-1] = count
        ChessBoard(tr+s, tc, tr+s, tc+s-1, s)
    # 覆盖右下角子棋盘
    if dr >= tr+s and dc >= tc+s:
        ChessBoard(tr+s, tc+s, dr, dc, s)
    else:
        Board[tr+s][tc+s] = count
        ChessBoard(tr+s, tc+s, tr+s, tc+s, s)


def showImage(Board):
    n=len(Board)
    for i in range(n):
        for j in range(n):
            print(Board[i][j], end=' ')
        print(' ')


def Input():
    global Board
    global mark
    mark = 0
    n=entry_board_size.get()
    x=entry_board_x.get()
    y=entry_board_y.get()



    n=2**int(n)
    #board = np.zeros(shape=[n, n], dtype=int)

    Board = [[-1 for x in range(n)] for y in range(n)]
    #showImage(Board)
    ChessBoard(0, 0, int(x), int(y), n)
    countboard(Board)

    window_chessboard = tk.Toplevel(window)
    window_chessboard.title('Chessboard')

    canvas1 = tk.Canvas(window_chessboard, bg="white")
    canvas1.pack()
    #button = tk.Button(window_chessboard, text="Next", font=('Arial', 15), command = drawboard(canvas1, Board))
    #button.pack()
    drawboard(canvas1, Board)
    showImage(Board)
    #count(Board)

window = tk.Tk()
window.title('棋盘覆盖图形化界面')
window.geometry('800x400')
tk.Label(window, text = 'ChessBoard', font=('Segoe UI Black',25)).place(x=300,y=50)
tk.Label(window, text = "请输入棋盘规模：",font=('Arial',15)).place(x=70, y=150)
var_board_size = tk.StringVar()
entry_board_size = tk.Entry(window, textvariable=var_board_size, font=('Arial',15))
entry_board_size.place(x=220, y=150)
tk.Label(window, text = "请输入特殊方格位置：", font=('Arial',15)).place(x=70,y=200)
tk.Label(window, text = "横坐标x:", font=('Arial',15)).place(x=150,y=250)
var_board_x = tk.StringVar()
entry_board_x = tk.Entry(window, textvariable=var_board_x, font=('Arial',15))
entry_board_x.place(x=230, y=250)
tk.Label(window, text = "纵坐标y:", font=('Arial',15)).place(x=450,y=250)
var_board_y = tk.StringVar()
entry_board_y = tk.Entry(window, textvariable=var_board_y, font=('Arial',15))
entry_board_y.place(x=530, y=250)
btn = tk.Button(window, text = "Run", font=('Arial',15),command = Input)
btn.place(x=350,y=300)

window.mainloop()
