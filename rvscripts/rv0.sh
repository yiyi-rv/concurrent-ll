#!/bin/bash

out_dir="./out/data";
cores="all";
duration="2000";

[ -d "$out_dir" ] || mkdir -p $out_dir;

# settings

initials="27";
updates="11";

for initial in $initials; 
do
    echo "rv0:* -i$initial";

    range=$((2*$initial));

    for update in $updates;
    do
	echo "rv0:** -u$update";

        out="$out_dir/ll.i$initial.u$update.dat";
#        ./scripts/scalability2.sh "$cores" \
 #           ./out/test-lock ./out/test-lockfree \
  #          -d$duration -i$initial -r$range -u$update | tee $out;
        ./scripts/scalability2.sh "$cores" \
            ./out/test-lock ./out/test-lockfree \
            -d$duration -i$initial -r$range -u$update 
    done
done
