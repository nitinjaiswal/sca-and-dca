# Deployment guide

## System Dependencies
- Pyhton 2.x

## Deployment

The directory `sca` and `dca` needs to be copied and paste on the system.These directories has three main files.

- **sca/sca.py**: This is the main file for the static code analyser.
- - **sca/requirements.txt**: This file contains requirements required by the sca.py
- **dca/dca.py**: This the main file for the dynamic code analyser.
- **dca/requirements.txt**: This file contains requirements required by the dca.py
- **dca/dca_timetravel.py**: This file is required for implementing time travelling debugging.

Copy and paste the file at `dca/dca_timetravel.py` at `python2x/lib`


### Directory Structure
```
    -|/sca/
           -|/requirements.txt
           -|/sca.py
    -|/dca/
            -|/dca.py
            -|/dca_timetravel.py
            -|/requirements.txt
```

## 3rd Party Libraries Used

- lizard
- watchdog
- pyYAML
- argh
- pathtools
- plyj
- slimit

## Installation of 3rd Party Libraries
- Open terminal in `../sca`
- Run command `pip install -r requirements.txt`
- open terminal in `../dca`
- Run command `pip install -r requirements.txt`