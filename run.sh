#!/bin/bash
source $HOME/.profile
PID=$(pgrep gnome-session)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)
foo="$(/home/lgbouma/Software/anaconda/bin/python /home/lgbouma/Dropbox/apod_desktop/get_apod.py)"
$foo
