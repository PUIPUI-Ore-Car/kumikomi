#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyudev
import subprocess
import time

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')
monitor.start()

bind_flag = False


for device in iter(monitor.poll, None):
    if(device.action == "bind"):
        if(bind_flag == False):
            time.sleep(2)
            cmd = "/home/pi/kumikomi/USB_mount/mount.sh"
            res = subprocess.call(cmd)
            bind_flag = True

    if(device.action == "unbind"):
        if(bind_flag == True):
            cmd = "/home/pi/kumikomi/USB_mount/umount.sh"
            res = subprocess.call(cmd)
            bind_flag = False