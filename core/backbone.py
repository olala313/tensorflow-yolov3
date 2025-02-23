#! /usr/bin/env python
# coding=utf-8
#================================================================
#   Copyright (C) 2019 * Ltd. All rights reserved.
#
#   Editor      : VIM
#   File name   : backbone.py
#   Author      : YunYang1994
#   Created date: 2019-02-17 11:03:35
#   Description :
#
#================================================================

import core.common as common
import tensorflow as tf


def darknet53(input_data, trainable):

    with tf.variable_scope('darknet'):

        input_data = common.convolutional(input_data, filters_shape=(3, 3,  3,  32), trainable=trainable, name='conv0')
        input_data = common.convolutional(input_data, filters_shape=(3, 3, 32,  64),
                                          trainable=trainable, name='conv1', downsample=True)

        for i in range(1):
            input_data = common.residual_block(input_data,  64,  32, 64, trainable=trainable, name='residual%d' %(i+0))

        input_data = common.convolutional(input_data, filters_shape=(3, 3,  64, 128),
                                          trainable=trainable, name='conv4', downsample=True)

        for i in range(2):
            input_data = common.residual_block(input_data, 128,  64, 128, trainable=trainable, name='residual%d' %(i+1))

        input_data = common.convolutional(input_data, filters_shape=(3, 3, 128, 256),
                                          trainable=trainable, name='conv9', downsample=True)

        for i in range(8):
            input_data = common.residual_block(input_data, 256, 128, 256, trainable=trainable, name='residual%d' %(i+3))

        route_1 = input_data
        input_data = common.convolutional(input_data, filters_shape=(3, 3, 256, 512),
                                          trainable=trainable, name='conv26', downsample=True)

        for i in range(8):
            input_data = common.residual_block(input_data, 512, 256, 512, trainable=trainable, name='residual%d' %(i+11))

        route_2 = input_data
        input_data = common.convolutional(input_data, filters_shape=(3, 3, 512, 1024),
                                          trainable=trainable, name='conv43', downsample=True)

        for i in range(4):
            input_data = common.residual_block(input_data, 1024, 512, 1024, trainable=trainable, name='residual%d' %(i+19))

        return route_1, route_2, input_data

def darknet19(input_data, trainable):

    with tf.variable_scope('darknet'):

        input_data = common.convolutional(input_data, filters_shape=(3, 3, 3, 16), trainable=self.trainable,name='conv0')
        input_data = common.max_pooling_2d(input_data,ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], data_format=self.data_format,name='max1')
        input_data = common.convolutional(input_data, filters_shape=(3, 3, 16, 32), trainable=self.trainable,name='conv2')
        input_data = common.max_pooling_2d(input_data, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1],data_format=self.data_format,name='max3')
        input_data = common.convolutional(input_data, filters_shape=(3, 3, 32, 64), trainable=self.trainable,name='conv4')
        input_data = common.max_pooling_2d(input_data, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1],data_format=self.data_format,name='max5')
        input_data = common.convolutional(input_data, filters_shape=(3, 3, 64, 128), trainable=self.trainable,name='conv6')
        input_data = common.max_pooling_2d(input_data, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1],data_format=self.data_format,name='max7')

        input_data = common.convolutional(input_data, filters_shape=(3, 3, 128, 256), trainable=self.trainable,name='conv8')
        route_8_layer = input_data
        input_data = common.max_pooling_2d(input_data, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1],data_format=self.data_format,name='max9')

        input_data = common.convolutional(input_data, filters_shape=(3, 3, 256, 512), trainable=self.trainable,name='conv10')
        input_data = common.max_pooling_2d(input_data, ksize=[1, 2, 2, 1], strides=[1, 1, 1, 1],data_format=self.data_format,name='max11')

        input_data = common.convolutional(input_data, filters_shape=(3, 3, 512, 1024), trainable=self.trainable,name='conv12')
        input_data = common.convolutional(input_data, filters_shape=(1, 1, 1024, 256), trainable=self.trainable,name='conv13')
        route_13_layer = input_data

        return route_8_layer, route_13_layer, input_data




