#!/bin/bash

setxkbmap latam &
feh --bg-fill ~/wallpaper/wallpaper.png &
picom --no-vsync &

udiskie -t &
nm-applet &
volumeicon & 
cbatticon -u 5 &
