#!/bin/sh

CRONDTEXT=$(echo "*/5 * * * * $(whoami) $(pwd)/update.py > $(pwd)/update.log")
sudo /bin/sh -c "echo '$CRONDTEXT' > /etc/cron.d/namecheap-update"
