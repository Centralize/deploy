#!/usr/bin/env python3

import subprocess
import os
import sys
import syslog


syslog.syslog('Deployment started.')

# Prepare apt and system.
os.system('apt update; apt upgrade -y')

mod = sys.argv[1]
if(sys.argv[1] is not None):
    subprocess.call(f"{mod}/run.py")
else:
    syslog.syslog(syslog.LOG_CRIT, "Fatal Error: Missing module.")

exit(0)