#!/bin/sh
OLDNAME=$(i3-msg -t get_workspaces | jq -r '.[] | select(.focused==true).name')
WORKSPACE=$(echo $OLDNAME |cut -d':' -f1)
NEWNAME=$(dmenu -p "New name: " <&-)
i3-msg "rename workspace to \"$WORKSPACE:$NEWNAME\""
