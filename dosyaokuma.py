# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 16:34:45 2018

@author: muham
"""
""" C:\Users\muham\OneDrive\Belgeler\4.sinif1.donem\machine learning\project"""
import pandas as pd
import emoji

file = open("data.txt",encoding="utf8")
data_file = open("emojis.txt", 'w',encoding="utf8")
for satir in file:
    part1 = satir.split(':')
    part2=part1[1]
    fullname=part2.split('-')[1]
    for karakter in satir:
        if karakter in emoji.UNICODE_EMOJI:
            data_file.write(fullname.strip()+",")
            data_file.write(karakter)
            data_file.write("\n")
            
 