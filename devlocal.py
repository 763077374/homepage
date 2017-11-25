from fabric.api import local
def install():
    local("pip install -r requirements.txt")

from fabric.api import local
def install(requirements_env="dev"):
    local("pip install -r requirements/%s.txt" % requirements_env)
    #fab install
    #fab install prod

from fabric.api import local
from fabric.decorators import task
@task
def runserver():
    """Run Server"""
    local("./manage.py runserver")
#fab  --list
#fab