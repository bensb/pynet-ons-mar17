#!/usr/bin/env python

from pprint import pprint

f = open("show_ip_bgp.txt")
bgp_output = f.read()

header, bgp_table = bgp_output.split("Weight Path")
#bgp_table = bgp_table.strip()

for line in bgp_table.split("\n"):
    fields = line.split()
    if fields:
        prefix = fields[1]
        as_path = fields[5:-1]
        as_path = " ".join(as_path)
        print "{}:  {}".format(prefix, as_path)
#        print prefix
#        print as_path

