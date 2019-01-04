#!c:\users\xiang\pycharmprojects\test_django\ll_env\scripts\python.exe
from django.core import management

import django

if __name__ == "__main__":
    management.execute_from_command_line()
print(django.__file__)