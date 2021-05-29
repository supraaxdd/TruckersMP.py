# TruckersMP.py

This repository hosts the code of the TruckersMP API Wrapper, written in Python.
* Most of the API endpoints available are able to be called via a function

# Table of contents

- [Installation and setup](https://github.com/supraaxdd/truckersmp-api/#installation-and-setup)
- [Usage](https://github.com/supraaxdd/truckersmp-api/#usage)
- [Support](https://github.com/supraaxdd/truckersmp-api/#support)
- [Contributing](https://github.com/supraaxdd/truckersmp-api/#contributing)
- [Acknowledgements](https://github.com/supraaxdd/truckersmp-api/#acknowledgements)

## Installation and setup

**This module is compatible with Python v3+**

You can install this module via github or PyPI:
```bash
$ pip install git+https://github.com/supraaxdd/truckersmp-api.git
```

```bash
$ pip install truckersmp-api
```
## Usage

```py
from truckersmp import TruckersMP

truckersmp = TruckersMP()

# Returns the statuses of all servers.
print(truckersmp.get_servers())

# Fetches the information about the desired player.
print(truckersmp.get_player("id of player")) # Can be a string or integer

# Fetches the information about the desired VTC.
print(truckersmp.get_vtc("id of vtc")) # Can be a string or integer

# Fetches any bans on the desired player's account.
print(truckersmp.get_bans("id of player")) # Can be a string or integer

```

Available Methods:

```py
get_player(playerID)                # Fetches Player data
get_bans(playerID)                  # Fetches any bans for a given player
get_servers()                       # Fetches information about servers
get_in_game_time()                  # Fetches current in-game time which is synced across all servers
get_version()                       # Fetches supported game version
get_events()                        # Fetches events from the index page in JSON format
get_event(eventID)                  # Fetches specific event using given eventID
get_vtc_index()                     # Fetches VTCs from the index page in JSON format
get_vtc(vtcID)                      # Fetches specific VTC data. Returns information such as roles, members, general information etc.
get_vtc_member(vtcID, memberID)     # Fetches a given member from the given VTC
get_vtc_event(vtcID, eventID)       # Fetches a given event from the given VTC
get_rules()                         # Fetches all the rules in JSON format
```

## Support

If you need help with anything, you should preferably contact Supra#6561 or Blinkzy#3819 on discord. If that is not possible, feel free to open a new issue. Note that if the issue is invalid, it may be closed.

## Contributing

1. Feel free to Fork & Clone the repository and make sure that it is on the __master branch__ as that branch is the most up to date one and the most stable.
2. Run `npm install` in the project folder.
3. Make the changes that you want to propose and code whatever you want!
4. Make sure that everything is good shape and then feel free to create a [Pull Request](https://github.com/supraaxdd/truckersmp-api/compare) which will be reviewed.

## Acknowledgements

Main Contributors: supraaxdd & ItzBlinkzy
