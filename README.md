# ChessBoard
棋盘覆盖算法实现（图形化界面）
## 棋盘覆盖问题（Python实现）

2020/9/27 18:28:30

### 问题描述

- 棋盘覆盖问题
  2^k x 2^k个方格；有一个方格与其他方格不同，则该方格为特殊方格；
  用L型骨牌覆盖棋盘上除了特殊方格以外的所有方格；**分治策略**

### 图形化界面

- 参考文档

  - [Tkinter库实现棋盘覆盖界面](https://download.csdn.net/download/kevinoop/10323229)

### 实验中遇到的问题与解决方案

1. 发生错误 TypeError: list indices must be integers or slices, not float
   - **出错代码**
     - ```s = size/2```
   - **解决方案**
   - 要是用//而非/，代码如下
     - ```s = size//2```
2. tkinter 绘制表格
   - **解决方案**
   - 使用canvas画布
3. 无法依次跳出L型骨牌
   - 之前想过设置一个button（按钮），每次点击按钮，则会跳出下一步骤，后来发现在弹出窗口中无法传参，设置的计数器cnt一直无法传入函数
   - **解决方案**
   - 转换了一下思路，不一定要按一下按钮再出现，可以设置定时刷新，让一个个L型骨牌弹出
   - 使用after（）函数
   - ```canvas1.after(1000, drawboard, canvas1, board)```
   - 每1000毫秒调用一次drawboard()函数（个人设置的函数），传参画布canvas1和二维数组board
4. tkinter只有十六进制，没有rgb
   - **解决方案**
   - 设置一个函数将rgb格式调整成十六进制
   - ```return "#%02x%02x%02x" % rgb```  
