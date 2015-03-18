#!/usr/bin/env python3

import bs4
import datetime as dt
import requests
import sys
import getopt


def get_latest_rss():
    url = 'http://rss.earwolf.com/comedy-bang-bang'
    r = requests.get(url)

    return str(r.content)


def get_episode_durations(soup):
    times = []
    for item in soup.find_all('item'):
        for tag in item.findChildren('itunes:duration'):
            times.append(tag.get_text())

    return times[::-1]


def cbb_cum_sum(episode_times, first=0, last=None):
    MAX = len(episode_times)
    if last is None:
        last = MAX

    episode_d = [dt.datetime.strptime(time, "%H:%M:%S") for time in episode_times]

    cbbsum = dt.timedelta(hours=0, minutes=0, seconds=0)
    for time in episode_d[first:last]:
        cbbsum += dt.timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)

    return cbbsum


def main(argv):
    first = 0
    last = None

    if len(argv) != 0:
        try:
            opts, args = getopt.getopt(argv, 'f:l:')
        except getopt.GetoptError:
            sys.exit(2)

        first = int(opts[0][1])
        last = int(opts[1][1])

    cbbrss = get_latest_rss()
    cbbsoup = bs4.BeautifulSoup(cbbrss)
    episode_times = get_episode_durations(cbbsoup)
    cbbsum = cbb_cum_sum(episode_times, first=first, last=last)

    print('you have listened to episodes', first, 'through', last, 'of comedy bang! bang! for', str(cbbsum))

if __name__ == '__main__':
    main(sys.argv[1:])
