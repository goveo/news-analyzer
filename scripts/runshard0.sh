#!/bin/bash

sudo mongod --shardsvr --port 27001 --dbpath /var/lib/mongodb1 --replSet rs0 &
sleep 2
sudo mongod --shardsvr --port 27002 --dbpath /var/lib/mongodb2 --replSet rs0 &
sleep 2
sudo mongod --shardsvr --port 27003 --dbpath /var/lib/mongodb3 --replSet rs0 &
sleep 2
