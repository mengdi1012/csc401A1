#!/usr/bin/python
import sys
import os
import re
def find_feature(twtt):
    list = twtt.split('\n')
    features = ''
    features += str(len(list)-1 )+','
    text = ' '.join(list[1:])
    print text;
    m = re.match(r'<A=(\d)>',list[0])
    features += m.group(1)
    return features

if __name__ == "__main__":

   if len(sys.argv) <3 or len(sys.argv)>4 :
       print "Usage: %s <input filename> <arff file> [<max number>]" %(sys.argv[0])
       sys.exit(0)
       
   if not os.path.exists(sys.argv[1]):
       print sys.argv[1] + " not exists"
       sys.exit(0)
       
   twtt_file = open(sys.argv[1],'r')
   arff_file = open(sys.argv[2],'w')
   print >> arff_file, '@relation tweets\n'
   print >> arff_file, '@attribute sentences_number numeric'
   print >> arff_file, '@attribute firstperson_pronoun numeric'
   print >> arff_file, '@attribute secondperson_pronoun numeric'
   print >> arff_file, '@attribute thirdperson_pronoun numeric'
   print >> arff_file, '@attribute coordinating_conjunction numeric'
   print >> arff_file, '@attribute past_tense_verb numeric'
   print >> arff_file, '@attribute future_tense_verb numeric'

   print >> arff_file, '@attribute polarity numeric\n'
   
   print >> arff_file, '@data'

   max_twt = 0
   
   if len(sys.argv)==4:
       max_twt = int(sys.argv[3])
   
   count = 0
   twtt = twtt_file.readline()
   while count < max_twt or max_twt == 0:
       while True:
          line = twtt_file.readline()
          if not line or line.startswith('<A='):
              break
          twtt += line
       print >> arff_file,find_feature(twtt)

       if not line:
           break
       twtt = line
       count += 1
    
   twtt_file.close()
   arff_file.close()