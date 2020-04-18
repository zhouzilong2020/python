from MLR import MLR, loadtxt

def main():
    data = loadtxt(r'/Users/zhouzilong/Desktop/python/modling /lecture6/data.txt')
    mlr = MLR(data[ : , 0], data[ : , 1], intersect = True)
    A = mlr.getCoef()
    print(A)
    print(mlr.predict([1,2,3,4,5]))

if __name__ == "__main__":
    main()

# 计算结果：
# [0.52690106 2.19422824]
# 预测结果
# [[ 2.72112931  4.91535755  7.10958579  9.30381404 11.49804228]]