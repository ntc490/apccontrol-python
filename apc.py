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
import os
import sys
import yaml
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
        self.filename = os.path.expanduser(filename)
        self.hostname = None
        self.user = None
        self.password = None
        self.last_port = None
        self.description = None
        self.aliases = {}
        self.descriptions = {}
        self.__data = None

    def read(self):
        "Read config file from disk, decode yaml and populate fields"
        with open(self.filename, 'r') as handle:
            self.__data = yaml.load(handle)
            self.hostname = self.__data['hostname']
            self.user = self.__data['user']
            # TODO: prompt user for password if one doesn't exist?  At
            # least handle scenario where password does not exist.
            self.password = self.__data.get('password') or "apc"
            self.last_port = self.__data['last_port']
            self.description = self.__data['description']
            self.aliases = self._create_aliases(self.__data['aliases'])
            self.descriptions = self._create_descriptions(self.__data['aliases'])

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

    def _create_aliases(self, yaml_list):
        """Turn list of dictionaries into a dictionary with the port number and alias
        """
        alias_dict = {}
        for entry in yaml_list:
            num = entry['port']
            name = entry['name']
            alias_dict[num] = name
        return alias_dict

    def _create_descriptions(self, yaml_list):
        """Turn list of dictionaries into a dictionary with the port number and description
        """
        description_dict = {}
        for entry in yaml_list:
            num = entry['port']
            description = entry['description']
            description_dict[num] = description
        return description_dict

    def __str__(self):
        descr = f"""{{filename: '{self.filename}', \
hostname: '{self.hostname}', \
user: '{self.user}', \
password: '{self.password}', \
last_port: '{self.last_port}', \
description: '{self.description}', \
aliases: {{"""

        secondary_port = False
        for port in self.aliases:
            if secondary_port:
                descr += ", "
            secondary_port = True
            descr += f"{port}: '{self.aliases[port]}'"

        descr += "}, descriptions: {"
        secondary_port = False
        for port in self.descriptions:
            if secondary_port:
                descr += ", "
            secondary_port = True
            descr += f"{port}: '{self.descriptions[port]}'"
        descr += "}}"
        return descr

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
    print("on command")
    config.read()
    print(config)

def off_command(args, config):
    print("off command")

def reset_command(args, config):
    print("reset command")

def list_command(args, config):
    print("list command")

def set_alias_command(args, config):
    print("set alias command")

def rm_alias_command(args, config):
    print("rm alias command")

def set_host_command(args, config):
    print("set host command")

def run_command(args, config):
    """Find function pointer for command name and call it with args and
    config file object.  Return error code from the function, or -1 if the 

    """
    commands = { 'on': on_command,
                 'off': off_command,
                 'reset': reset_command,
                 'list': list_command,
                 'set-alias': set_alias_command,
                 'rm-alias': rm_alias_command,
                 'set-host': set_host_command,
    }
    for command in commands:
        if not command in args:
            raise ValueError('Invalid command key %s' % command)
        if args[command]:
            return commands[command](args, config)
    raise ValueError('Must pass in at least one True command')

if __name__ == "__main__":
    main()
