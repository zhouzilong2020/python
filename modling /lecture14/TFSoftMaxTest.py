import numpy as np
from TFSoftMax import TFSoftMax
XX = np.loadtxt(r"E:\teach\python\data\wheat_train_PCA_X.txt")
yy=np.loadtxt(r"E:\teach\python\data\wheat_train_PCA_Y.txt")
#yy1=np.r_[yy,2]  # 原来是-1，1,现在加一个2, 称为三类模式，且2是最大模式
from sklearn import preprocessing
scaler = preprocessing.StandardScaler().fit(XX)
XX=scaler.fit_transform(XX)
yylabel=[]
for i in range(len(yy)):
    temp=2*[0]
    if yy[i]==1:
        temp[0]=1
    else:
        temp[1]=1
    yylabel.append(temp)
yy=np.array(yylabel)  # 正交编码
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(XX, yy, test_size=.1)

tfSoftMax=TFSoftMax(5,25)
tfSoftMax.fit(X_train,y_train)
ans=tfSoftMax.predict(X_test)
print(ans)
print(y_test)
yhat=np.argmax(ans,axis=1)
print(yhat)
yTrue=np.argmax(y_test,axis=1)
print(yTrue)
err=np.abs(yhat-yTrue).sum()
print(err/len(yhat)*100)
    
