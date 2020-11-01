microsoft-dynamics-auth
===========

Microsoft Power Platform auth plugin for [HTTPie](https://httpie.org/)

## Installation

    $ pip install microsoft-dynamics-auth

Verify that you see `msft-power-platform` under `--auth-type` by running

    $ http --help

## Configuration

To be able to execute requests you must setup the credentials for the target power platform environment. This auth plugin requires a clientid and secret for an app registerd in Active Directory. You must register an app in Active Directory and add it as an application user in the target power platform environment. Once you have the app configured in both AAD and Power Platform.

Use `env-generator.py` included in this repository to generate the credentials file `.parc` in user home directory.

    $ python env-generator.py

This will generate a ~/.parc file to store power platform environment credentials. Paste credentials in the following format after the prompt and then press enter")

    name: [SECTION_NAME] tenant: [TENANT] key: [CLIENT-ID] secret: [CLIENT-SECRET] resource: [ENVIRONMENT-URL]\n")

For example

    name: dev-contoso tenant: contoso.onmicrosoft.com key: highlyconfenditialkey secret: highlyconfidentialsecret resource: https://dev-contoso.crm.dynamics.com")

You can also manually create the `~/.parc` in the following format

    [default]
    tenant = contoso.onmicrosoft.com
    key = 52a44848-095e-4882-a880-e8b8083714d8a
    secret = highly-confidential-secret
    resource = https://dev-contoso.crm.dynamics.com

    [dev-contoso1]
    tenant = contoso.onmicrosoft.com
    key = 52a44848-095e-4882-a880-e8b8083714d8a
    secret = highly-confidential-secret
    resource = https://dev-contoso1.crm.dynamics.com

    [dev-northwind]
    tenant = northwind.onmicrosoft.com
    key = f4d9f805-a172-4698-9228-518013cd04c5
    secret = highly-confidential-secret
    resource = https://dev-northwind.crm.dynamics.com

## Usage

    $ http --auth-type=msft-power-platform --auth='client-key:client-secret' https://your-org-name.your-crm-region.dynamics.com/api/data/v9.0

Use [HTTPie sessions](https://httpie.org/doc#sessions>)

### Create session

    $ http --session=logged-in --auth-type=msft-dynamics --auth='client-key:client-secret' your-org-name.your-crm-region.dynamics.com

### Re-use auth

    $ http --session=logged-in POST your-org-name.your-crm-region.dynamics.com hello=world
