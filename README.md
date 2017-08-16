# swvx-cli
Digium Switchvox API cli testing tool 

## Description: 
swvx-cli is used to rapidly test Digium Switchvox api from command prompt shell.
This allows you to make quick API requests, and changes to your Digium Switchvox from the CLI.

Change the USERNAME, PASSWORD, and ADDRESS variables to fit your server setup.

Outputs to the cli are pretty printed. 

All requests are logged by default to swvx-cli.log located where ever you run the script from.
Logging by default is set to INFO, change it as needed.

## Usage:
Simply provide the API method you wish to use, followed by any parameters. Parameters should be wrapped in double quotes (")

    ./swvx-cli.py <api method> [parameters=value]
    e.g.: 
    ./swvx-cli.py switchvox.extensions.search
    ./swvx-cli.py switchvox.extensions.getInfo extensions=[899]

## Testing
Runing swvx-cli.py with no paramerters will by default execute the `switchvox.info.getList` method.

    ./swvx-cli.py
    {
        "method": "switchvox.info.getList",
        "result": {
            "info": {
                "phone_config_tokens": {
                    "used": "1",
                    "max_allowed": "40"
                },
                "peering": {
                    "last_compatible_peer_version": "[% last_compatible_peer_version %",
                    "version": "3"
                },
                "max_concurrent": {
                    "calls": "99"
                },
                "user_extensions": {
                    "used": "100",
                    "max_allowed": "100"
                },
                "software": {
                    "edition": "smb",
                    "version": "84996",
                    "version_display": "6.3.6"
                }
            }
        }
    }


## Use case
This script was created to help rapidly test API calls to Switchvox system. It does very little error checking and was designed to use as few addon modules as possible. 

## Feedback
Your feedback is welcome, please use the issue tracker to report a bug or issues you might have.
