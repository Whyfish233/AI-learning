# 波士顿房价数据集（校正版）

## 简介

本仓库提供了一个校正版的波士顿房价数据集（Boston Housing Dataset），文件格式为CSV。该数据集是机器学习和数据分析领域中常用的经典数据集之一，适用于回归问题的分析和模型验证。

## 数据集说明

波士顿房价数据集包含506个样本，每个样本有14个属性。这些属性包括：

- CRIM：城镇人均犯罪率
- ZN：占地面积超过25,000平方英尺的住宅用地比例
- INDUS：城镇非零售业务地区的比例
- CHAS：查尔斯河虚拟变量（如果临河为1，否则为0）
- NOX：一氧化氮浓度（每千万分之一）
- RM：住宅平均房间数
- AGE：1940年以前建成的自住单位比例
- DIS：到波士顿五个就业中心的加权距离
- RAD：径向公路的可达性指数
- TAX：每10,000美元的全额物业税率
- PTRATIO：城镇师生比例
- B：1000(Bk - 0.63)^2，其中Bk是城镇黑人比例
- LSTAT：人口中地位较低人群的百分比
- MEDV：自住房屋的中位数价值（单位：千美元）

## 数据集来源

该数据集最初由Harrison和Rubinfeld于1978年收集，并在许多机器学习教材和研究中被广泛使用。本仓库提供的版本经过校正，确保数据完整无缺失。

## 使用方法

1. 下载数据集文件 `波士顿房价数据集.csv`。
2. 使用Python或其他数据分析工具加载CSV文件进行分析。

```python
import pandas as pd

data = pd.read_csv("波士顿房价数据集.csv")
print(data.head())
```

## 注意事项

- 该数据集仅供学习和研究使用，不得用于商业用途。
- 数据集中的某些属性可能存在历史局限性，使用时请注意。

## 贡献

如果您发现数据集存在问题或有改进建议，欢迎提交Issue或Pull Request。

## 许可证

本数据集遵循CC 4.0 BY-SA版权协议，转载请附上原文出处声明。