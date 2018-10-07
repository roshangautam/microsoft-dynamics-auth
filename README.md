microsoft-dynamics-auth
===========

Microsoft Dynamics 365 oauth2 plugin for [HTTPie](https://httpie.org/)


Installation
------------

    $ pip install microsoft-dynamics-auth


You should now see `dynamics-auth` under `--auth-type` while running

    $ http --help

To be able to execute requests you must export a few shell variables. Copy and rename the sample msft-dynamics.sh.sample to msft-dynamics.sh
and modify the values as required and run the following

    $ source msft-dynamics.sh

Usage
-----

    $ http --auth-type=msft-dynamics --auth='client-key:client-secret' https://your-org-name.your-crm-region.dynamics.com/api/data/v9.0


Use [HTTPie sessions](https://httpie.org/doc#sessions>)

#### Create session

    $ http --session=logged-in --auth-type=msft-dynamics --auth='client-key:client-secret' your-org-name.your-crm-region.dynamics.com

#### Re-use auth

    $ http --session=logged-in POST your-org-name.your-crm-region.dynamics.com hello=world

