# Sneaze
Random Coughing, Wheezing, Sneezing, Throat-clearing noises on a Raspberry Pi (or similar Linux systems)

## Setup

(On a Raspberry Pi under Raspbian with the default user pi that also has sudo rights to install a systemd service)

* Clone/download the project

As user pi:

    mkdir ~/sounds/sneaze
    # copy the WAV files to the directory (feel free to add your own)
    mkdir ~/sounds/temp
    mkdir ~/bin # if it doesn't exist
    cp sneaze.py ~/bin/ 
    chmod o+x ~/bin/sneaze.py
    sudo cp sneaze.service /etc/systemd/system/
    sudo systemctl enable sneaze.service
    sudo systemctl start sneaze.service

If either of the files "\~/muted" or "\~/radio_is_on" exist, output is muted and random timer starts anew.