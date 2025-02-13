# 忽略警告提示，自己做的时候没有写这两行代码后期运行的时候果然出现警告提示，还好只是提示程序还可以正常运行。
import warnings                                         ### 理解数据！！！
warnings.filterwarnings('ignore')

# 导入处理数据包
import numpy as np
import pandas as pd
pd.set_option('display.max_rows', 500)     #3个代码是为了显示更多行、更多列，并且在更宽的范围
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
import os
# 导入数据
#训练数据集
train=pd.read_csv(r'D:\a为什么捉妖\python\寒假训练营\learning\code\Day-11(Titanic)\data\train.csv')
#测试数据集
test=pd.read_csv(r'D:\a为什么捉妖\python\寒假训练营\learning\code\Day-11(Titanic)\data\test.csv')

print('训练数据集:{}测试数据集:{}'.format(train.shape,test.shape))

rowNum_train=train.shape[0]
rowNum_test=test.shape[0]

print('kaggle训练数据集有多少行数据：',rowNum_train,
     ',kaggle测试数据集有多少行数据：',rowNum_test,)

full = train.append(test,ignore_index=True)
print('合并后的数据集：{}'.format(full.shape))

# 查看数据
print(full.head())#要用print才能输出
#获取数据类型列的描述统计信息，只能查看数据类型的描述统计信息
print(full.describe())#与上述同理
'''
我们发现数据总共有1309行。
其中数据类型列：年龄（Age）、船舱号（Cabin）里面有缺失数据：
1）年龄（Age）里面数据总数是1046条，缺失了1309-1046=263，缺失率263/1309=20%
2）船票价格（Fare）里面数据总数是1308条，缺失了1条数据

字符串列：
1）登船港口（Embarked）里面数据总数是1307，只缺失了2条数据，缺失比较少
2）船舱号（Cabin）里面数据总数是295，缺失了1309-295=1014，缺失率=1014/1309=77.5%，缺失比较大
这为我们下一步数据清洗指明了方向，只有知道哪些数据缺失数据，我们才能有针对性的处理。
'''
# 对比缺失值处理前后的info                                  ### 数据清洗！！！
# 3.数据清洗
# (1) 数据预处理
# 缺失值处理
# 在前面，理解数据阶段，我们发现数据总共有1309行。 其中数据类型列：年龄（Age）、船舱号（Cabin）里面有缺失数据。 字符串列：登船港口（Embarked）、船舱号（Cabin）里面有缺失数据。
# 这为我们下一步数据清洗指明了方向，只有知道哪些数据缺失数据，我们才能有针对性的处理。
# 很多机器学习算法为了训练模型，要求所传入的特征中不能有空值。
# 1.如果是数值类型，用平均值取代（如本例中的Age，Fare）
# 2.如果是分类数据，用最常见的类别取代（如本例中的登船港口（Embarked）,船舱号（Cabin））
# 3.使用模型预测缺失值，例如：K-NN
print('********************处理前********************')
full.info()
#处理年龄（Age）缺失值
full['Age'] = full['Age'].fillna(full['Age'].mean())
#处理船票价格（Fare）缺失值
full['Fare'] = full['Fare'].fillna(full['Fare'].mean())
print('********************处理后********************')
full.info()
# 检查数据处理是否正常
print(full.head())
'''
总数据是1309
字符串列：
1）登船港口（Embarked）里面数据总数是1307，只缺失了2条数据，缺失比较少
2）船舱号（Cabin）里面数据总数是295，缺失了1309-295=1014，缺失率=1014/1309=77.5%，缺失比较大
'''
#登船港口（Embarked）：查看里面数据长啥样
'''
出发地点：S=英国南安普顿Southampton
途径地点1：C=法国 瑟堡市Cherbourg
途径地点2：Q=爱尔兰 昆士敦Queenstown
'''
print("\n")
print(full['Embarked'].head(10))
'''
分类变量Embarked，看下最常见的类别，用其填充
'''
print(full['Embarked'].value_counts())
'''
从结果来看，S类别最常见。我们将缺失值填充为最频繁出现的值：
S=英国南安普顿Southampton
'''
full['Embarked'] = full['Embarked'].fillna( 'S' )
#船舱号（Cabin）：查看里面数据长啥样
print(full['Cabin'].head(10))
#缺失数据比较多，船舱号（Cabin）缺失值填充为U，表示未知（Uknow）
full['Cabin'] = full['Cabin'].fillna( 'U' )
#检查数据处理是否正常
print(full.head())
#查看最终缺失值处理情况，记住生存情况（Survived）这里一列是我们的标签，用来做机器学习预测的，不需要处理这一列
full.info()
# (2) 特征提取
# 数据分类
# 查看数据类型，分为3种数据类型。并对类别数据处理：用数值代替类别，并进行One-hot编码
'''
1.数值类型：
乘客编号（PassengerId），年龄（Age），船票价格（Fare），同代直系亲属人数（SibSp），不同代直系亲属人数（Parch）
2.时间序列：无
3.分类数据：
1）有直接类别的
乘客性别（Sex）：男性male，女性female
登船港口（Embarked）：出发地点S=英国南安普顿Southampton，途径地点1：C=法国 瑟堡市Cherbourg，出发地点2：Q=爱尔兰 昆士敦Queenstown
客舱等级（Pclass）：1=1等舱，2=2等舱，3=3等舱
2）字符串类型：可能从这里面提取出特征来，也归到分类数据中
乘客姓名（Name）
客舱号（Cabin）
船票编号（Ticket）
'''
#查看性别数据这一列
print(full['Sex'].head())
'''
利用pandas的.map()将性别的值映射为数值
男（male）对应数值1，女（female）对应数值0
'''
sex_mapDict={'male':1,
            'female':0}
#map函数：对Series每个数据应用自定义的函数计算
full['Sex']=full['Sex'].map(sex_mapDict)
print(full.head())
'''
登船港口(Embarked)的值是：
出发地点：S=英国南安普顿Southampton
途径地点1：C=法国 瑟堡市Cherbourg
途径地点2：Q=爱尔兰 昆士敦Queenstown
'''
#查看该类数据内容
print(full['Embarked'].head())
# 存放提取后的特征
embarkedDf = pd.DataFrame()
'''
使用get_dummies进行one-hot编码，产生虚拟变量（dummy variables），列名前缀是Embarked,prefix用来设置前缀。
'''
embarkedDf = pd.get_dummies(full['Embarked'],prefix='Embarked')
print(embarkedDf.head())
#添加one-hot编码产生的虚拟变量（dummy variables）到泰坦尼克号数据集full替换之前的'Embarked'列
full = pd.concat([full,embarkedDf],axis=1)
'''
因为已经使用登船港口(Embarked)进行了one-hot编码产生了它的虚拟变量（dummy variables）
所以这里把登船港口(Embarked)删掉,用.drop()
'''
full.drop('Embarked',axis=1,inplace=True)
print(full.head())
'''
客舱等级(Pclass):
1=1等舱，2=2等舱，3=3等舱
'''
#存放提取后的特征 方法同上
pclassDf = pd.DataFrame()
#使用get_dummies进行one-hot编码，列名前缀是Pclass
pclassDf = pd.get_dummies(full['Pclass'],prefix='Pclass')
print(pclassDf.head())
#添加one-hot编码产生的虚拟变量（dummy variables）到泰坦尼克号数据集full,替换原有的'Pclass'列
full = pd.concat([full,pclassDf],axis=1)
full.drop('Pclass',axis=1,inplace=True)
print(full.head())
# b.分类数据：字符串类型
# 字符串类型：可能从这里面提取出特征来，也归到分类数据中，这里数据有：
# 1.乘客姓名（Name） 2.客舱号（Cabin） 3.船票编号（Ticket）
# 从姓名中提取头衔
'''
查看姓名这一列长啥样
注意到在乘客名字（Name）中，有一个非常显著的特点：
乘客头衔每个名字当中都包含了具体的称谓或者说是头衔，将这部分信息提取出来后可以作为非常有用一个新变量，可以帮助我们进行预测。
例如：
Braund, Mr. Owen Harris
Heikkinen, Miss. Laina
Oliva y Ocana, Dona. Fermina
Peter, Master. Michael J
'''
print(full[ 'Name' ].head())
#练习从字符串中提取头衔，例如Mr
#split用于字符串分割，返回一个列表
#我们看到姓名中'Braund, Mr. Owen Harris'，逗号前面的是“名”，逗号后面是‘头衔. 姓’
'''
split用于字符串按分隔符分割，返回一个列表。这里按逗号分隔字符串
也就是字符串'Braund, Mr. Owen Harris'被按分隔符,'拆分成两部分[Braund,Mr. Owen Harris]
你可以把返回的列表打印出来瞧瞧，这里获取到列表中元素序号为1的元素，也就是获取到头衔所在的那部分，即Mr. Owen Harris这部分
'''
name1='Braund, Mr. Owen Harris'
str1=name1.split( ',' )[1]
print(str1)
'''
继续对字符串Mr. Owen Harris按分隔符'.'拆分，得到这样一个列表[Mr, Owen Harris]
这里获取到列表中元素序号为0的元素，也就是获取到头衔所在的那部分Mr
'''
str2=str1.split( '.' )[0]
print(str2)
#strip() 方法用于移除字符串头尾指定的字符（默认为空格）
str3=str2.strip()
'''
定义函数：从姓名中获取头衔
'''
def getTitle(name):
    str1 = name.split(',')[1]
    str2 = str1.split('.')[0]
    str3 = str2.strip()
    return str3
#存放提取后的特征
titleDf = pd.DataFrame()
#map函数：对Series每个数据应用自定义的函数计算
titleDf['Title'] = full['Name'].map(getTitle)
print(titleDf.head())
'''
定义以下几种头衔类别：
Officer政府官员
Royalty王室（皇室）
Mr男士
Mrs已婚妇女
Miss年轻未婚女子
Master有技能的人/教师
'''
#姓名中头衔字符串与定义头衔类别的映射关系
title_mapDict = {
                    "Capt":       "Officer",
                    "Col":        "Officer",
                    "Major":      "Officer",
                    "Jonkheer":   "Royalty",
                    "Don":        "Royalty",
                    "Sir" :       "Royalty",
                    "Dr":         "Officer",
                    "Rev":        "Officer",
                    "the Countess":"Royalty",
                    "Dona":       "Royalty",
                    "Mme":        "Mrs",
                    "Mlle":       "Miss",
                    "Ms":         "Mrs",
                    "Mr" :        "Mr",
                    "Mrs" :       "Mrs",
                    "Miss" :      "Miss",
                    "Master" :    "Master",
                    "Lady" :      "Royalty"
                    }
#map函数：对Series每个数据应用自定义的函数计算
titleDf['Title'] = titleDf['Title'].map(title_mapDict)
#使用get_dummies进行one-hot编码
titleDf = pd.get_dummies(titleDf['Title'])
print(titleDf.head())
#添加one-hot编码产生的虚拟变量（dummy variables）到泰坦尼克号数据集full替换'Name'列
full = pd.concat([full,titleDf],axis=1)
full.drop('Name',axis=1,inplace=True)
full.head()
'''
客舱号的首字母是客舱的类别
'''
# 查看客舱号的内容
print(full['Cabin'].head())
# 存放客舱号信息
cabinDf = pd.DataFrame()

'''
客场号的类别值是首字母，例如：
C85 类别映射为首字母C
'''
full['Cabin'] = full['Cabin'].map(lambda c : c[0])
# 使用get_dummies进行one-hot编码，列名前缀是Cabin
cabinDf = pd.get_dummies(full['Cabin'],prefix='Cabin')
cabinDf.head()
#添加one-hot编码产生的虚拟变量（dummy variables）到泰坦尼克号数据集full替换'Cabin'列
full = pd.concat([full,cabinDf],axis=1)
full.drop('Cabin',axis=1,inplace=True)
print(full.head())
#存放家庭信息
familyDf = pd.DataFrame()
'''
家庭人数=同代直系亲属数（Parch）+不同代直系亲属数（SibSp）+乘客自己
（因为乘客自己也是家庭成员的一个，所以这里加1）
'''
familyDf['FamilySize'] = full['Parch']+full['SibSp']+1
'''
家庭类别：
小家庭Family_Single：家庭人数=1
中等家庭Family_Small: 2<=家庭人数<=4
大家庭Family_Large: 家庭人数>=5
'''
#if 条件为真的时候返回if前面内容，否则返回0
familyDf['Family_Single'] = familyDf['FamilySize'].map(lambda s : 1 if s==1 else 0)
familyDf['Family_Small'] = familyDf['FamilySize'].map(lambda s : 1 if 1<=s<=4 else 0)
familyDf['Family_Large'] = familyDf['FamilySize'].map(lambda s : 1 if s>=5 else 0)
print(familyDf.head())
#添加one-hot编码产生的虚拟变量（dummy variables）到泰坦尼克号数据集full
full = pd.concat([full,familyDf],axis=1)
print(full.head())
# #到现在我们已经有了这么多个特征了
# full.shape
# (1309, 33)
# (3)特征选择
# 相关系数法：计算各个特征的相关系数
#相关性矩阵
corrDf = full.corr()
print(corrDf)
print(corrDf['Survived'].sort_values(ascending =False))
'''
查看各个特征与生成情况（Survived）的相关系数，
ascending=False表示按降序排列
'''
# 根据各个特征与生成情况（Survived）的相关系数大小，我们选择了这几个特征作为模型的输入：
# 头衔（前面所在的数据集titleDf）、客舱等级（pclassDf）、家庭大小（familyDf）、船票价格（Fare）、
# 船舱号（cabinDf）、登船港口（embarkedDf）、性别（Sex）
# 特征选择,头衔、客舱等级、家庭大小、船票价格、船舱号、登船港口、性别
full_X = pd.concat([titleDf,pclassDf,familyDf,full['Fare'],cabinDf,embarkedDf,full['Sex']],axis=1)
print(full_X.head())
# 4.构建模型
# 用训练数据和某个机器学习算法得到机器学习模型，用测试数据评估模型
# （1）建立训练数据集和此时数据集
'''
1）坦尼克号测试数据集因为是我们最后要提交给Kaggle的，里面没有生存情况的值，所以不能用于评估模型。
我们将Kaggle泰坦尼克号项目给我们的测试数据，叫做预测数据集（记为pred,也就是预测英文单词predict的缩写）。
也就是我们使用机器学习模型来对其生存情况就那些预测。
2）我们使用Kaggle泰坦尼克号项目给的训练数据集，做为我们的原始数据集（记为source），
从这个原始数据集中拆分出训练数据集（记为train：用于模型训练）和测试数据集（记为test：用于模型评估）。
'''
#原始数据集有891行
sourceRow=891
'''
sourceRow是我们在最开始合并数据前知道的，原始数据集有总共有891条数据
从特征集合full_X中提取原始数据集提取前891行数据时，我们要减去1，因为行号是从0开始的。
'''
# 原始数据集：特征
source_X = full_X.loc[0:sourceRow-1,:]
# 原始数据集：标签
source_y = full.loc[0:sourceRow-1,'Survived']
# 预测数据集：特征
pred_X = full_X.loc[sourceRow:,:]
'''
确保这里原始数据集取的是前891行的数据，不然后面模型会有错误
'''
#原始数据集有多少行
print('原始数据集有多少行:',source_X.shape[0])
#预测数据集大小
print('原始数据集有多少行:',pred_X.shape[0])
'''
从原始数据集（source）中拆分出训练数据集（用于模型训练train），测试数据集（用于模型评估test）
train_test_split是交叉验证中常用的函数，功能是从样本中随机的按比例选取train data和test data
train_data：所要划分的样本特征集
train_target：所要划分的样本结果
test_size：样本占比，如果是整数的话就是样本的数量
'''
from sklearn.model_selection import train_test_split

#建立模型用的训练数据集和测试数据集
train_X,test_X,train_y,test_y = train_test_split(source_X,source_y,train_size=.8)

#输出数据集大小
print ('原始数据集特征：',source_X.shape,
       '训练数据集特征：',train_X.shape ,
      '测试数据集特征：',test_X.shape)

print ('原始数据集标签：',source_y.shape,
       '训练数据集标签：',train_y.shape ,
      '测试数据集标签：',test_y.shape)
#第1步：导入算法
from sklearn.linear_model import LogisticRegression
#第2步：创建模型：逻辑回归（logisic regression）
model = LogisticRegression()
#第3步：训练模型
model.fit( train_X , train_y )
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
          intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
          penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
          verbose=0, warm_start=False)
# 分类问题，score得到的是模型的正确率
print(model.score(test_X , test_y ))
#使用机器学习模型，对预测数据集中的生存情况进行预测
pred_Y = model.predict(pred_X)
'''
生成的预测值是浮点数（0.0,1,0）
但是Kaggle要求提交的结果是整型（0,1）
所以要对数据类型进行转换
'''
pred_Y = pred_Y.astype(int)
#乘客id
passenger_id = full.loc[sourceRow:,'PassengerId']
#数据框：乘客id，预测生存情况的值
predDf = pd.DataFrame({'PassengerId':passenger_id,
                      'Survived':pred_Y})
print(predDf.shape)
print(predDf.head())
#保存结果
predDf.to_csv( r'D:\a为什么捉妖\python\寒假训练营\learning\code\Day-11(Titanic)\data\output\titanic_pred.csv' , index = False )