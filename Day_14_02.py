#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:12:23 2020

@author: venky
"""
# remove .pyc files from git repo
"""
find . -name "*.pyc" -exec git rm -f {} \;
"""

import os
import sys
ENVIRONMENT = "development"
CONFIGFILE = None


def get_config_file():
    directory = os.path.dirname(__file__)
    return {
        "development": "{}/../config/development.cfg".format(directory),
        "staging": "{}/../config/staging.cfg".format(directory),
        "production": "{}/../config/production.cfg".format(directory)
    }.get(ENVIRONMENT, None)

CONFIGFILE = get_config_file()

if CONFIGFILE is None:
    sys.exit("Configuration error! Unknown environment set. \
              Edit config.py and set appropriate environment")
print("Config file: {}".format(CONFIGFILE))
if not os.path.exists(CONFIGFILE):
    sys.exit("Configuration error! Config file does not exist")
print("Config ok ....")


#_git_all_repos.py
import sys
import os
import requests


def get_total_repos(group, name):
    repo_urls = []
    page = 1
    while True:
        url = 'https://api.github.com/{0}/{1}/repos?per_page=100&page={2}'
        r = requests.get(url.format(group, name, page))
        if r.status_code == 200:
            rdata = r.json()
            for repo in rdata:
                repo_urls.append(repo['clone_url'])
            if (len(rdata) >= 100):
                page += 1
            else:
                print('Found {0} repos.'.format(len(repo_urls)))
                break
        else:
            print(r)
            return False
    return repo_urls


def clone_repos(all_repos):
    count = 1
    print('Cloning...')
    for repo in all_repos:
        os.system('Git clone ' + repo)
        print('Completed repo #{0} of {1}'.format(count, len(all_repos)))
        count += 1

if __name__ == '__main__':
    if len(sys.argv) > 2:
        total = get_total_repos(sys.argv[1], sys.argv[2])
        if total:
            clone_repos(total)

    else:
        print('Usage: python USERS_OR_ORG GITHUB_USER_OR_ORG-NAME')