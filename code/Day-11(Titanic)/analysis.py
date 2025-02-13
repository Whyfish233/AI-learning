# 忽略警告提示
import warnings
warnings.filterwarnings('ignore')

#导入处理数据包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 500)     #3个代码是为了显示更多行、更多列，并且在更宽的范围
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
#导入数据
#训练数据集
train = pd.read_csv(r'D:\a为什么捉妖\python\寒假训练营\learning\code\Day-11(Titanic)\data\train.csv')
#获取数据类型列的描述统计信息
print(train.describe())
n = train['Survived'].value_counts()
train['Survived'].value_counts()

