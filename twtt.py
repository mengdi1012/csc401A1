#!/usr/bin/python

import sys
import re

def twtt1(tw):
   
   tw = re.sub(r'<[^>]+>','', tw) 
   return tw

def twtt2(tw):
   tw = tw.replace("&amp;",'&').replace("&lt;",'<').replace("&gt;",'>')\
   .replace("&quot;",'"').replace("&#39;","'")
   return tw
   
if __name__ == "__main__":

   if len(sys.argv) != 4:
      print "Usage: %s <training-data-filr> <student#> <output-file>" %(sys.argv[0])
      #sys.exit(0)

   rawfile = open("/u/cs401/A1/tweets/training.1600000.processed.noemoticon.csv","r")
   resultfile = open("train.twt","w")
   X = int("1001601019")%80
   count = 0
   while count <= 800000+X*10000+9999:
      line = rawfile.readline()
      if (count >= X*10000 and count <= X*10000+9999) \
         or (count >= 800000+X*10000):
         twtt = twtt1(line.strip())
         twtt = twtt2(twtt)
         
         print >>resultfile, twtt
         
      count+=1
         
   resultfile.close()
   rawfile.close()