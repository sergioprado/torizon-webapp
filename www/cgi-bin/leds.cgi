#!/bin/sh

LED_RED="/sys/class/leds/led-0/brightness"
LED_GREEN="/sys/class/leds/led-1/brightness"
LED_BLUE="/sys/class/leds/led-2/brightness"

read CONTENT

case $CONTENT in
    "red=red-on")
        echo 1 > $LED_RED
	;;
    "red=red-off")
        echo 0 > $LED_RED
	;;
    "green=green-on")
        echo 1 > $LED_GREEN
	;;
    "green=green-off")
        echo 0 > $LED_GREEN
	;;
    "blue=blue-on")
        echo 1 > $LED_BLUE
	;;
    "blue=blue-off")
        echo 0 > $LED_BLUE
	;;
esac

echo -e 'Content-type: text/html\r\n'
echo -e '<html>'
echo -e '<META HTTP-EQUIV="refresh" CONTENT="0;URL=/index.html">'
echo -e '</html>'
