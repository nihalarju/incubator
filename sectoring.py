#!/usr/bin/python

__author__      = "Nihal Arju, nihal.arju@gmail.com"
__version__     = "0.1"
__license__     = "GNU GPL v3.0"

import numpy as np
import scipy as sc
import pandas as pd
from random import shuffle
import Quandl
from matplotlib.mlab import PCA

global verbose
verbose = True

def main():
    nin = 10
    npc = 3
    SP500_all = pd.read_csv('tickers.csv')
    #len(SP500['Ticker']))
    shuffle(SP500_all["Ticker"])
    SP500 = SP500_all[:10]
    print(SP500)
        
#     history = pd.DataFrame()
#     for ticker in SP500['Ticker']:
#         qhandle = 'WIKI/'+ticker
#         print(qhandle)
#         history[ticker] = Quandl.get(qhandle)['Close']
#         pass
    #history.to_pickle('history.pkl')
    
    pd.from_pickle('history.pkl')
    
    history = history.interpolate(method='linear', axis=1, limit=None)
    hm = np.array(history.values)
    pc = PCA(hm)
    
    phm = pc.project(hm)
    import matplotlib.pyplot as pp
    # %matplotlib inline
    dateseries = history.index
    latent = pc.fracs
    print("variance: ", np.cumsum (latent))
    
    for n in range(npc):
        pcn = phm[:,n]
        pp.plot(dateseries,pcn)
        legend(['1', '2', '3'])
    pp.show()
    
    
    
    
    
    
    

if __name__ == '__main__': main()