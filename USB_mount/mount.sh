#!/bin/sh

echo "raspberry" | sudo -S mount -o owner,uid=1001,gid=1001,utf8 UUID="5E4E-27F2" /media/share

exit 0