def trim(s):
    # 去除开头的空格
    start = 0
    while start < len(s) and s[start] == ' ':
        start += 1

    # 去除结尾的空格
    end = len(s)
    while end > start and s[end - 1] == ' ':
        end -= 1

    # 返回去除空格后的字符串
    return s[start:end]
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
