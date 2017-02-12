#!/bin/bash
for (( c=500; c<=10000; c=c+500 ))
do  
   echo "====$c"
   python selectetrain.py $c
   java -cp weka-3-8-1/weka.jar weka.classifiers.functions.SMO -t train_$c.arff  -T test.arff | grep "Weighted Avg"|tail -n 1 >> 3.2.out
done
