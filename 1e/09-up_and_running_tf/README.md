In [1]: # %load xxy_y_2.py
   ...: import tensorflow as tf
   ...:
   ...: x = tf.Variable(3, name='x')
   ...: y = tf.Variable(4, name='y')
   ...: f = x*x*y + y + 2
WARNING:tensorflow:From /home/leif/.virtualenvs/homl-1e/lib64/python3.6/site-packages/tensorflow/python/framework/op_def_library.py:263: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a future version.
Instructions for updating:
Colocations handled automatically by placer.

In [2]: sess = tf.Session()
2021-01-11 15:19:34.388106: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2021-01-11 15:19:34.412877: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 1999965000 Hz
2021-01-11 15:19:34.414024: I tensorflow/compiler/xla/service/service.cc:150] XLA service 0x55636e7c01b0 executing computations on platform Host. Devices:
2021-01-11 15:19:34.414094: I tensorflow/compiler/xla/service/service.cc:158]   StreamExecutor device (0): <undefined>, <undefined>

In [3]: tf.get_default_session()

In [4]: sess is tf.get_default_session()
Out[4]: False

In [5]: sess1 =  tf.get_default_session()

In [6]: id(sess1)
Out[6]: 139644298092880

In [7]: id(sess)
Out[7]: 139643555425808

In [8]:
Do you really want to exit ([y]/n)? y
(homl-1e) ~/.../homl/1e/09-up_and_running_tf ❯❯❯ ls
h
