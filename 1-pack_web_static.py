#!/usr/bin/python3
'''
    Fabric script that generates a .tgz archive
    from the contents of the web_static folder of
    your AirBnB Clone repo, using the function do_pack.
'''
from os import path
from fabric.api import local
from datetime import datetime


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
    final_file = 'web_static_{}.tgz'\
                 .format(datetime.now().strftime(formater))
    local('tar -czvf {} web_static'.format(final_file))
    return final_file
