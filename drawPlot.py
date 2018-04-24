#coding:utf-8
import os
import json

import numpy as np
import pylab as pl

def drawPlot(savePlotPath,name):
    savePathItem=open(savePlotPath).readlines()
    totalData=[]

    cntLen=0
    for item in savePathItem:
        try:
            if item == "":
                continue
            result=float(item.strip())
            totalData.append(result)
        except:
            continue
        # if cntLen>100:
        #     break
        # cntLen+=1
    print len(totalData)
    #data = np.random.normal(5.0, 3.0, 10)
    #print totalData
    #make a histogram of the data array
    pl.hist(totalData)
    # make plot labels
    pl.xlabel(name)
    pl.show()
