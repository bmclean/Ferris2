"""
This file is used to configure application settings

Settings is just a dictionary that is loaded and made available to your
application via the settings api.

You can use the settings API via:

    from ferris import settings

    mysettings = settings.get("mysettings")

The settings API will load the "settings" dictionary from this file. Anything else
will be ignored.

Optionally, you may enable the dynamic settings plugin at the bottom of this file.
"""

settings = {}

settings['timezone'] = {
    'local': 'US/Eastern'
}

settings['email'] = {
    # Configures what address is in the sender field by default.
    'sender': None
}

settings['app_config'] = {
    'webapp2_extras.sessions': {
        # WebApp2 encrypted cookie key
        # You can use a UUID generator like http://www.famkruithof.net/uuid/uuidgen
        'secret_key': '9a788030-837b-11e1-b0c4-0800200c9a66',
    }
}

settings['oauth2'] = {
    # OAuth2 Configuration should be generated from
    # https://code.google.com/apis/console
    'client_id': None,  # XXXXXXXXXXXXXXX.apps.googleusercontent.com
    'client_secret': None
}

# Enables or disables app stats.
# NOTE: This must also be enabled in app.yaml.
settings['appstats'] = {
    'enabled': False,
    'enabled_live': False
}


# Optionally, you may use the settings plugin to dynamically
# configure your settings via the admin interface
from plugins.settings import activate
activate(settings)
