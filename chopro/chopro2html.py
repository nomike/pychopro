"""chopro2html.py

Convert ChoPro/Chordpro to HTML

Usage:
    chopro2html.py [(-l | --lyrics)] <chopro_file>
    chopro2html.py (-h | --help)
    chopro2html.py --version

Example:
    chopro2html.py twinkle_twinkle_little_star.chopro > twinkle.html
"""

from docopt import docopt
import sys
import os

with open('VERSION') as version_file:
    VERSION = version_file.read().strip()


def print_usage():
    print(__doc__)

def main(argv=None):
    LYRICS_MODE = False
    arguments = docopt(__doc__, version=VERSION)
    if arguments['--help']:
        print_usage()
        sys.exit(0)
    if arguments['--version']:
        print(VERSION)
        sys.exit(0)
    if arguments['--lyrics']:
        LYRICS_MODE = True
    
    chopro_file_path = arguments['<chopro_file>']
    f = open(chopro_file_path, 'r')
    chopro = f.read()
    f.close()
    if LYRICS_MODE:
        lyrics = chopro2lyrics(chopro)
        print (lyrics)
    else:
        html = chopro2html(chopro)
        print (html)

def chopro2html(chopro_text):
    from chopro.core import ChoPro
    chopro = ChoPro(chopro_text)
    html = chopro.get_html()
    return html

def chopro2lyrics(chopro_text):
    from chopro.core import ChoPro
    chopro = ChoPro(chopro_text)
    lyrics = chopro.get_lyrics()
    return lyrics

if __name__ == '__main__':
    main()
