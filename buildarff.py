#!/usr/bin/python
import sys
import os
import re

mordern_slang = dict.fromkeys(['smh', 'fwb', 'lmfao', 'lmao', 'lms', 'tbh', 'rofl', 'wtf', 'bff',\
            'wyd', 'lylc', 'brb', 'atm','lol','imao', 'sml', 'btw','bw', 'imho', 'fyi', 'ppl', 'sob', 'ttyl',\
            'imo', 'ltr', 'thx', 'kk', 'omg', 'ttys', 'afn', 'bbs', 'cya', 'ez', 'f2f', 'gtr',\
            'ic', 'jk', 'k', 'ly', 'ya', 'nm', 'np', 'plz', 'ru', 'so', 'tc', 'tmi', 'ym', 'ur', 'u', 'sol'])

def collecting_data(twtt):
   list_data=[0 for i in range(24)]
   list = twtt.split('\n')
   features = ''
   features += str(len(list)-1 )+','
   text = ' '.join(list[1:])
   list_data[0] = str(feat1(text))
   list_data[1] = str(feat2(text))
   list_data[2]= str(feat3(text))
   list_data[3]= str(feat4(text))
   list_data[4]= str(feat5(text))
   list_data[5]= str(feat6(text))
   list_data[6]= str(feat7(text))
   list_data[7]= str(feat8(text))
   list_data[8]= str(feat9(text))
   list_data[9]= str(feat10(text))
   list_data[10]= str(feat11(text))
   list_data[11]= str(feat12(text))
   list_data[12]= str(feat13(text))
   list_data[13]= str(feat14(text))
   list_data[14]= str(feat15(text))
   list_data[15]= str(feat16(text))
   list_data[16]= str(feat17(text))
   list_data[17]= str(feat18(twtt))
   list_data[18]= str(feat19(text))
   list_data[19]= str(feat20(twtt))
   list_data[20]= str(feat21(text))
   list_data[21]= str(feat22(text))
   list_data[22]= str(feat23(text))
   m = re.match(r'<A=(\d)>',list[0])
   #polarity number
   list_data[23] = m.group(1)
   
   return ','.join(list_data)


def feat1(twtt):
   regex = re.compile(r"(\s|^)(I|me|my|mine|we|us|our|ours)/PRP",re.IGNORECASE)
   match = regex.findall(twtt)
   return len(match)

def feat2(twtt):
   regex = re.compile(r"(\s|^)(you|your|yours|u|ur|urs)/PRP",re.IGNORECASE)
   match = regex.findall(twtt)
   return len(match)

def feat3(twtt): 
   regex = re.compile(r"(\s|^)(he|she|her|him|his|hers|it|they|them|their|theirs)/PRP",re.IGNORECASE)
   match = regex.findall(twtt)
   return len(match)

def feat4(twtt):
   regex = re.compile(r"(\s|^)[\w]+/CC")
   match = regex.findall(twtt)
   return len(match)

def feat5(twtt):
   regex = re.compile(r"(\s|^)[\w]+/VBD")
   match = regex.findall(twtt)
   return len(match)

def feat6(twtt):
   regex = re.compile(r"(\s|^)((('ll|will)/MD)|(gonna/VBG)|(going/VBG to/TO \w+/VB))",re.IGNORECASE)
   match = regex.findall(twtt)
   return len(match)
def feat7(twtt):
   regex = re.compile(r"(\s|^),/,")
   match = regex.findall(twtt)
   return len(match)

def feat8(twtt):
   regex = re.compile(r"(\s|^)[:;]/:")
   match = regex.findall(twtt)
   return len(match)

def feat9(twtt):
   regex = re.compile(r"(\s|^)\-+/:")
   match = regex.findall(twtt)
   return len(match)

def feat10(twtt):
   regex = re.compile(r"(\s|^)([\[\(\{]+/\()|([\]\)\}]+/\))")
   match = regex.findall(twtt)
   return len(match)

def feat11(twtt):
   regex = re.compile(r"(\s|^)[...]{3,}/")
   match = regex.findall(twtt)
   return len(match)

def feat12(twtt):
   regex = re.compile(r"(\s|^)[\w]+/NNS?(\s|$)")
   match = regex.findall(twtt)
   return len(match)

def feat13(twtt):
   regex = re.compile(r"\w+/NNPS?")    # NNP or NNPS
   match = regex.findall(twtt)
   return len(match)

def feat14(twtt):
   regex = re.compile(r"(\s|^)\w+/RB")     #RB RBR RBS
   match = regex.findall(twtt)
   return len(match)

def feat15(twtt):
   regex = re.compile(r"(\s|^)\w+/(WDT|WP|WRB)")
   match = regex.findall(twtt)
   return len(match)

def feat16(twtt):
   list_word = twtt.split()
   count = 0;
   for word in list_word:
      w = word.split('/')[0].lower()
      if w in mordern_slang:
         count += 1
   return count

def feat17(twtt):
   regex = re.compile(r"(\s|^)[A-Z]{2,}/")
   match = regex.findall(twtt)
   return len(match)

def feat18(twtt):
   list = twtt.split('\n')
   tok = 0
   n = 0
   for sent in list[1:]:
      if sent:
         tok += len(sent.split())
         n+=1
   return round(1.0*tok/n,2)

def feat19(twtt):
   tok = 0
   char = 0
   for token in twtt.split():
      m = re.match(r"([\d\w\.]+)/\w+",token)
      if m:         
         char += len(m.group(1))
         tok += 1
   return round(1.0*char/tok,2)

def feat20(twtt):
   list = twtt.split('\n') 
   return len(list)-1

def feat21(twtt):
   #negative emoji :( ;( -( :;(
   regex = re.compile(r"[:;\-\']\(/[\w]+")
   match = regex.findall(twtt)
   return len(match) 

def feat22(twtt):
   #positive emoji :) ;) -) ;D :D XD :P
   regex = re.compile(r"([:;\-][\)DP]|^XD|^xD)/[\w]+")
   match = regex.findall(twtt)
   return len(match) 

def feat23(twtt):
   regex = re.compile(r"^(not|no|never|'t|deny|nobody|nonsense)/",re.IGNORECASE)
   match = regex.findall(twtt)
   return len(match)
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
   print >> arff_file, '@attribute 1st_person_pro numeric'
   print >> arff_file, '@attribute 2ndperson_pro numeric'
   print >> arff_file, '@attribute 3rdperson_pro numeric'
   print >> arff_file, '@attribute coordinating_conjunction numeric'
   print >> arff_file, '@attribute past_tense_verb numeric'
   print >> arff_file, '@attribute future_tense_verb numeric'
   print >> arff_file, '@attribute commas numeric'
   print >> arff_file, '@attribute colon_and_semicolon numeric'
   print >> arff_file, '@attribute dashes numeric'
   print >> arff_file, '@attribute parenthses numeric'
   print >> arff_file, '@attribute ellipses numeric'
   print >> arff_file, '@attribute common_nouns numeric'
   print >> arff_file, '@attribute proper_nouns numeric'
   print >> arff_file, '@attribute adv numeric'
   print >> arff_file, '@attribute wh_words numeric'
   print >> arff_file, '@attribute modern_slang numeric'
   print >> arff_file, '@attribute all_up_case numeric'
   print >> arff_file, '@attribute avg_len_sent numeric'
   print >> arff_file, '@attribute avg_len_token numeric'
   print >> arff_file, '@attribute num_sentences numeric'
   print >> arff_file, '@attribute neg_emoji numeric'
   print >> arff_file, '@attribute pos_emoji numeric'
   print >> arff_file, '@attribute neg_words numeric' 
   print >> arff_file, '@attribute polarity {0,4}\n'
   
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
      print >> arff_file, collecting_data(twtt)

      if not line:
         break
      twtt = line
      count += 1
   
   twtt_file.close()
   arff_file.close()