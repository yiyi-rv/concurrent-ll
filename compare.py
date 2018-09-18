#!/usr/bin/env python3
import time
import os
import subprocess
def measure_time(script="", init_script="", prerun_script="", postrun_script="", final_script="", iteration=20):
    if len(init_script) > 0:
        subprocess.call(init_script, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    i = 0
    timestamps = []
    while i < iteration:
        if len(prerun_script) > 0:
            subprocess.call(prerun_script, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        start_time = time.time()
        subprocess.call(script, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        end_time = time.time()
        timestamps.append(end_time - start_time)

        if len(postrun_script) > 0:
            subprocess.call(postrun_script, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        i += 1
    timestamp = sum(timestamps) / float(len(timestamps))

    if len(final_script) > 0:
        subprocess.call(final_script, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return timestamp

print("Performance measurement - 20 iterations")
print("GCC - Compile time (second/iter): " + str(measure_time(script="./compile_gcc.sh", postrun_script=["make", "clean"])))
print("RVPC - Compile time (second/iter): " + str(measure_time(script="./compile_rvpc.sh", postrun_script=["make", "clean"])))
print("--------------")
print("GCC - Execution time (second/iter): " + str(measure_time(script="./run_gcc.sh", init_script="./compile_gcc.sh", final_script=["make", "clean"])))
print("RVPC - no analysis, tracing to /dev/null - Execution time (second/iter): " + str(measure_time(script="./run_rvpc_no_trace.sh", init_script="./compile_rvpc.sh", final_script=["make", "clean"])))
print("RVPC - no analysis, tracing to ./trace   - Execution time (second/iter): " + str(measure_time(script="./run_rvpc_trace.sh", init_script="./compile_rvpc.sh", prerun_script="rm ./trace", final_script=["make", "clean"])))

