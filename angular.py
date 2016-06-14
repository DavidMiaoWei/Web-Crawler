#!/usr/bin/env python
"""
This is a template script to get the phase of N fireflies
Author: Yunjing LIU
"""

# Standard imports 
import numpy as np
from scipy.integrate import odeint
# A class is a way of grouping variables and functions 
# together. Functions of a class are called methods.

# This defined a class which inherits from the standard python object.
class Angularfrequency(object):
    
    # The __init__ method is a special function that gets called
    # when a new instance of the class is called. All class methods
    # must have "self" as the first argument. This refers to the instance
    # itself.
    def __init__(self, numpoints):
        """
        In this method we will randomly pick initial phase for 
        the given number of points and setup a 2d figure that 
        we will use to plot to.
        """
        self.numpoints = numpoints
        self.delta = 0.5 # the time step between frames                
        #set parameters 
        self.K = 0.13;
        self.mu = np.pi/12.0
        self.sigma = np.pi/60.0
        self.omega = np.random.normal(self.mu, 
                                      self.sigma, 
                                      self.numpoints)
        self.kura0 = np.zeros(self.numpoints);
        # pick random initial phase
        for i in range(self.numpoints):
            self.kura0[i] = np.random.uniform(0,2*np.pi);       
        # call the kuramoto function, therefore we have an array kura
        self.kuramoto();
        #set time value
        self.time = 500
        self.deriva = self.phase(self.kura[self.time,:],
                                 self.space[self.time])
        
       
    def phase(self,y,t):
        """
        In this method we are calculating the derivative functions for the ode
        """
        self.y = y;
        self.t = t;
        
        self.deri = np.zeros(self.numpoints);
        # the derivatives of every phase        
        for i in range(self.numpoints):
            self.p = 0;
            for j in range(self.numpoints):
                self.p = self.p + np.sin(self.y[j] - self.y[i])
            self.p = self.p*self.K/self.numpoints;
            self.deri[i] = self.omega[i] + self.p;
        # return the derivatives as an array
        return self.deri;
        
    def kuramoto(self):
        """
        In this method we are calculating the phase of every fireflies
        """
        self.spacemin =  0.0;
        self.spacemax = 1000.0;
        # get linear distributed time 
        self.space = np.arange(self.spacemin, 
                               self.spacemax+self.delta, self.delta);
        # calculate phase of every fireflies 
        self.kura = odeint(self.phase, self.kura0, self.space)
       

