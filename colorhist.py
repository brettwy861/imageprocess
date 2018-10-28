#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 13:36:51 2018

@author: brettwang
"""

from PIL import Image
import os
import json

def gethex(val):
    if len(hex(val)[2:])<2:
        return '0'+hex(val)[2:]
    else:
        return hex(val)[2:]
    
stepsize = 1
result = {}
for item in os.listdir():
    if item[-4:]=='.png':
        result['.'.join(item.split('.')[0].split('_'))]=[]
        # Create an Image with specific RGB value
        image = Image.open("./"+item)
        colordict = {}
        size = image.size
        for i in range(0,size[0],stepsize):
            for h in range(0,size[1],stepsize):
                #print([i,h])
                pixel = image.getpixel((i,h))
                hexcolor = '#'+gethex(pixel[0])+gethex(pixel[1])+gethex(pixel[2])
                if hexcolor not in colordict.keys():
                    colordict[hexcolor]=1
                else:
                    colordict[hexcolor]+=1
        
        #merge all black white grey color 
        whiteblack = {}
        for k,v in colordict.items():
            if (k[1:3]==k[3:5]) and (k[3:5]==k[5:7]):
                whiteblack[k]=v
        colordict['#blackwhite']= sum(whiteblack.values())
                  
        #remove these color from colordict and replace with new key:value        
        for k in whiteblack.keys():
            colordict.pop(k)
    
        sorted_names = sorted(colordict, key=lambda x: colordict[x])
        for k in sorted_names[-1:-10:-1]:
            print("{} : {}%".format(k, round(100*colordict[k]/(size[0]*size[1]/(stepsize**2)),2)))    
            result['.'.join(item.split('.')[0].split('_'))].append({k:round(100*colordict[k]/(size[0]*size[1]/(stepsize**2)),2)})
            
with open('color_result.json','w') as f:
    json.dump(result, f, indent=2)
