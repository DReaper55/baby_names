#!C:\Users\Daniel\PycharmProjects\TKinter\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'cursor==1.3.1','console_scripts','cursor_hide'
__requires__ = 'cursor==1.3.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('cursor==1.3.1', 'console_scripts', 'cursor_hide')()
    )
