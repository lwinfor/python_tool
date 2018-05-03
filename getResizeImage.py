#coding:utf-8
import os
import math
import numpy as np
import PIL
from PIL import Image

srcPath=u"E:/植物分析/test_set_6k_safe"
resultpath=u"E:/植物分析/result.txt"

resizeDstPath=u"/4thdd1/plant/test/test_set_6k_safe_min_wx"
cropDstPath=u"/4thdd1/plant/test/test_set_6k_safe_ios_qb"


srcImgList=[]

def centerCrop(imgList,dstPath):
    for imgPath in imgList:
        target_w=480
        target_h=640
        factor=0.0
        fileName=os.path.basename(imgPath)
        dstItem=os.path.join(dstPath,fileName)
        img=Image.open(imgPath)
        w, h=img.size
        print w,h
        w_factor=target_w/float(w)
        h_factor=target_h/float(h)
        w_center=0
        h_center=0
        print w_factor,h_factor
        if w_factor>=1 and h_factor>=1:
            print "=========crop===========111111"
            pass
        elif w_factor <1 and h_factor>=1:
            print "=========crop===========22222"
            pass
        elif w_factor>=1 and h_factor<1:
            print "=========crop===========33333"
            pass
        else:
            print "=========crop===========444444"
            pass
        if w_factor>=h_factor:
            factor=w_factor
            h_center=(target_h-h*factor)*0.5
        else:
            factor=h_factor
            w_center=(target_w-w*factor)*0.5
        if w_center<0:
            w_center*=-1
        if h_center<0:
            h_center*=-1
        if w_factor>=h_factor:
            w_new=target_w
            h_new=factor*h
        else:
            h_new=target_h
            w_new = factor*w
        w_center=int(w_center)
        h_center=int(h_center)
        w_new=int(w_new)
        h_new=int(h_new)
        print w_center,h_center,w_new,h_new,target_w,target_h

        img = img.resize((w_new, h_new))
        print "resize===>>",img.size
        target_w+=w_center
        target_h+=h_center
        img=img.crop((w_center,h_center,target_w,target_h))
        print img.size
        img.save(dstItem)

def resize(imgList,dstPath):
    for imgPath in imgList:
        fileName=os.path.basename(imgPath)
        dstItem=os.path.join(dstPath,fileName)
        img=Image.open(imgPath)
        w, h=img.size
        w_new=w
        h_new=int(round(h/1.15))
        print w_new, h_new
        result = img.resize((w_new, h_new))
        print result.size
        result.save(dstItem)

for item in os.listdir(srcPath):
    itemPath=os.path.join(srcPath,item)
    srcImgList.append(itemPath)


def wh_list(srcImgList):
    w_file=[]
    h_file=[]
    for imgPath in srcImgList:
        fileName=os.path.basename(imgPath)
        img = Image.open(imgPath)
        w, h = img.size
        if w>h:
            w_file.append(fileName)
        else:
            h_file.append(fileName)
    with open(u"E:/植物分析/w_file.txt",'w') as fw:
        for item in w_file:
            fw.write(item.encode('utf-8')+"\n")
    with open(u"E:/植物分析/h_file.txt",'w') as fwte:
        for item in h_file:
            fwte.write(item.encode('utf-8')+"\n")

def get_WH_right(srcImgList,resultpath):
    resultList=open(resultpath).readlines()
    rightCnt=0
    wrongCnt=0
    w_file=[]
    h_file=[]
    for imgPath in srcImgList:
        fileName=os.path.basename(imgPath)
        img = Image.open(imgPath)
        w, h = img.size
        if w>h:
            w_file.append(fileName.encode('utf-8'))
        else:
            h_file.append(fileName.encode('utf-8'))
    print len(w_file),len(h_file)
    for result in resultList:
        reItem=result.split('|')
        name=os.path.basename(reItem[1].strip())
        flag=reItem[13].strip()
        print name,flag
        if name in h_file:
            print "hhhhhhh",name
        else:
            #print "wwwww",name
            continue
        if flag =='False':
            wrongCnt+=1
        elif flag == 'True':
            rightCnt+=1
        else:
            print "error"
    print wrongCnt,rightCnt,rightCnt/float(wrongCnt+rightCnt)
    pass

#resize(srcImgList,resizeDstPath)
#centerCrop(srcImgList,cropDstPath)
#wh_list(srcImgList)
get_WH_right(srcImgList,resultpath)
