#!/usr/bin/python3
"""
    that creates and distributes an archive to
    your web servers, using the function deploy:
"""
import os.path
from fabric.api import *
from fabric.operations import run, put, sudo
env.hosts = ['35.243.207.104', '35.196.142.184']



def do_pack():
    '''
        function to generate a .tgz archive
        ---
        The function do_pack must return the archive path
        if the archive has been correctly generated.
        Otherwise, it should return None.
    '''
    if not path.exists('versions'):
        local('mkdir versions')
    formater = '%Y%m%d%H%M%S'
    final_file = 'versions/web_static_{}.tgz'\
                 .format(datetime.now().strftime(formater))
    local('tar -czvf {} web_static'.format(final_file))
    return final_file


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
        run("sudo cp -r {}/web_static/* {}/".format(path_folder, path_folder))
        run("sudo rm -rf {}/web_static".format(path_folder))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {} /data/web_static/current".format(path_folder))
        return True
    except Exception:
        return False


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
        return(do_deploy(created_archive))
    except Exception:
        return False
