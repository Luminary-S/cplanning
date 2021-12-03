#!/usr/bin/python3
# -*- coding: utf-8 -*-
#author: sgl
#date: 20211203

import matplotlib.pyplot as plt
import numpy as np

class Env:
    '''
    create the environment of the window in 2D way, if the window is described in 3D, it should be mapped into 2D;
    gray map, gray level of the point means the hard 

    :Param a  window length
    :Param b  window width
    :Param S  ( s, t ): s is the area of the dirt, and t is the cleaned times in this area
    :Param S_list  dirt list, list the dirt area
    :returns: planning path P in list 
    '''
    CLEAN = 0
    def __init__(self):
        # self.a = 
        pass
        self.S_list = []
    
    def init_param(self):
        self.a = 100
        self.b = 100
        self.N = 10
        s_max, s_min, f_max, f_min = 10, 10, 10, 10
        self.S = self.dirt_creator(N, s_max, s_min, f_max, f_min)
    '''
    procedure:
    1. init parameters
    2. input dirt list; simulator:dirt_creator(self, N, s_max, s_min, f_max, f_min)
    2. display dirt area
    '''
    def run(self):
        global CLEAN
        self.init_param()
        S = self.S
        self.S_list.append(S)
        while CLEAN:
            self.F_creator(F,S)  # if in reality, F ig given to robot controller
            S = self.clean_dirt(F) # simulation, if in reality, it's the real cleaning process
            self.S_list.append(S)
            CLEAN = self.dirt_check(S)
            self.dirt_display(S)

    '''
    get the clean force from robot, if simulation,  F gets from F_creator
    '''     
    def set_F(self, F):
        self.F = F

    def F_creator(self, F, S):


        return F

    '''
    create the dirt area

    @input N, s_max, s_min, f_max, f_min
    @Param N number of the dirt
    @Param s_max Maximum area of the dirt
    @Param s_min Minimum area of the dirt
    @Param f_max Maximum cleaning force of the dirt
    @Param f_min Minimum cleaning force of the dirt
    @return  S
    '''
    def dirt_creator(self, N, s_max, s_min, f_max, f_min):
        
        pass

    def dirt_display(self):
        fig = plt.figure()
        figure = ax.plot(first_2000, second_2000, third_2000, c='r')
        plt.show()


    def dirt_clean(self):
        return S_list

    def dirt_f_function(self, f, f_in):
        pass

'''
vibration utilization planning
get the vibration direction vx,
get the outline of the 

'''
class Planner:

    def __init__(self):
        
        pass