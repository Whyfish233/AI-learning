# Day-1——Day-6 总结

### 已完成内容：

* 1.完成相关工具的安装

* 2.掌握python的基础语法，数据类型，数据结构

* 3.掌握条件控制以及循环控制，推导式，错误和异常捕获，map，lambda，filter函数

* 4.理解运用面向对象（类与实例化，类变量以及方法，私有变量和私有方法，封装，继承，多态等

	

### 仍需努力的地方

* 1.需继续对map/filter/lambda继续复习

* 2.闭包的理解如

	```python
	def count():
	    fs = []
	    for i in range(1, 4):
	        def f():
	             return i*i
	        fs.append(f)
	    return fs
	
	f1, f2, f3 = count()
	```

需理解：返回的函数引用了变量`i`，但它并非立刻执行，而是直到调用了`f()`才执行