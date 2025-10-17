# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 12:45:43 2025

@author: Christopher Ivan B
"""

class Controller:
    '''
    Developed as a class to accomodate further changes, eg.
     - integral control (for full PID)
     - adaptive control (parameter retuning)
    '''
    def __init__(self, KP, KD, sub):
        # PD control
        self.KP = KP
        self.KD = KD
        self.sub = sub # submarine instance - to get time step size
        
    def get_action(self,e_t,e_t1):
        return self.KP*e_t + self.KD*(e_t-e_t1)/self.sub.dt