identity_mat=tf.diag([1.0,1.0,1.0])#用一维数组创建对角矩阵
+/-
tf.matmul(B,identity_mat)
tf.transpose(B)
#再次运行sess.run(B),重新初始化随机变量会得到不同的值

#矩阵的行列式
print(sess.run(tf.matrix_determinant(B))
-38.0
#矩阵的逆矩阵
print(sess.run(tf.matrix_inverse(B)))

#矩阵的特征值和特征向量
print(sess.run(tf.self_adjoint_eig(D)))
(array([-10.65907521,  -0.22750691,   2.88658212]), 
array([[ 0.21749542,  0.63250104, -0.74339638],
       [ 0.84526515,  0.2587998 ,  0.46749277],
       [-0.4880805 ,  0.73004459,  0.47834331]]))
