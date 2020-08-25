#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 19:40:06 2020

@author: venky
"""
# Python Script to update all PIP packages
from subprocess import Popen, PIPE

def runCommand(command):
    with Popen(command, stdout=PIPE, bufsize=1, shell=False, universal_newlines=True) as proc:
        lines = []
        for line in proc.stdout:
            print(line, end="")
            lines.append(line)
    return lines
        
banner = "-" * 80
print("Tekgar's Glitchy Scripts - Package Updater")
print(banner)

print("* Checking PIP for packages to update...")
cmd1 = ["pip3", "list", "-o", "--format=freeze"]
reqs = runCommand(cmd1)

print("* Getting things ready...")

packages = []
for line in reqs:
    packages.append(line.split("==")[0])

cmd2 = lambda index: ["pip3", "install", "-U", "--no-color", packages[index]]

pkgsNum = len(packages)

for i in range(pkgsNum):
    print(f"\n* Installing package {packages[i]} ({i + 1}/{pkgsNum})\n")
    runCommand(cmd2(i))