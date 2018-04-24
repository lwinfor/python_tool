#coding:utf-8

import cv2
print cv2.__version__
import numpy as np

import numpy as np
import cv2

#BackgroundSubtractorMOG2
#opencv自带的一个视频
cap = cv2.VideoCapture('vtest.avi')
#获得码率及尺寸
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
videoWriter = cv2.VideoWriter('./test_bgs_KNN_default.avi', fourcc, fps, size)
#创建一个3*3的椭圆核
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
#创建BackgroundSubtractorMOG2
#fgbg = cv2.createBackgroundSubtractorMOG2()
fgbg = cv2.createBackgroundSubtractorKNN()
ret, frame = cap.read()
while(ret):
    fgmask = fgbg.apply(frame)

    # 二值化阈值处理，前景掩码含有前景的白色值以及阴影的灰色值，在阈值化图像中，将非纯白色（244~255）的所有像素都设为0，而不是255
    th = cv2.threshold(fgmask.copy(), 244, 255, cv2.THRESH_BINARY)[1]
    # 下面就跟基本运动检测中方法相同，识别目标，检测轮廓，在原始帧上绘制检测结果
    fgmask = cv2.dilate(th, kernel, iterations=2) # 形态学膨胀

    #形态学开运算去噪点
    #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    #寻找视频中的轮廓
    im, contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, contours, -1, (0, 0, 255), 3)
    #print contours
    max=0
    save=[]
    for c in contours:
        #计算各轮廓的周长
        perimeter = cv2.arcLength(c,True)
        if cv2.contourArea(c) > 1600:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)

    # # 找到一个直矩形（不会旋转）
    # x, y, w, h = cv2.boundingRect(save)
    # # 画出这个矩形
    # cv2.rectangle(frame, (x, y), (x + w, y + h), ( 0, 0,255), 2)

    cv2.imshow('frame',frame)
    cv2.imshow('fgmask', fgmask)
    videoWriter.write(frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    ret, frame = cap.read()
cap.release()
videoWriter.release()
cv2.destroyAllWindows()
print 'done!'