# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 23:11:51 2022

@author: Meiru

"""
#import packages
import math 
from scipy.stats import sem
import random

#define function to calculate mean of the sample
def cal_mean(sample,size):
    sum = 0
    for value in sample:
        sum += value
    mean = sum/size
    return mean

#define function to calculate standard deviation of the sample
def cal_dev(sample,mean):
    n = len(sample) -1
    sum = 0
    for i in sample:
        sum += (i-mean)**2
    var = sum/n
    std = math.sqrt(var)
    return std

#define function to calculate standard error of the sample
def cal_sterror(std,size):
    sterror =std/math.sqrt(size)
    return sterror

#set seed to replicate the results
random.seed(111)
population =range(10001)
population = list(population)
sample_sizes = [10,20,50,100,200,500,1000,5000]

# calculate the mean, std, standard error manually and verify the result by sem function
for size in sample_sizes:
    sample = random.sample(population, k = size)
    mean = round(cal_mean(sample,size),2)
    std = round(cal_dev(sample,mean),2)
    sterror = round(cal_sterror(std,size),2)
    ssem = round(sem(sample),2)
 
    print('sample size: '+str(size), 'sample mean: '+ str(mean),'sample standard deviation: '+str(std), 
              'sample standard error: '+ str(sterror), 'st error2: '+str(ssem))

