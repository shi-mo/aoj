#!/bin/sh

set -u

NUM_SETS="0 1 100 10000"

for N in ${NUM_SETS}; do
    ruby sub_gen_sets.rb ${N} "_1_sets_${N}"
done
