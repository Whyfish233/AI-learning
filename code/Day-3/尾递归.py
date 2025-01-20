def factorial(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial(n - 1, acc * n)  # 尾递归调用

# 测试
print(factorial(1000))  # 会导致栈溢出
