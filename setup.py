from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options={'py2exe': {'compressed': True, "includes": ["sip"]}},
    windows=[{
        "script": "McPython.py",
        "icon_resources": [(1, "icons/icon.ico")],
    }],
)
