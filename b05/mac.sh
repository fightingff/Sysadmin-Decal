#!/bin/bash

mac_address=$(ip -a addr | grep -oP '(?<=link/ether )[a-fA-F0-9:]+')

if [ -z "$mac_address" ]; then
    echo "Error: Could not find the MAC address for ens3."
else
    echo "MAC Addresses:" 
    echo "${mac_address}"
fi
