#!/bin/sh

cd ~/.wallpapers

while test $DISPLAY; do
	feh -z --bg-scale wallpaper.jpg
	convert $(python wallpaper_scraper.py) $HOME/.wallpapers/wallpaper.jpg
	rm -rf wallpaper.png &
	sleep 5m
done
