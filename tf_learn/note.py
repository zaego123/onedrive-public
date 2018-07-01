zero_tsr=tf.zero([1,2])
ones_tsr=tf.ones([1,2])
filled_tsr=tf.fill([1,2],42)
constant_tsr=tf.constant([1,2,3])
constant_2=tf.constant(42,[1,2])

2.形状相似的张量
zeros_similiar=tf.zeros_like(constant_tsr)
ones_similiar=tf.ones_like(constant_tsr)

3.序列张量



#创建变量并初始化
my_var=tf.Variable(tf.zeros([2,3]))
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