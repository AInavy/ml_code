#! -*- coding=utf-8 -*-
from os import listdir
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

    # for i in range(0, len(sortedClassCount)):
    #     print sortedClassCount[i]

    return sortedClassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0

    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1

    return returnMat, classLabelVector

def autoNorm(dataSet):
    # dataSet.min(0)选取列的最小值
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))

    return normDataSet, ranges, minVals

def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('./datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0

    for i in range(numTestVecs):
        # normMat[i, :] 单一预测样本;  normMat[numTestVecs:m, :] 900训练样本
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :],
                                     datingLabels[numTestVecs:m], 3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
        if (classifierResult != datingLabels[i]) :
            errorCount += 1.0
        print "the total error rate is: %f " % (errorCount / float(numTestVecs))

def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(raw_input("percentage of time spent playing video games? "))
    ffMiles = float(raw_input("frequent flier miles earned per year? "))
    iceCream = float(raw_input("liters of ice cream consumed per year? "))

    datingDataMat, datingLabels = file2matrix('./datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = [percentTats, ffMiles, iceCream]

    classifierResult = classify0((inArr-minVals)/ranges, normMat, datingLabels, 3)

    print "You will probably like this person: ", resultList[classifierResult - 1]

def img2vector(filename):
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        linestr = fr.readline()
        for j in range(32):
            returnVect[0, 32*i+j] = int(linestr[j])
    return returnVect

def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('./digits/trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        # print fileNameStr   # txtfilename
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)