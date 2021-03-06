import numpy as np
import tensorflow as tf


def jaccard_coef(y_true, y_pred, mean=True):
    # __author__ = Vladimir Iglovikov

    epsilon = 1e-12
    # y_pred_pos = tf.round(y_pred)
    y_pred_pos = tf.floor(y_pred+0.5) # bug in tensroflow - no gradients for `tf.round`

    intersection = tf.reduce_sum(y_true * y_pred_pos, axis=[0, 1, 2])
    sum_ = tf.reduce_sum(y_true + y_pred, axis=[0, 1, 2])
    jac = (intersection + epsilon) / (sum_ - intersection + epsilon)

    if mean:
        jac = tf.reduce_mean(jac)

    return jac
