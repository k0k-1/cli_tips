#! /bin/bash

set -u
trap exit ERR

if [ -f arp.log ]
then
  rm arp.log
fi

for i in `seq 0 255`
do
  bash pa.sh ${i} &
done
