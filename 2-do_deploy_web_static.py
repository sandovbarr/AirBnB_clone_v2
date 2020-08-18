#!/usr/bin/python3
'''
    Fabric script (based on the file 1-pack_web_static.py)
    that distributes an archive to your web servers, using
    the function do_deploy:
'''
import os
from fabric.api import local, env
from fabric.operations import run, put, sudo
from datetime import datetime
env.hosts = ['35.243.207.104', '35.196.142.184']


def do_pack():
    '''
        function to generate a .tgz archive
        ---
        The function do_pack must return the archive path
        if the archive has been correctly generated.
        Otherwise, it should return None.
    '''
    if not os.path.exists('versions'):
        local('mkdir versions')
    formater = '%Y%m%d%H%M%S'
    final_file = 'versions/web_static_{}.tgz'\
                 .format(datetime.now().strftime(formater))
    local('tar -czvf {} web_static'.format(final_file))
    return final_file


def do_deploy(archive_path):
    '''
        Returns False if the file at the path
        archive_path doesn’t exist
    '''
    if (os.path.isfile(archive_path) is False):
        return False

    try:

        fname = archive_path.split("/")[-1]
        uncompressed_path = ("/data/web_static/releases/" + fname.split(".")[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(uncompressed_path))
        run("sudo tar -xzf /tmp/{} -C {}".
            format(fname, uncompressed_path))
        run("sudo rm /tmp/{}".format(fname))
        run("sudo mv {}/web_static/* {}/".format(uncompressed_path, uncompressed_path))
        run("sudo rm -rf {}/web_static".format(uncompressed_path))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {} /data/web_static/current".format(uncompressed_path))
        print('New version deployed!')
        return True

    except Exception:
        return False
