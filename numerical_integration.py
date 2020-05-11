#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def euler_rate(rate,time,x0):
    time = np.array(time); f = np.array(rate)
    dt = time[1]-time[0]
    x = x0*np.ones(np.size(time))
    for i,t in enumerate(time[0:-1]):
        dx = f[i]*dt
        x[i+1] = x[i]+dx
    return x


# In[3]:


def eulerA(A,x0,y0,T,dt):
    time = np.arange(0,T,dt)
    x = np.ones(np.size(time))*x0
    y = np.ones(np.size(time))*y0
    #nth variable
    for i,t in enumerate(time[0:-1]):
        v = np.array([[x[i]], [y[i]]])
        dv = np.dot(A,v)*dt
        v = v+dv
        x[i+1] = v[0]
        y[i+1] = v[1]
        #nth variable
    return x,y,time #,n


# In[4]:


def eulerFG(f,g,x0,y0,T,dt):
    time = np.arange(0,T,dt)
    x = np.ones(np.size(time))*x0
    y = np.ones(np.size(time))*y0
    #nth variable
    for i,t in enumerate(time[0:-1]):
        dx = f(x[i],y[i])*dt
        dy = g(x[i],y[i])*dt
        x[i+1] = x[i]+dx
        y[i+1] = y[i]+dy
        #nth variable
    return x,y,time #,n


# In[5]:


def vectorize(f,g,ax_max,sp):
    #creating the meshgrid
    x = np.arange(0, ax_max, sp)
    y = np.arange(0, ax_max, sp)
    X, Y = np.meshgrid(x, y, sparse = True)
    U = f(X,Y)
    V = g(X,Y)
    C = np.sqrt((U**2)+(V**2))
    U = U/C; V = V/C
    return U,V,X,Y,C

