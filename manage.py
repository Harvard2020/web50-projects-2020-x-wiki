#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wiki.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
<<<<<<< HEAD
        ) 
=======
        ) from exc
>>>>>>> 323cbed56534f37580f2db0e532a9b7ac9b5db10
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
