#!/usr/bin/env python
import time
import os
def measure_time(script="", init_script="", prerun_script="", postrun_script="", final_script="", iteration=20):
    if len(init_script) > 0:
        os.system(init_script)
    
    i = 0
    timestamps = []
    while i < iteration:
        if len(prerun_script) > 0:
            os.system(prerun_script)

        start_time = time.time()
        os.system(script)
        end_time = time.time()
        timestamps.append(end_time - start_time)

        if len(postrun_script) > 0:
            os.system(postrun_script)
        i += 1
    timestamp = sum(timestamps) / float(len(timestamps))

    if len(final_script) > 0:
        os.system(final_script)

    return timestamp


print("GCC - Compile time (second): " + str(measure_time(script="./compile_gcc.sh", prerun_script="make clean")))
print("RVPC - Compile time (second): " + str(measure_time(script="./compile_rvpc.sh", prerun_script="make clean")))
print("--------------")
print("GCC - Execution time (second): " + str(measure_time(script="./run_gcc.sh", init_script="./compile_gcc.sh", final_script="make clean")))
print("RVPC - tracing to /dev/null - Execution time (second): " + str(measure_time(script="./run_rvpc_no_trace", init_script="./compile_rvpc.sh", final_script="make clean")))
print("RVPC - tracing to ./trace   - Execution time (second): " + str(measure_time(script="./run_rvpc_trace", init_script="./compile_rvpc.sh", prerun_script="rm ./trace", final_script="make clean")))

