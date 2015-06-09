#!/bin/bash

echo "Start ElasticSearch"
service elasticsearch start
sleep 5

echo "Start Logstash server"
service logstash start
sleep 5

echo "Start Logstash Forwarder"
service logstash-forwarder start
sleep 5

echo "Start SNMP server"
service snmpd start 
sleep 5

echo "Start Problem #3 web app."
su - techcon -c "cd /opt/problem3; python bin/problem3.py &"
sleep 5

echo "Start loading Problem #3:"
while [ 1 ]; do wget -q -O - http://ubuntu:8080/ ; sleep 3; date; done
