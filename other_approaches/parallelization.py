# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 17:45:29 2017

@author: sarthak
"""

import pandas as pd
import redis
import numpy as np
from multiprocessing import Process


if __name__ == '__main__':

    user_data = pd.read_csv('data/sample_data.csv')
    airport_data = pd.read_csv('data/optd-sample-20161201.csv')
    
    user_data_np = user_data.as_matrix()
    airport_data_np = airport_data.as_matrix()
    
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    
    for row in user_data_np:
        r.geoadd("user", row[2], row[1], row[0])
    
    for row1 in airport_data_np:
        r.geoadd("user", row1[2], row1[1], row1[0])
    
    airp = []
    for i in r.zrange("user", 0, -1):
        if len(i)==3:
            airp.append(i)
    
    uuser = []
    for i in r.zrange("user", 0, -1):
        if len(i) > 3:
            uuser.append(i)
            
    distt = {}
    def cal_dist(xx):
        for i in xx:
            dis_a = {}
            for j in airp:
                dis_a[j] = r.geodist("user", i, j)
            distt[i] = min(dis_a, key=dis_a.get)
        
    X1 = uuser[0:200000]
    X2 = uuser[200000:400000] 
    X3 = uuser[400000:600000] 
    X4 = uuser[600000:800000] 
    X5 = uuser[800000:1000000] 
    
    
    p1 = Process(target=cal_dist,args=(X1))
    p2 = Process(target=cal_dist,args=(X2))
    p3 = Process(target=cal_dist,args=(X3))
    p4 = Process(target=cal_dist,args=(X4))
    p5 = Process(target=cal_dist,args=(X5))
    
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()