from fabric.api import env, task, run, cd, prefix
from fabric.operations import sudo

env.hosts = ['192.168.2.27']
env.user = 'pi'
env.password = 'raspberry'

def virtualenv(what):
    run('/home/{0}/.virtualenvs/obsidian/bin/{1}'.format(env.user, what))

@task
def configure():
    # sudo('apt-get update')
    # sudo('apt-get install -y virtualenvwrapper')
    run('mkdir -p /home/{0}/ohc'.format(env.user))
    with cd('/home/{0}/ohc'.format(env.user)):
        run('rm -rf obsidian')
        run('git clone https://github.com/davidmiller/obsidian')
    with cd('/home/{0}/ohc/obsidian'.format(env.user)):
        with prefix('WORKON_HOME=$HOME/.virtualenvs'):
            with prefix('source /etc/bash_completion.d/virtualenvwrapper'):
                run('rmvirtualenv obsidian')
                run('mkvirtualenv -a /home/{0}/ohc/obsidian obsidian'.format(env.user))
    pass

@task
def deploy():
    with cd('/home/{0}/ohc/obsidian'.format(env.user)):
        run('git pull origin master')
        virtualenv('pip install -r requirements.txt')

    pass
