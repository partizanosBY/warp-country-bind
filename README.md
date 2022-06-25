# warp-country-bind

Python script for crontab to bind the connection in a specific country (PL), because in my country warp can randomly connect to Hungary, Poland, Lithuania, Russia, Finland

* */6 * * * python3 /usr/bin/warp-country-bind.py >/dev/null 2>&1
