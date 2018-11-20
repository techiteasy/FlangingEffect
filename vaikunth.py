# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 23:50:30 2018

@author: Vaikunth Bhandare

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import math

#Input file for filter effect
data = pd.read_csv('vaikunth.dat', sep='\s+', header=None)# read file

x=data[0]#read colmn 0
y=data[1] #read coumn 1
xlist=[] 
ylist=[]
#set float values for range
for i in range(0,int(len(x))):
    xlist.append(float(x.iloc[i]))
    ylist.append(float(y.iloc[i]))
    
print(len(ylist))
#output file for setting filtered values with write settings
f= open("outvaikunth.dat","w")

#Set Sample Rate & Channel in Output File on each line
f.write("; Sample Rate "+ str(44100)+"\n")
f.write("; Channels 1 "+"\n")

rate=1

#Set Time Delay Threshold
Dt=0.003
index=range(1,len(ylist))
sin_ref=[0]

#Calculate filter equation
for i in range(1,len(ylist)):
    
    temp = (np.sin(2*np.pi*i*(float(rate)/44100)))#Sine Wave Equation
    sin_ref.append(temp)

#Set Sample Delay Threshold
Ds=round(Dt*44100)

y =[0 for x in range(len(ylist))]
for i in range(1,Ds):
  y[i]=ylist[i]

#Set Amp
amp=0.7

#Loop to create Flanging effect
for i in range((Ds+1),len(ylist)):
    Sc=abs(sin_ref[i])
    Dc=math.ceil(Sc*Ds)
    y[i] = (amp*ylist[i]) + amp*(ylist[i-Dc])





#Set Final Values of Xlist & Ylist
for i in range(0,len(y)):

    f.write(str(xlist[i])+"  " + str((y[i])) +"\n")

f.close()
