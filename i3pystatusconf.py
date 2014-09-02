import subprocess

from i3pystatus import Status

status = Status(standalone=True)

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
status.register("clock",
    format="%a %-d %Y %b %X",)

# Displays the weather like this:
#
status.register("weather",
    location_code="ASXX0043:1",
    format="GEELONG {current_temp}",
    interval=60)
status.register("weather",
    location_code="ASXX0075:1",
    format="MELBOURNE {current_temp}",
    interval=60)

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
status.register("load")

# Shows your CPU temperature, if you have a Intel CPU
status.register("temp",
    format="CPU TEMP {temp:.0f}°C",)

# Displays whether a DHCP client is running
status.register("runwatch",
    name="DHCP",
    path="/var/run/dhclient*.pid",)

# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces
status.register("network",
    interface="eno1",
    format_up="{v4cidr}",)

# Has all the options of the normal network and adds some wireless specific things
# like quality and network names.
#
# Note: requires both netifaces and basiciw
status.register("wireless",
    interface="wlp1s0",
    format_up="{essid} {quality:03.0f}% {v4}",)

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk",
    path="/",
    format="{avail}G",)

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
status.register("pulseaudio",
    format="♪ {volume}",)

# all my custom buttons
status.register("text",
    text="New Comic",
    cmd_leftclick="/home/benkaiser/.i3/update_background",
    color="#44bbff")

status.register("text",
    text="Sleep Screen",
    cmd_leftclick="sleep 1; xset dpms force off",
    color="#44bbff")

status.register("text",
    text="Suspend System",
    cmd_leftclick="systemctl suspend",
    color="#44bbff")

status.register("text",
    text="Screensaver",
    cmd_leftclick="xscreensaver-command -activate",
    color="#44bbff")

status.run()
