# cbbtime
Shitty back of the envelope way to count up how long I've been listening to Comedy Bang! Bang!

## Requirements
Requires python 3 and BeautifulSoup library

    $ pip install bs4

## Usage
  Without arguments gives you the runtime of all the episodes (i.e from episode 1 to the lastest)

    $ python cbbtime.py 
    you have listened to episodes 0 through 359 of comedy bang! bang! for 20 days, 14:59:33

  To calculate the runtime between two specific episodes use the arguments -f and -l. For example to calculate the runtime betwen episodes 1 and 10

    $ python cbbtime.py -f 0 -l 10
    you have listened to episodes 0 through 10 of comedy bang! bang! for 9:15:51

## Disclaimer
This is in no way meant to be a rigourous, reliable method of doing much of anything. I don't expect people will even see this but I figure it's useful to get some practice using github.
