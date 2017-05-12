# 创建棒球运动员的身高列表 baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]
# 导入numpy包
import numpy as np

# 用列表baseball创建numpy数组：np_baseball
np_bb = np.array(baseball)
# 打印np_baseball的数据类型
type(np_bb)
# 将以厘米为单位的身高转换成以米为单位
np_bb / 100
# 找出高于2米的运动员身高数据
np_bb[np_bb > 2]
# 打印输出最后一个棒球运动员的身高
np_bb[-1]
# 打印输出最后两个运动员的身高
np_bb[-2:]
