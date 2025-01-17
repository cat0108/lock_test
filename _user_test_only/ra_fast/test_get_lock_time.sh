#!/bin/bash
echo > /sys/kernel/tracing/trace
echo 1 > /sys/kernel/tracing/events/cat/enable
./set_cgroup_128m.sh
cat /sys/kernel/tracing/trace > ./trace.txt
echo 0 > /sys/kernel/tracing/events/cat/enable
