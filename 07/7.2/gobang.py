# -*- coding: utf-8 -*-
# @Time : 2019/6/23 18:43
# @Author : wangmengmeng
# 定义棋盘的大小
BOARD_SIZE = 15
# 定义一个二维列表来充当棋盘
board = []
def initBoard() :
    # 把每个元素赋为"╋"，用于在控制台画出棋盘
    for i in range(BOARD_SIZE) :
        row = ["╋"] * BOARD_SIZE
        board.append(row)
# 在控制台输出棋盘的方法
def printBoard() :
    # 打印每个列表元素
    for i in range(BOARD_SIZE) :
        for j in range(BOARD_SIZE) :
            # 打印列表元素后不换行
            print(board[i][j], end="")
        # 每打印完一行列表元素后输出一个换行符
        print()
initBoard()
printBoard()
input_str = input("请输入您下棋的坐标，应以x，y的格式：\n")
while input_str != None:
    try:
        x_str,y_str = input_str.split(sep=',')
        if board[int(x_str)-1][int(y_str)-1] != '+':
            continue
        board[int(y_str) - 1][int(x_str) - 1] = "●"
    except Exception:
        inputStr = input("您输入的坐标不合法，请重新输入，下棋坐标应以x,y的格式\n")
        continue
    printBoard()
    input_str = input("请输入您下棋的坐标，应以x,y的格式：\n")

