#!/bin/bash
for fs in examples/*.fs; do
    echo "loading fs: $fs"
    pcap_file="$(basename $fs .fs).pcap"
    echo $pcap_file
    flowsynth "$fs" -f pcap -w "pcaps/$pcap_file"
done