#! /usr/bin/python

#  Copyright 2013 Linaro Limited
#  Author Matt Hart <matthew.hart@linaro.org>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import logging
from subprocess import call
from lavapdu.drivers.localbase import LocalBase


class FPanelCtl(LocalBase):

    @classmethod
    def accepts(cls, drivername):
        if drivername == "fpanelctl":
            return True
        return False

    def _port_interaction(self, command, port_number):
        if port_number < 1 or port_number > 4:
            logging.debug("Port number out of range!")
            return
 
        if command == "on":
            print("Attempting local commandline ON control: %s port: %i" % (command, port_number))
            # replace the call arguments below with your command line for the ON and OFF commands
            call(["fpanelctl", "-d", "1", str(port_number)])

        elif command == "off":
            print("Attempting local commandline OFF control: %s port: %i" % (command, port_number))
            call(["fpanelctl", "-d", "5", str(port_number)])

        else:
            logging.debug("Unknown command!")

