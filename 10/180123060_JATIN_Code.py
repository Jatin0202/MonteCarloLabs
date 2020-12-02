""" Lab-10
    
    !! Designed by Jatin Dhingra !!
"""

import math
import random
import numpy as np
import matplotlib.pyplot as plt

M= [100, 1000, 10000, 100000]

for m in M:
    Im_Values= []
    Im_Tilda_Values= []
    for i in range(0, m):
        U= random.random()
        Im_Values.append( math.exp(math.sqrt(U)) )
        Im_Tilda_Values.append( (math.exp(math.sqrt(U))+math.exp(math.sqrt(1-U)))/2.00 )
    Mean1= np.average(Im_Values)
    Mean2= np.average(Im_Tilda_Values)
    Variance1= np.var(Im_Values)
    Variance2= np.var(Im_Tilda_Values)
    
    Length1= (1.96*Variance1)/math.sqrt(m)
    Length2= (1.96*Variance2)/math.sqrt(m)
    
    print("   Value of m: %d"%m)
    print("   Im: %f"%Mean1)
    print("   Im_Tilda: %f"%Mean2)
    print("   95Percent Confidence Interval of Im: [%f, %f]"%(Mean1-Length1, Mean1+Length1))
    print("   95Percent Confidence Interval of Im_Tilda: [%f, %f]"%(Mean2-Length2, Mean2+Length2))
    print("   Ratio of length of both Intervals: %f\n\n\n\n\n"%(Length1/Length2))
    