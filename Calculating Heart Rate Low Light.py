#!/usr/bin/env python
# coding: utf-8

# In[10]:


import cv2
import face_recognition
import PIL.Image
import PIL.ImageDraw
import os
from PIL import Image
import numpy as np
import datetime
from scipy import signal
from scipy.fftpack import fft, fftfreq, fftshift
from sklearn.decomposition import PCA, FastICA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


# In[11]:


vid1=cv2.VideoCapture("Desktop/Intern/Bright.mp4")
vid2=cv2.VideoCapture("Desktop/Intern/Lowlight.mp4")


# In[12]:


video_capture = cv2.VideoCapture("Desktop/Intern/Lowlight.mp4")
face_locations = []
R = []
G = []
B = []
T=0
pca = FastICA(n_components=3)
t1 = str(datetime.datetime.now())[-12:-7]
tim = []
bpmlist= []
i=0

while True:
    ret, frame = video_capture.read()
    if(ret==True):
        i+=1

    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_landmarks_list = face_recognition.face_landmarks(rgb_frame)
    pil_image = PIL.Image.fromarray(rgb_frame)

    for top, right, bottom, left in (face_locations):
        draw_shape = PIL.ImageDraw.Draw(pil_image)
        im = rgb_frame
        k = face_landmarks_list[0]['right_eyebrow']
        bottom= face_landmarks_list[0]['right_eyebrow'][0][1]
        for k1 in k :  
            if(bottom>k1[1]):
                bottom=k1[1]
        k = face_landmarks_list[0]['left_eyebrow']
        lbottom= face_landmarks_list[0]['left_eyebrow'][0][1]
        for k1 in k :   
            if(lbottom>k1[1]):
                lbottom=k1[1]
        bottom=min(bottom,lbottom)
        roi=frame[top:bottom, left:right]
        draw_shape.rectangle([left, top, right, bottom],outline="blue")
        r_channel=roi[:, :, :1]
        g_channel = roi[:, :, 1:2]
        b_channel=roi[:,:,2:]
        r_mean = np.mean(r_channel)
        g_mean = np.mean(g_channel)
        b_mean = np.mean(b_channel)
        R.append(r_mean)
        G.append(g_mean)
        B.append(b_mean)
    cv2.imshow('Video',roi)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    else:
        t2 = str(datetime.datetime.now())[-12:-7]
        FMT = '%M:%S'
        tdelta = datetime.datetime.strptime(t2, FMT) - datetime.datetime.strptime(t1, FMT)
        tim.append(tdelta.total_seconds())
        if i>=900:
            N=900
            G_std = StandardScaler().fit_transform(np.array(G[-(N-1):]).reshape(-1, 1))
            G_std = G_std.reshape(1, -1)[0]
            R_std = StandardScaler().fit_transform(np.array(R[-(N-1):]).reshape(-1, 1))
            R_std = R_std.reshape(1, -1)[0]
            B_std = StandardScaler().fit_transform(np.array(B[-(N-1):]).reshape(-1, 1))
            B_std = B_std.reshape(1, -1)[0]
            T = 1/(len(tim[-(N-1):])/(tim[-1]-tim[-(N-1)]))
            X_f=pca.fit_transform(np.array([R_std,G_std,B_std]).transpose()).transpose()
            N = len(X_f[0])
            yf = fft(X_f[1])
            yf = yf/np.sqrt(N)
            xf = fftfreq(N,T)
            xf = fftshift(xf)
            yplot = fftshift(abs(yf))
            plt.gcf().clear()
            fft_plot = yplot
            fft_plot[xf<=0.85] = 0
            print(str(xf[fft_plot[xf<=4].argmax()]*60)+' bpm')
            plt.plot(xf[(xf>=0) & (xf<=4)], fft_plot[(xf>=0) & (xf<=4)])
            plt.pause(0.001)
            bpm = xf[fft_plot[xf<=4].argmax()]*60
            bpmlist.append(bpm)
            
video_capture.release()
cv2.destroyAllWindows()


# In[13]:


s=0
for j in range(1,len(bpmlist)):
    dif = (bpmlist[j-1]/60-bpmlist[j]/60)**2
    s+=dif
s=s/len(bpmlist)
hrv=np.sqrt(s)
print("Heart rate variability is",hrv*1000,end=" milliseconds")


# In[14]:


print(np.mean(bpmlist),"beats per minute")


# In[ ]:




