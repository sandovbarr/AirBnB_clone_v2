#!/usr/bin/python3
'''
    Fabric script (based on the file 1-pack_web_static.py)
    that distributes an archive to your web servers, using
    the function do_deploy:
'''
import os
from fabric.api import *
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
    if os.path.exists(archive_path) is False:
        return False
    try:
        put(archive_path, '/tmp/')
        path_split = archive_path.split('/')
        filename = path_split[-1]
        filesplit = filename.split('.')
        filename_no_ext = filesplit[0]
        uncompress_path = '/data/web_static/releases/' + filename_no_ext

        run('sudo mkdir -p {}'.format(uncompress_path))
        run('sudo tar -xvf {} -C {}'.format('/tmp/' + filename, uncompress_path))

        run('sudo rm /tmp/{}'.format(filename))
        rum('sudo rm /data/web_static/current')

        run('sudo ln -sf /data/web_static/releases/{} /data/web_static/current'
            .format(filename_no_ext))
        return True
    except Exception:
        return False