#!/usr/bin/env python
# coding: utf-8

# In[27]:


import numpy as np
import matplotlib.pyplot as plot

def main():
    period1 = np.arange(0, 2*np.pi,0.01)
    period2 = np.arange(0,2*np.pi,0.02)
    period3 = np.arange(0,2*np.pi,0.05)
    sin = np.sin(period1)
    cos = np.cos(period2)
    tan = np.tan(period3)
    plot.plot(period1,sin,period2,cos,period3,tan)
    plot.ylim(-5,5)
    plot.xlim(0,6)
    plot.title("Sine, Cosine, and Tangent Graphs")
    plot.legend(['Sine', 'Cosine','Tangent'])
    plot.show()
    
if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




