#!/usr/bin/python3
"""
    that creates and distributes an archive to
    your web servers, using the function deploy:
"""
import os.path
from fabric.api import *
from fabric.operations import run, put, sudo
from 2-do_deploy_web_static import do_deploy
from 1-pack_web_static import do_pack
env.hosts = ['35.243.207.104', '35.196.142.184']


def deploy():
    """
        Call the do_pack() function and store the
        path of the created archive
        Return False if no archive has been created

        Call the do_deploy(archive_path) function,
        using the new path of the new archive
        Return the return value of do_deploy
    """

    created_archive = do_pack()
    if (os.path.isfile(created_archive) is False):
        return False
    try:
        do_deploy(created_archive)
    except Exception:
        return False
