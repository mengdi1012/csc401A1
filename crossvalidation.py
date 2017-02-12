#!/usr/bin/python
import sys
import os
import re


if __name__ == "__main__":
   n = int(sys.argv[1])
   f = open("train.arff")
   train = open("train."+ str(n)+".arff",'w')
   test = open("test."+ str(n)+".arff",'w')
   
   while True:
      line = f.readline()
      print>> train,line.strip()
      print>> test,line.strip()
      if line.strip() == '@data':
         break
      

   for i in range(20000):
      line = f.readline()
      if (i/1000) % 10 == n:
         print>> test,line.strip()
      else:
         print>> train,line.strip()     
   
   train.close()
   test.close()
   f.close()
   