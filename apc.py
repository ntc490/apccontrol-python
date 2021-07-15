#!/usr/bin/env python3
"""apc.py - Control APC network power strip

Usage:
  apc.py (on [<port>] | off [<port>] | reset [<port>] | list)
  apc.py list-aliases
  apc.py set-alias <name> <num>
  apc.py rm-alias <name>
  apc.py set-host <hostname>
  apc.py --help

Options:
  --help                              Print this usage screen

"""
import docopt


def main():
    args = docopt.docopt(__doc__)
    print(args)

if __name__ == "__main__":
    main()
