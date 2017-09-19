There is a command-line utility `t` which uses the configuration file `$HOME/.trc` for saving api-keys different users and the default user. `tvitor` hijacks this file.

Creating a .trc file
--------------------

The credentials will live in a file named .trc in the home directory.

Copy and paste the template below (make sure you keep the indentation consistent) into that ~/.trc file, edit it accordingly; there are nine lines you need to change (they're in all-caps), make sure you've put the values specific to you in those fields or the authentication process won't work.

(it should go without saying that you don't want other people to look at this file)

```
    configuration:
    default_profile:
    - YOUR_USER_NAME
    - YOUR_CONSUMER_KEY
    profiles:
    YOUR_USER_NAME:
	YOUR_CONSUMER_KEY:
	username: YOUR_USER_NAME
	consumer_key: YOUR_CONSUMER_KEY
	consumer_secret: YOUR_CONSUMER_SECRET
	token: YOUR_ACCESS_TOKEN
	secret: YOUR_ACCESS_TOKEN_SECRET
```
