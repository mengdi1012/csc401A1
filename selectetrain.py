#!/usr/bin/python
import sys
import os
import re


if __name__ == "__main__":
   n = int(sys.argv[1])
   f = open("train.arff")
   w = open("train_"+ str(n)+".arff",'w')
   
   while True:
      line = f.readline()
      print>> w,line.strip()
      if line.strip() == '@data':
         break
   for i in range(n):
      line = f.readline()
      print>> w,line.strip()
   for j in range(10000-n):
      line = f.readline()
   for i in range(n):
      line = f.readline()
      print>> w,line.strip()     
   
   w.close()
   f.close()
   
   
