# masscan-api-plugin

Step 1:

Run setup.sh on your webserver.
This script will create a user called demo with the password: demo
It will also create a database called masscan_api and then assign privledges to demo user.

Step 2:

Copy api folder to your web directory then set correct permissions on web server.

chmod 500 /var/www/html/api
chown www-data /var/www/html/api

Step 3:

Adjust client "config.cfg" file to suite your configuration.
