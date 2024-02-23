# pi-robot

# Setup
## SSH Pi
`ssh {username}@{hostname}`

You might need to provide that user password.

## Check Cricket Board

`i2cdetect -y 1`
```sh
$ i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- 49 -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- -- 
```

Issue the following commands once you were able to verify the above:
```bash
sudo apt update
sudo apt upgrade
sudo apt autoremove
sudo reboot
```

## Install Libraries
```bash
python3 -m venv ~/pyenv
~/pyenv/bin/pip install adafruit-circuitpython-crickit
```

## Activate Python Environment
```bash
echo "alias activate='source ~/pyenv/bin/activate'" >> ~/.bashrc
~/pyenv/bin/python
```

## Test Color Change
```bash
>>> from adafruit_crickit import crickit
>>> crickit.onboard_pixel.fill(0xFF0000)
```

# Running
## Activating Environment After Setup

`activate`
`python`
