#!/usr/bin/python3
"""
script that distributes archive to webservers
"""
import os.path
from fabric.api import *
from fabric.operations import run, put, sudo
env.hosts = ['34.74.9.37', '34.74.166.225']


def do_deploy(archive_path):
    """ Preprares .tgz file to be deployed """
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        fname = archive_path.split("/")[-1]
        path_folder = ("/data/web_static/releases/" + fname.split(".")[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(path_folder))
        run("sudo tar -xzf /tmp/{} -C {}".
            format(fname, path_folder))
        run("sudo rm /tmp/{}".format(fname))
        run("sudo mv {}/web_static/* {}/".format(path_folder, path_folder))
        run("sudo rm -rf {}/web_static".format(path_folder))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {} /data/web_static/current".format(path_folder))
        return True
    except Exception:
        return False
