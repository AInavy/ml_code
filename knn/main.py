#! -*- coding=utf-8 -*-
import os, sys
import KNN

if __name__ == "__main__":
    group, labels = KNN.createDataSet()
    print group
    # print type(group)
    print labels

    print KNN.classify0([0,0], group, labels, 3)