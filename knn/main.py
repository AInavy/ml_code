#! -*- coding=utf-8 -*-
import os, sys
import matplotlib
from numpy import *
import matplotlib.pyplot as plt

import KNN

if __name__ == "__main__":
    print "1--"
    group, labels = KNN.createDataSet()
    print group
    # print type(group)
    print labels

    print KNN.classify0([0,0], group, labels, 3)

    print "2--"
    datingDataMat, datingLabels = KNN.file2matrix('./datingTestSet2.txt')
    # print datingDataMat
    # print datingLabels
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2],
               15.0 * array(datingLabels), 15.0 * array(datingLabels))
    plt.show()

    normMat, ranges, minVals = KNN.autoNorm(datingDataMat)
    print minVals, ranges
    print normMat

