import os

from django.core.management.base import NoArgsCommand
from django.conf import settings 

from codenode_desktop import run


class Command(NoArgsCommand):
    """
    Run a Backend Server.
    """

    def handle_noargs(self, **options):
        abspath = os.path.abspath(".")
        cmd = "twistd "
        if not options.get('daemonize', False):
            cmd += "-n "
        cmd += "codenode-backend "
        cmd += "--env_path=%s " % settings.HOME_PATH
        run(cmd.split()[1:])