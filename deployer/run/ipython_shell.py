#!/usr/bin/env python

def start(settings):
    from IPython.Shell import IPShellEmbed
    root = settings()
    ipshell = IPShellEmbed()
    ipshell()

if __name__ == '__main__':
    from deployer.contrib.default_config import settings
    start(settings=settings)
