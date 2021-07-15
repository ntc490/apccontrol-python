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
    """POD (Plain Old Data) class + a little bit of smarts"""
    def __init__(self, filename):
        """Must have a filename. All other fields start off as None except
        aliases, which starts as an empty dictionary

        """
        self.filename = filename
        self.hostname = None
        self.user = None
        self.password = None
        self.last_port = None
        self.description = None
        self.aliases = {}

    def read(self):
        "Read config file from disk, decode yaml and populate fields"
        pass

    def write(self):
        "Write POD to config file in yaml format"
        pass

    def set_alias(self, num, name):
        "Add or overwrite a port alias"
        pass

    def rm_alias(self, name):
        """Remove a port alias.  Return True if we removed an existing alias,
        or False if nothing by that name was found.

        """
        for num in self.aliases:
            if self.aliases[num] == name:
                del self.aliases[num]
                return True
        return False


class Apc(object):
    def __init__(self, host=None, user=None, password=None, map=None):
        self.host = host or "apc"
        self.user = user or "apc"
        self.password = password or "apc"
        self.port_map = map or {}
        self.last_port = None

    def set_map(self, map):
        """Set port alias map by passing in a dictionary with number is key,
        and alias as value.

        """
        self.port_map = map

    def port_name(num):
        """Return port name/alias associated with port number.  Return
        'Unknown' if not found.

        """
        return self.port_map.get(num, 'Unknown')

    def port_num(name):
        """Return port number associated with port alias 'name'.  Return -1 if
        not found.

        """
        for num in self.port_map:
            if self.port_map[num] == name:
                return num
        return -1

    def on(self, port):
        pass

    def off(self, port):
        pass

    def reset(self, port):
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
