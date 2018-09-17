import matplotlib.pyplot as plt
import numpy as np

dx = .01 # difference in x and x-1 on axis.
exp = 0

def func(x):
    return(x**exp)
	
def derive(x,dt):
    return((func(x+dt)-func(x)) / dt)
	
def plot():
    fig, ax = plt.subplots(2,1,figsize=(5,10), dpi= 80,facecolor='w', edgecolor='k')
    x = np.arange(-5,5,dx)
    ax[0].set_title("X^" + str(exp))
    ax[0].scatter(x=x,y=[func(i) for i in x],s=1)
    ax[1].scatter(x=x,y=[derive(i,dx) for i in x],s=1,color='green')

powers = 5
fig, ax = plt.subplots(2,powers,figsize=(15,5), dpi= 80,facecolor='w', edgecolor='k')
plt.rcParams.update({'font.size': 10})
plt.subplots_adjust(wspace = 0.5,hspace=0.4)
x = np.arange(-5,5,dx)
exp = 0
for i in range(len(ax[0])):
    ax[0][i].set_title("x^" + str(exp))
    ax[0][i].scatter(x=x,y=[func(i) for i in x],s=1)
    ax[1][i].scatter(x=x,y=[derive(i,dx) for i in x],s=1,color='green')
    ax[1][i].set_title(str(exp) + "x^" + str(exp-1))
    exp = exp + 1

