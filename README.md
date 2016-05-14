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


TODO

Bugs:

Api in the host and port parameters in request.php are vulnerable to sql injection.

Temp Fix: Setup ip filtering to api directory using .htaccess

Make sure that your web directory is not writeable set permission 550
on your www-data folder so avoid server compromise through sql injection flaw.

I am currently looking for a developer to fix sql injection and apply proper sanitation and contributions would be much appreciated.


