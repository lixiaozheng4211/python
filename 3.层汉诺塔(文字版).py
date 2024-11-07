sum=0
def hanoi(n, x, y, z):
    if n > 0:
        # 将n - 1个盘子从源柱子移动到辅助柱子
        hanoi(n - 1, x, z, y)
        print(f"Move disk {n} from {x} to {z}")
        sum=+1
        # 将n - 1个盘子从辅助柱子移动到目标柱子
        hanoi(n - 1, y, x, z)
    return sum
    elif n==1 :
        print("Move disk 1 Tower1 from  to Tower3 ")
        sum=1
        return sum
# 测试，这里以3个盘子为例
n=int(input('please input n (int)\t'))
hanoi(int(n),'Tower1', 'Tower2', 'Tower3')
print(f'移动{n}个盘子需要{sum)}个步骤')