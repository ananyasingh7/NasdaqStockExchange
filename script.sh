#!/bin/bash          

totalTime=0

if [ -e tagsoup-1.2.1.jar ]
then
    while [ $totalTime -lt 61 ]
    do
        now=$(date +"%m-%d-%Y-%H-%M-%S")
        touch $now.html
        wget -O - http://wsj.com/mdc/public/page/2_3021-activnnm-actives.html >> $now
        java -jar tagsoup-1.2.1.jar --files $now
        rm $now.html
        totalTime=$((totalTime+1))
        python3 xhtmlToCsv.py "$now.xhtml" 
        sleep 60
    done
else
    wget -O - http://vrici.lojban.org/~cowan/XML/tagsoup/tagsoup-1.2.1.jar >> tagsoup-1.2.1.jar
    while [ $totalTime -lt 61 ]
    do
        now=$(date +"%m-%d-%Y-%H-%M-%S")
        touch $now.html
        wget -O - http://wsj.com/mdc/public/page/2_3021-activnnm-actives.html >> $now
        java -jar tagsoup-1.2.1.jar --files $now
        rm $now.html
        totalTime=$((totalTime+1))
        python3 xhtmlToCsv.py "$now.xhtml" 
        sleep 60
    done
fi
