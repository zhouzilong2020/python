from sklearn.datasets import load_digits
import numpy as np
digits = load_digits()
X = digits.data    # 数字图片特征向量
y = digits.target  #  y是数字，如 0，1，2，..., 9

remove = np.zeros(64, dtype=bool)
sum_col = X.sum(axis=0).tolist()

for i, col in enumerate(sum_col):
    # 不为0保留
    if sum_col[i] != 0:
        remove[i] = True

# 老师，由于mac系统圆形，我用不了该方法过滤数据
remove_index = np.array([sum_col==0])

# 过滤
X = X[:, remove]
print(X)
