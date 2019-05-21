#!/bin/bash

sudo mongod --shardsvr --port 27004 --dbpath /var/lib/mongodb4 --replSet rs1 &
sleep 2
sudo mongod --shardsvr --port 27005 --dbpath /var/lib/mongodb5 --replSet rs1 &
sleep 2
sudo mongod --shardsvr --port 27006 --dbpath /var/lib/mongodb6 --replSet rs1 &
sleep 2

