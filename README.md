microsoft-dynamics-auth
===========

Microsoft Dynamics 365 oauth2 plugin for `HTTPie <https://httpie.org/>`_.


Installation
------------

    $ pip install httpie-msft-dynamics-auth


You should now see ``dynamics-auth`` under ``--auth-type`` in ``$ http --help`` output.

To be able to execute requests you must export a few shell variables. Copy and rename the sample msft-dynamics.sh.sample to msft-dynamics.sh
and modify the values as required and run the following

    $ source msft-dynamics.sh

Usage
-----

    $ http --auth-type=msft-dynamics --auth='client-key:client-secret' https://your-org-name.your-crm-region.dynamics.com/api/data/v9.0


You can also use `HTTPie sessions <https://httpie.org/doc#sessions>`_:

    # Create session
    $ http --session=logged-in --auth-type=msft-dynamics --auth='client-key:client-secret' your-org-name.your-crm-region.dynamics.com

    # Re-use auth
    $ http --session=logged-in POST your-org-name.your-crm-region.dynamics.com hello=world

