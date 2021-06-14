#!/usr/bin/env python3
"""
后台服务启动脚本

Usage::

    $ ./gunicorn_server.py 9999
"""
import os
import sys
from pathlib import Path

PORT = 9999


def run_silently(cmd):
    with os.popen(cmd) as p:
        return p.read().strip()


def main():
    if sys.argv[1:]:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid arg.\n", __doc__)
            sys.exit()
        cmd = "poetry run gunicorn -b :{} --daemon --reload wechat.wsgi".format(port)
    else:
        a = input("Which port to start server? (Leave blank to use 9999) ").strip()
        if a:
            try:
                port = int(a)
            except ValueError:
                print("Invalid arg.", __doc__)
                sys.exit()
        else:
            port = PORT
        cmd = "poetry run gunicorn -b :{} wechat.wsgi".format(port)
        b = input("Auto reload? [Y/n] ").strip()
        if b.lower() != "n":
            cmd += " --reload"
        c = input("Start as daemon? [Y/n] ").strip()
        if c.lower() != "n":
            cmd += " --daemon"
    cmd = cmd.replace("poetry run ", "")
    print("-->", cmd)
    if os.system(cmd) == 0:
        print("Waiting for server starting ...")
        check = "ps -ef|grep {}".format(port)
        if Path(__file__).resolve().parent.name not in run_silently(check):
            print("\nIt seems that server start failed!")
            d = input("Do you want to start without daemon flag to see why? [Y/n]")
            if d.strip().lower() == "n":
                print("Exit!")
                sys.exit()
            cmd = cmd.replace("--daemon", "")
            print("-->", cmd)
            os.system(cmd)
        else:
            print("Success to start server.")


if __name__ == "__main__":
    main()
