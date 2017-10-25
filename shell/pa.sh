#! /bin/bash

set -u
trap exit ERR

ip=192.168.0.$1

ping -c 1 -W 1 ${ip} && arp -a ${ip} >> arp.log
