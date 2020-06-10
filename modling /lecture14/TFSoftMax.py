import numpy as np
# 用于分类，类模式必须是正交编码
import tensorflow as tf
class TFSoftMax:
    def __init__(self,batch_size,maxIter):
        self.batch_size=batch_size
        self.maxIter=maxIter
    def fit(self,XX,yy):
        batch_size = self.batch_size # 每次修正模型使用的样本个数
        x = tf.placeholder(tf.float32, [None, XX.shape[1]])  # 构造网络拓扑，24个输入节点
        y = tf.placeholder(tf.float32, [None, yy.shape[1]])  # 2个输出节点
        # 模型权重
        W = tf.Variable(tf.zeros([XX.shape[1], yy.shape[1]]),name='w')
        b = tf.Variable(tf.zeros([yy.shape[1]]),name='b')
        # 用softmax构建逻辑回归模型
        pred = tf.nn.softmax(tf.matmul(x, W) + b)
        self.x=x
        self.y=y
        self.W=W
        self.b=b
        self.pred=pred
        
        # 损失函数(交叉熵)
        cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred), axis=1))
        # 低度下降
        optimizer = tf.train.GradientDescentOptimizer(0.01).minimize(cost)
        init = tf.global_variables_initializer()
        sess=tf.Session()
        sess.run(init)
        total_batch = len(XX)//batch_size
        for epoch in range(self.maxIter):
            avg_cost = 0.
            for i in range(total_batch):
                batch_xs=XX[i*batch_size:(i+1)*batch_size]
                batch_ys=yy[i*batch_size:(i+1)*batch_size]
                sess.run(optimizer, {x: batch_xs,y: batch_ys})
                #计算损失平均值
                avg_cost += sess.run(cost,{x: batch_xs,y: batch_ys}) / total_batch
            if (epoch+1) % 5 == 0:
                print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(avg_cost))
        self.sess=sess

    def predict(self,XX):
        sess=self.sess
        x=self.x

        W=self.W
        b=self.b
        pred=self.pred       
        # 用softmax构建逻辑回归模型
        pred = tf.nn.softmax(tf.matmul(x, W) + b)
        with sess:
            ans=sess.run(pred, feed_dict={x: XX})
            ans=np.array(ans)
            maxIndex=np.argmax(ans,axis=1)
            for i,index in enumerate(maxIndex):
                ans[i][index]=1
            ans[ans!=1]=0
            return ans
        

