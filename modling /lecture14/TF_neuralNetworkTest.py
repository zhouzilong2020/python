from PIL import Image
import numpy as np
from ImageDigit import ImageDigit
img=Image.open(r"E:\22\cong_digit.jpg")
imageToDigit=ImageDigit(img)
imageToDigit.histShow()  # 先显示直方图
thr=int(input('请输入背景阈值:'))
imageToDigit.convert_to_bw(thr) # 去掉背景
digits=imageToDigit.split()  # 切割小数字
imageToDigit.to_32_32()   #  标准化小数字
XX,yy=imageToDigit.featureExtract()  # 提取特征
    
from TF_neuralNetwork import TF_neuralNetwork
from sklearn.model_selection import train_test_split 
trX, teX, trY, teY = train_test_split(XX, yy, test_size=.1)  
tfnn=TF_neuralNetwork(256,20,10,100)
tfnn.fit(trX,trY)
ans=tfnn.predict(teX)
print(ans)
print(np.argmax(teY, axis=1))
