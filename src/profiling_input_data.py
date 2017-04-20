#!/usr/bin/env python

##
# @file profiling_input_data.py
# Generated input for profiling
#
# @author Igor Ignác xignac00@stud.fit.vutbr.cz

import random
import sys

##
# @brief Generate random numbers in range <1,1000>
# @param switch Int value, sets which group is called
def random_input(switch):
    if switch == 1:
        my_randoms_10 = random.sample(range(1000000), 10)
        for i in my_randoms_10:
            print (i)

    elif switch == 2:
        my_randoms_100 = random.sample(range(1000000), 100)
        for i in my_randoms_100:
            print (i)

    elif switch == 3:
        my_randoms_1000 = random.sample(range(1000000), 1000)
        for i in my_randoms_1000:
            print (i)
    return;

switch=int(sys.argv[1])
random_input(int(switch))
## End of file
