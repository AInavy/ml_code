#! -*- coding=utf-8 -*-
from numpy import *
import operator

def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]

    # calc distance inX -> dataSet for each rows
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5

    # 将x中的元素从小到大排列，提取其对应的index(索引)
    sortedDistIndicies = distances.argsort()
    # print sortedDistIndicies
    classCount = {}

    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

    #sorted从小到大排序，返回新list, 所以这里求频率最大需要reverse
    sortedClassCount = sorted(classCount.iteritems(),
                              key=operator.itemgetter(1), reverse=True)

    for i in range(0, len(sortedClassCount)):
        print sortedClassCount[i]

    return sortedClassCount[0][0]
