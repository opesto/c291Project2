#!/bin/bash

#remove tweets.idx, dates.idx and terms.idx; otherwise we just append
rm tw.idx da.idx te.idx > /dev/null #pipe to null
# sort/read      per line    replace blah: with blah\n  replace : with something that looks like :
#                                                                       load with db_load    output to tw.idx
sort -u tweets.txt | perl -lpe 's/^([^:]*):/$1\n/g;' -lpe 's/\\/&92;/g' | db_load -c duplicates=1 -T -t hash tw.idx
sort -u dates.txt | perl -lpe 's/^([^:]*):/$1\n/g;' -lpe 's/\\/&92;/g' | db_load -c duplicates=1 -T -t btree da.idx
sort -u terms.txt | perl -lpe 's/^([^:]*):/$1\n/g;' -lpe 's/\\/&92;/g' | db_load -c duplicates=1 -T -t btree te.idx
