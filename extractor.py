#!/usr/bin/python
# -*- coding: utf-8 -*-
import glob
import subprocess
import os

def mtd_extractor(imgPath):
    infoDict = {} #Creating the dict to get the metadata tags
    exifToolPath = "exiftool"
    ''' use Exif tool to get the metadata '''
    process = subprocess.Popen([exifToolPath,imgPath],stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True) 
    ''' get the tags in dict '''
    for tag in process.stdout:
        line = tag.strip().split(':')
        infoDict[line[0].strip()] = line[-1].strip()

    #for k,v in infoDict.items():
        #print(k,':', v)
    return infoDict['File Type']+' '+infoDict['File Size']+' '+infoDict['Image Size']+' '+infoDict['Megapixels']

# Main
paths = glob.glob('images/*.jpg')
f = open("metadata.txt","w+")
for imgPath in paths:
    metadata = mtd_extractor(imgPath)
    f.write(os.path.basename(imgPath) + ' ' + metadata + '\n')
f.close()
