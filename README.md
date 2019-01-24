Graphene Healthchecker
======================

This role installs the graphene healthchecker from BLockchain B.V.

    https://github.com/blockchainbv/graphene-healthchecker

Requirements
------------

No requirements

Role Variables
--------------


Dependencies
------------

     # Linux user name that runs the healthchecks
     healthcheck__user: healthcheck

     # A unique instance name in case multiple healthcheckers are installed
     # at the same time
     healthcheck__instance: healthcheck

     # The service name that is used to install systemd service
     healthcheck__service: graphene-healthchecks-{{healthcheck__instance}}.service

     # Installation directory
     healthcheck__install_path: /home/{{healthcheck__user}}/healthcheck_{{healthcheck__instance}}/

     # Virtual Environment path
     healthcheck__install_env: /home/{{healthcheck__user}}/healthcheck_{{healthcheck__instance}}/env

     # UWSGI configuration file path
     healthcheck__path_to_wsgi: /home/{{healthcheck__user}}/healthcheck_{{healthcheck__instance}}/uwsg.ini

     # Listen to host
     healthcheck__listen_host: 0.0.0.0

     # List to port
     healthcheck__listen_port: 8080

     # Monitor this graphene backend (HTTP/HTTPS only! No websocket support!)
     healthcheck__witness_url: https://node.bitshares.eu

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - role: graphene-healthchecker
           healthcheck__witness_url: https://node.bitshares.eu

License
-------

MIT

Author Information
------------------

Blockchain B.V.
