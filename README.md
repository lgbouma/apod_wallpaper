# Auto-update your desktop wallpaper to APOD!

So this should work on any bash-shell running system with Python
installed. Obviously this works for any site with images, but you
can't go wrong with APOD.
I've only tested it on `ubuntu 15.04`. If you try it and
it breaks, let me know!

## Installation instructions
Clone this repository to a local directory on your computer.

### Modify `run.sh`
In `run.sh`, be sure to source whatever your relevant shell login profile is for the
`source` call. 

Modify what I put in as absolute paths to whatever is appropriate on your system.

In the python call, make sure to use the absolute path of your python installation.

The real trick in this is getting cron the correct environment variables. To set a desktop
background in gnome with `gsettings`, that variable is `DBUS_SESSION_BUS_ADDRESS`. See the
relevant [stack exchange
description](http://askubuntu.com/questions/140305/cron-not-able-to-succesfully-change-background).

### Modify absolute paths in `get_apod.py`
This script does the bulk lifting, downloading the image and writing out the caption
in a text file to your desktop.
It outputs a `gsettings` command that with appropriate nudging, `run.sh` executes.

### Run permissions
`chmod +x` both the python and the shell scripts.

### cron to run at fixed time:
Your cron file (`crontab -e`) should include:
```
SHELL=/bin/bash
13 2 * * * /home/lgbouma/Dropbox/apod_wallpaper/run.sh
```
where the time is whenever every 24 hours you want the freshest new astronomy
pictures on the block!

