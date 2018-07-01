
import numpy as np
    
def my_func(arg):
    arg = tf.convert_to_tensor(arg)
    return tf.matmul(arg, arg) + arg
    
    # The following calls are equivalent.
value_1 = my_func(tf.constant([[1, 2], [3, 4]]))#tensor
value_2 = my_func([[1, 2], [3, 4]])#python list
value_3 = my_func(np.array([[1.0, 2], [3, 4]], dtype=np.float32))#numpy arrays
 
with tf.Session() as sess:
    result1,result2,result3=sess.run([value_1,value_2,value_3])
    print('result1 = \n%s'%(result1))
    print('result2 = \n%s'%(result2))
    print('result3 = \n%s'%(result3))
