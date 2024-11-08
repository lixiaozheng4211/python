def hanoi(n, start='A', middle='B', end='C'):
    if n == 1:
        print(f"Move disk 1 from {start} to {end}")
        return 1
    else:
        steps1 = hanoi(n - 1, start, end, middle)
        print(f"Move disk {n} from {start} to {end}")
        steps2 = hanoi(n - 1, middle, start, end)
        return steps1 + 1 + steps2


n = int(input('请输入整数n\n'))  # 这里可以修改盘子的数量
print(f"Moving {n} disks requires {hanoi(n)} steps.")
'''
这里运用了f输入法（还是格式化输入）换一种格式化输入其实也是可以的就是format格式化输入
对于这个汉诺塔的编程其实从数学的角度讲基本没什么难度就是一个基本的用配凑法的数列求和，但
是编程不仅要实现结果的正确还有过程的可操作性，所以难度上就是实现用print打印步骤

主要数学思想：整体法将n-1个盘子看成一个整体就分成两部进行
1.将n-1个圆盘放到中间的柱子上
2.将第n个盘子放到最后一个盘子上
3.将n-1个盘子从中间的柱子上放到最后一个柱子上

从编程的角度：对于n>1的情况，函数会进行多次递归调用。在每次递归调用中，无论是
hanoi(n - 1, start, end, middle)还是hanoi(n - 1, middle, start, end)，
这些递归调用都会继续细分问题，直到达到n = 1的情况。当这些递归调用完成后（即从最底层
的n = 1情况开始回溯），每一层的hanoi函数调用都会返回一个代表移动一定数量圆盘所需步数
的值。这个值通过steps1和steps2在不同的递归层次中被正确地记录和传递。
'''