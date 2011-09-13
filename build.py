#!/usr/bin/env python
import os
import optparse
from subprocess import check_call
import codecs

def main():
    p = optparse.OptionParser(usage='%prog [options] slides-source.txt')
    (options, args) = p.parse_args()
    if len(args) != 1:
        p.error('Incorrect args')
    source = args[0]
    output = '%s.html' % os.path.splitext(source)[0]
    check_call(['./custom_rst2s5.py', source, output])
    print "Wrote %s" % output

if __name__ == '__main__':
    main()
