#!/usr/bin/env python3
from subprocess import Popen, PIPE


TARGET_FILE = "linux-2.6.0.tar.xz"
TARGET_LINK = "http://www.kernel.org/pub/linux/kernel/v2.6/%s" % TARGET_FILE

with Popen(["wget", TARGET_LINK], stdout=PIPE, bufsize=1, universal_newlines=True) as p:
    print("".join(p.stdout))
