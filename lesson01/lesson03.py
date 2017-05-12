# 导入 numpy 基础包
import numpy as np

# 创建二维列表 baseball, 第一列是身高，第二列是体重
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# 用二维列表baseball创建二维数组 np_baseball
np_baseball = np.array(baseball)

# 打印输出 np_baseball 的类型
type(np_baseball)

# 打印输出 np_baseball的shape属性
print(np_baseball.shape)

# 打印输出第3行的数据
print(np_baseball[2])

# 打印输出第二列的数据
print(np_baseball[:, 1])

# 打印输出第4名运动员的身高
print(np_baseball[3][0])
