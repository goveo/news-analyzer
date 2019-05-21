#!/bin/bash

startport=27001
endport=27013
mongosport=27100

let i=startport END=endport
while ((i<=END)); do
    echo sudo fuser -k -n tcp $i
    sudo fuser -k -n tcp $i
    let i++
done
echo sudo fuser -k -n tcp $mongosport
sudo fuser -k -n tcp $mongosport

echo killed