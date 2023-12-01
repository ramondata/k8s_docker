#!/usr/bin/env python

print("hello kubernetes!")

import subprocess

d = subprocess.Popen('pwd', shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = d.communicate()

print(err) if out == b'' else print(out)

from datetime import datetime

hour_min = datetime.today().strftime("%HH-%MM")
print(hour_min)


