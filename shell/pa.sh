#! /bin/bash

set -u
trap exit ERR

ping -c 1 -W 1 ${ip} && arp -a ${ip} >> arp.log
