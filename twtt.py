#!/usr/bin/python
import os
import sys
import re
import NLPlib

abbr = {}
tagger = NLPlib.NLPlib()


def twtt1(tw):
    tw = re.sub(r'<[^>]+>','', tw) 
    return tw

def twtt2(tw):
    tw = tw.replace("&amp;",'&').replace("&lt;",'<').replace("&gt;",'>')\
       .replace("&quot;",'"').replace("&#39;","'")
    return tw

def twtt3(tw):
    tw = re.sub(r'([^\w\d])(http://|https://|www\.)[^\s\"]+',r'\1',tw)
    return tw

def twtt4(tw):
    tw = re.sub(r'[@#]([\w\d]+)',r'\1',tw)
    return tw


def twtt5(tw):
    listwords= tw.split()
    sentences = ''
    for i in range(len(listwords)):
        word = listwords[i]
        sentences += word+' '
        lastchar = word[-1]
        if lastchar == '?' or lastchar == '!':
            sentences += '\n'
        
        elif lastchar == '.':
            if not abbr.has_key(word) and i+1 < len(listwords) \
                and listwords[i+1][0].isupper(): 
                sentences += '\n' 
    return sentences

def twtt7(tw):
    sent_list = tw.split('\n')
    sentences = ''
    for sentence in sent_list:
        words = sentence.split()
        for word in words:
            if abbr.has_key(word):
                sentences += word+' '
            else:   
                m = re.match(r'([^\w]*)(\w+)([^\w].*|$)', word)
                if not m:
                    sentences +=word + ' '
                else:
                    if not m.group(1):
                        sentences += m.group(2)+' '
                        # try to match such as "word...word!!!"
                        m1 = re.match(r'([^\w]*)(\w+)([^\w].*|$)', m.group(3))
                        if not m1:
                           sentences += m.group(3)+' '
                        else:
                           if not m1.group(1):
                              sentences += m1.group(2)+' '+m1.group(3)+' '
                           else:
                              sentences += m1.group(1)+' '+m1.group(2)+' '+m1.group(3)+' '
                    else:
                        sentences += m.group(1)+' '+m.group(2)+' '+m.group(3)+' '
        
        if sentence:
            sentences += '\n'
    return sentences
 
def twtt8(tw):
    sent_list = tw.split('\n')
    result = ''
    
    for sentence in sent_list:
        word_list = sentence.split()
        tags = tagger.tag(word_list)
        for i in range(len(word_list)):
            result += word_list[i]+'/'+tags[i] +' '
        result +=  '\n'
     
    return result.strip()

def twtt9(pol,twtt):
    return '<A='+pol+'>\n' + twtt
    
if __name__ == "__main__":

    if len(sys.argv) != 4:
        print "Usage: %s <training-data-filr> <student#> <output-file>" %(sys.argv[0])
        sys.exit(0)
      
    if not os.path.exists(sys.argv[1]):
        print sys.argv[1] + " not exists"
        sys.exit(0)
       
    fn_abbr = "/u/cs401/Wordlists/abbrev.english"
    if not os.path.exists(fn_abbr):
        print fn_abbr + " not found"
        exit(0)

    fileabbr = open(fn_abbr,"r")
    while True:
        line = fileabbr.readline()
        if not line:
            break
        line = line.strip()
        ##abbr[line] = True    
    fileabbr.close()
   
    rawfile = open(sys.argv[1],"r")
    resultfile = open(sys.argv[3],"w")
    X = int(sys.argv[2])%80
    count = 0

    is_train_data = sys.argv[1].find("train") != -1
    while count <= 800000+X*10000+9999:
        line = rawfile.readline()
        if not line:
            break
        if (not is_train_data or (count >= X*10000 and count <= X*10000+9999) \
              or (count >= 800000+X*10000)):
            m = re.match(r'"(\d)"(,[^,]+){4},"(.+)"',line)
            if not m:
                print 'format error: ' + line + count
                exit(0)
            polarity = m.group(1)
            twtt = twtt1(m.group(3))
            twtt = twtt2(twtt)
            twtt = twtt3(twtt)
            twtt = twtt4(twtt)
            twtt = twtt5(twtt)
            twtt = twtt7(twtt)
            twtt = twtt8(twtt)
            print >>resultfile, twtt9(polarity, twtt)
        count+=1
         
    resultfile.close()
    rawfile.close()
