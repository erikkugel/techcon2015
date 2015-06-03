#!/bin/bash

service elasticsearch start
sleep 5

service logstash start
sleep 5

service logstash-forwarder start
sleep 5

su - techcon -c "cd /opt/problem3; python bin/problem3.py & echo $! > /tmp/problem3.pid"

while [ 1 ]; do wget -q -O - http://ubuntu:8080/ ; sleep 3; date; done
