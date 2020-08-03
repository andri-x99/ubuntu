#!/bin/bash

echo "input the name of process you want to terminate"
read x
#pidof $x (berlaku firefox, tetapi chrome tidak)
ps -ef | grep $x

echo "input the top of pid"
read y

kill -9 $y

#https://www.commandlinefu.com/commands/matching/kill/a2lsbA==/sort-by-votes/25/50
#https://www.youtube.com/watch?v=9MOxb4DPEZk
