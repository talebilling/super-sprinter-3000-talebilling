# super-sprinter-3000

1. edit the `connect_str.txt` (put your database name into it)
2. run this command (where the setup.py file is located):
`sudo pip3 install --editable .`
3. run:
`export FLASK_APP=sprinter`
4. run:
`export FLASK_DEBUG=true`
5. run to create the database:
`flask initdb`
6. start the application:
`flask run`

This should start the server & you can reach it from your browser:
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)
