#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import sys
import io
import time


# ## 파일명을 현재 시간으로 생성

# In[2]:


def makeFileName(saveDir = None, saveName = None):
    if saveDir is None:
        saveDir = "."
    if saveName is not None:
        return saveDir + '/' + saveName
    timestr = time.strftime("%y%m%d_%H%M%S")
    saveName = "Save_Rec_" + timestr
    return saveDir + '/' + saveName + '.mp4'


# In[3]:


def VideoWrite():
    try:
        print("카메라 구동")
        cap = cv2.VideoCapture(0)
    except:
        print("카메라 실패")
        return
    
    recode = False
    default_path = 'rec'
    newFileName = makeFileName(saveDir = default_path)
    
    # 폭, 높이 값을 카메라속성에 맞춤 (probID : 3 = 너비, 4 = 높이)
    # cap.set(probID, 속성값) 은 출력될 값들을 지정
    # cap.get(probID) 는 해당 속성에 대한 값을 리턴
    # 아래의 폭과 높이는 웹캠의 속성을 그대로 가져와 사용하는것.
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    fps = 20.0 # 초당 프레임 횟수
    
    # 코덱정보를 나타냄 아래의 두줄과 같이 사용할 수 있음.
    # 여러가지의 코덱종류가 있지만 윈도우라면 DIVX 를 사용
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    # fourcc = cv2.VideoWriter_fourcc('D','I','V','X')

    # 비디오 저장을 위한 객체를 생성해줌.
    out = cv2.VideoWriter(newFileName,fourcc, fps,(width, height))
    
    while(True):
        ret, frame = cap.read()

        if not ret:
            print("비디오 읽기 오류")
            break

        # 비디오 프레임이 정확하게 촬영되었으면 화면에 출력하여줌
        cv2.imshow('video',frame)
        # 비디오 프레임이 제대로 출력되면 해당파일에 프레임을 저장
        out.write(frame)

        # ESC키값을 입력받으면 녹화종료 메세지와 함께 녹화종료
        k= cv2.waitKey(1)
        if(k == 27):
            print('녹화 종료')
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


# In[4]:


if __name__ == '__main__':
    VideoWrite()


# In[ ]:




