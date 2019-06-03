#! -*- coding=utf-8 -*-
import os, sys
import matplotlib
from numpy import *
import matplotlib.pyplot as plt

import KNN

if __name__ == "__main__":
    # print "1--"
    # group, labels = KNN.createDataSet()
    # print group
    # # print type(group)
    # print labels
    #
    # print KNN.classify0([0,0], group, labels, 3)
    #
    # print "2--"
    # datingDataMat, datingLabels = KNN.file2matrix('./datingTestSet2.txt')
    # # print datingDataMat
    # # print datingLabels
    #
    # # show viewer
    # fig = plt.figure()
    # plt.title('knn')
    # plt.xlabel('X')
    # plt.ylabel('Y')
    #
    # ax1 = fig.add_subplot(211)
    # ax1.scatter(datingDataMat[:, 1], datingDataMat[:, 2],
    #            15.0 * array(datingLabels), 15.0 * array(datingLabels))
    #
    # ax2 = fig.add_subplot(212)
    # ax2.scatter(datingDataMat[:, 1], datingDataMat[:, 2])
    # plt.show()
    #
    # normMat, ranges, minVals = KNN.autoNorm(datingDataMat)
    # print minVals, ranges
    # print normMat

    # KNN.datingClassTest()
    # KNN.classifyPerson()
    # testVector = KNN.img2vector('./digits/testDigits/0_13.txt')
    # print testVector[0, 0:31]
    # print testVector[0, 32:63]

    # KNN.handwritingClassTest()
    KNN.handwritingClassTest()