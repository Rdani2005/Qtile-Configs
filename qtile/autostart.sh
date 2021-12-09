#!/bin/bash
xrandr --output eDP1 --primary --mode 1366x768 --pos 0x312 --rotate normal --output DP1 --off --output DP2 --off --output HDMI1 --mode 1920x1080 --pos 1366x0 --rotate normal --output HDMI2 --off --output HDMI3 --off --output VGA1 --off --output VIRTUAL1 --off &
setxkbmap latam &

feh --bg-fill ~/wallpaper/wallpaper.jpeg &
picom &

volumeicon & 
cbatticon -u 5 &
