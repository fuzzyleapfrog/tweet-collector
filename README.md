# The Tweet Collector
Tweet collector allows you to collect specific tweets of specific users.

# Create your own Tweet Collector
- You first have to create your own `tweet-collector.cfg` based on the example config to get the script running. Move your `tweet-collector.cfg` to `/etc`.
- In a second step, create the database using `create_database.sql` with the variables set in `tweet-collector.cfg`.
- For Apache2, there is an example configuration in in `tweet-collector.conf`. Modify and move the Apache configuration to Apache directory `sites-available` and create symlink in Apache directory `sites-enabled`.

# Framework
- The database is MariaDB.
- Uses Apache2 and WSGI. 
- Uses jinja2 for creating HTML.
- Uses Javascript. Set link to Javascripts of Tweet Collector located in folder `tweet-collector/js` in your Apache2 configuration to variable `DocumentRoot`. 


