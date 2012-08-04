import os, sys
import pprint

import lxml.etree, lxml.html
from optparse import OptionParser

from microtron import Parser


def parse(argv=None):
    if argv is None:
        argv = sys.argv

    parser = OptionParser('usage: %prog <file> <format>')
    options, arguments = parser.parse_args(argv[1:])
    if len(arguments) != 2:
        parser.error('Incorrect number of arguments')

    source_filename = os.path.abspath(arguments[0])
    format = arguments[1]

    tree = lxml.html.parse(source_filename)
    pprint.pprint(Parser(tree).parse_format(format))


def check(argv=None):
    if argv is None:
        argv = sys.argv

    parser = OptionParser('usage: %prog <url> <format>')
    parser.add_option(
        "-s", "--strict",
        action="store_true", dest="strict", default=False,
        help="be strict about parsing"
    )

    options, arguments = parser.parse_args(argv[1:])
    if len(arguments) != 2:
        parser.error('Incorrect number of arguments')

    url = arguments[0]
    format = arguments[1]

    tree = lxml.html.parse(url)
    parser = Parser(tree, strict=True, collect_errors=True)
    parser.parse_format(format)
    print "%d errors:" % (len(parser.errors))

    errs = parser.errors
    errs.sort(lambda x, y: cmp(x.sourceline, y.sourceline))
    for err in errs:
        print "ERROR (line %d): %s" % (err.sourceline, err)

    # TODO: extra checks for hnews:
    # - warn if dates insane (future, or distant past)
    # - updated but no published
    # - concatenated authors in single vcard ("Bob Smith and Fred Bloggs")
    # - insanity in content (eg adverts, scripts....)
