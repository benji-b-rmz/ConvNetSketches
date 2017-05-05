# Benjamin Ramirez
# May 4 2017
# Modifying TensorFlow's code from 'A Guide to TF Layers: Building a Convolutional Neural Network'
# found here: https://www.tensorflow.org/tutorials/layers

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf

from tensorflow.contrib import learn
from tensorflow.contrib.learn.python.learn.estimators import model_fn as model_fn_lib

