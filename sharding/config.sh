#!/bin/bash

sudo mongod --configsvr --port 27011 --dbpath /var/lib/mongodb7 --replSet configReplSet &
sleep 2
sudo mongod --configsvr --port 27012 --dbpath /var/lib/mongodb8 --replSet configReplSet &
sleep 2
sudo mongod --configsvr --port 27013 --dbpath /var/lib/mongodb9 --replSet configReplSet &
sleep 2
sudo mongos --configdb configReplSet/localhost:27011,localhost:27012,localhost:27013 --port 27100
