zero_tsr=tf.zero([1,2])
ones_tsr=tf.ones([1,2])
filled_tsr=tf.fill([1,2],42)
constant_tsr=tf.constant([1,2,3])
constant_2=tf.constant(42,[1,2])

2.形状相似的张量
zeros_similiar=tf.zeros_like(constant_tsr)
ones_similiar=tf.ones_like(constant_tsr)

3.序列张量
np.linspace()
np/tf.range()
4.随机张量
tf.random_uniform([row_dim,col_dim],minval,maxval)
tf.random_normal([row_dim,col_dim],mean,stddev)
tf.truncated_normal([row_dim,col_dim],mean,stddev)
tf.random_shuffle(input_tensor)
rf.random_crop(input_tensor,cropsize)

#创建变量并初始化
my_var=tf.Variable(tf.zeros([2,3]))#封装向量，可以用numpy，Python列表，tensor
sess=tf.Session()
initialize_op=tf.global_variables_initializer()
sess.run(initialize_op)

#identity操作返回占位符传入的数据本身
sess=tf.Session()
x=tf.placeholder(tf.float32,shape=[2,2])
y=tf.identity(x)
x_vals=np.random.ran(2,2)
sess.run(y,feed_dict{x:x_vals})
#Note that sess.run(x,feed_dict={x:x_vals}) will result in a self-referencing error
#占位符上必须执行至少一个操作

#global_variables_initializer()一次性初始化所有变量
#但是，若要基于已经初始化的变量进行初始化，则必选按序初始化

