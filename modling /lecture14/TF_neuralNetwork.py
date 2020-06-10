import numpy as np
import tensorflow as tf
class TF_neuralNetwork:
    def __init__(self,inputNode,hiddenNode,outputNode,maxIter):
        self.inputNode=inputNode
        self.hiddenNode=hiddenNode
        self.outputNode=outputNode
        self.maxIter=maxIter
        
    def init_weights(self,shape):
        return tf.Variable(tf.random_normal(shape, stddev=0.01))
    def model(self,X, w_h, w_o):
        h = tf.nn.sigmoid(tf.matmul(X, w_h))
        return tf.matmul(h, w_o)
    def fit(self,XX,yy):
        X = tf.placeholder("float", [None, self.inputNode])
    
        Y = tf.placeholder("float", [None, self.outputNode])
        w_h = self.init_weights([self.inputNode, self.hiddenNode]) # 隐含层100个节点
        w_o = self.init_weights([self.hiddenNode, self.outputNode])
        py_x = self.model(X, w_h, w_o)
        cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=py_x, labels=Y)) # 计算费用
        train_op = tf.train.GradientDescentOptimizer(0.05).minimize(cost) # 创建优化器
        predict_op = tf.argmax(py_x, 1)
        sess=tf.Session()
        init = tf.global_variables_initializer()
        sess.run(init)
    
        for i in range(self.maxIter):
            for start, end in zip(range(0, len(XX), 5), range(5, len(XX)+1, 5)):
                sess.run(train_op, feed_dict={X: XX[start:end], Y: yy[start:end]})
        self.sess=sess
        self.predict_op=predict_op
        self.X=X
    def predict(self,Xnew):
        sess=self.sess
        predict_op=self.predict_op
        X=self.X
        with sess:
            ans=sess.run(predict_op, feed_dict={X: Xnew})
        return ans
