#!/bin/bash
export RVP_TRACE_ONLY=yes         # Disable analysis
export RVP_TRACE_FILE=/dev/null   # Tracing to /dev/null
./scripts/test_correctness.sh
