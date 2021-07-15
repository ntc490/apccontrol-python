#!/usr/bin/env python3
"""apc.py - Control APC network power strip

Usage:
  apc.py [options] (on [<port>] | off [<port>] | reset [<port>] | list)
  apc.py [options] set-alias <name> <num>
  apc.py [options] rm-alias <name>
  apc.py [options] set-host <hostname>
  apc.py --help

Commands:
  on                     Turn port on [defaults to last port if empty]
  off                    Turn port off [default to last port if empty]
  reset                  Reset port [default to last port if empty]
  list                   List all ports, their aliases, and their status
  set-alias              Set an alias for a port number
  rm-alias               Remove alias for a port
  set-host               Set host of APC device via IP address or hostname
  --help                 Print this usage screen

Options:
  --config <filename>    Point to custom config file [default: ~/.config/apc/config]

"""
import sys
import docopt


def main():
    args = docopt.docopt(__doc__)
    print(args) # TODO: remove this line - initial debug ONLY
    config = ConfigFile(args['--config'])
    error = run_command(args, config)
    sys.exit(error)
    

# --------------- Classes ---------------

class ConfigFile(object):
    def __init__(self, filename):
        self.filename = filename

    def read():
        pass

    def port_name(port_num):
        pass

    def port_num(port_name):
        pass

# --------------- Command Handlers ---------------

def on_command(args, config):
    pass

def off_command(args, config):
    pass

def reset_command(args, config):
    pass

def list_command(args, config):
    pass

def set_alias_command(args, config):
    pass

def rm_alias_command(args, config):
    pass

def set_host_command(args, config):
    pass

def run_command(args, config):
    pass

if __name__ == "__main__":
    main()
