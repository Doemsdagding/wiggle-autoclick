import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    '--name=Wiggle&CLick',
    '--windowed',
    '--onefile',
    '--add-data', 'wiggler\\wiggle.kv:.',
    '--hidden-import', 'pkg_resources.extern.packaging.version',
    '--hidden-import', 'pkg_resources.extern.packaging.specifiers', 
    '--hidden-import', 'pkg_resources.extern.packaging.requirements',
    'wiggler\wiggler.py'
])

