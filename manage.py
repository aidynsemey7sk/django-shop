#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from termcolor import colored, cprint
import socket
from base.settings import DEBUG


hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
    try:
        from django.core.management import execute_from_command_line
        if len(sys.argv) > 0:
            if DEBUG:
                print(colored(f'Режим "DEBUG"', 'yellow'))
            print(colored(f'Была запущена команда {sys.argv[1].upper()} от пользователя {os.getlogin().upper()}, операционная система {sys.platform.upper()},'
                          f' IP: {IPAddr}', 'yellow', attrs=['underline']))
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
