# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by leesavide
# Copyright (c) 2017 leesavide
#
# License: MIT

"""This module exports the Abcm2ps plugin class."""

from SublimeLinter.lint import Linter, util

class Abcm2ps(Linter):
    """Provides an interface to abcm2ps."""

    syntax = 'abc'
    cmd = ['abcm2ps', '-i', '-S', '-N 3', '-j 1', '-O =']
    executable = None
    version_args = '-V'
    version_re = r'abcm2ps-(?P<version>\d+\.\d+\.\d+) \(.*\)'
    version_requirement = '>= 5.0.0'
    regex = (
      r'^.+?:(?P<line>\d+):(?P<col>\d+): '
      r'(?:(?P<error>(?:Internal )?error)|(?P<warning>warning): )(?P<message>.+)'
    )
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = '-'
    error_stream = util.STREAM_BOTH
    selectors = {
      'abc': 'meta.tune.abc'
    }
    # Highlight the symbol the error or warning occured on
    word_re = r'([-\w]+)'
    defaults = {
      '--abc2pscompat:': 'no',
      '--alignbars:': 0,
      '--aligncomposer:': 2,
      '--annotationfont: +': 'Helvetica utf-8 12.0',
      '--autoclef:': 'yes',
      '--barsperstaff:': 0,
      '--bgcolor:': "",
      '--botmargin:': '1.00cm',
      '--breaklimit:': 0.70,
      '--breakoneoln:': 'yes',
      '--bstemdown:': 'no',
      '--cancelkey:': 'yes',
      '--combinevoices:': 0,
      '--composerfont: +': 'Times-Italic utf-8 14.0',
      '--composerspace:': 6.00,
      '--contbarnb:': 'no',
      '--continueall:': 'no',
      '--custos:': 'no',
      '--dateformat: +': "%b', %#d, %Y %H:%M",
      '--dblrepbar:': ':][:',
      '--decoerr:': 'yes',
      '--dynalign:': 'yes',
      '--footer:': "",
      '--footerfont: +': 'Times-Roman utf-8 16.0',
      '--flatbeams:': 'no',
      '--gchordbox:': 'no',
      '--gchordfont: +': 'Helvetica utf-8 12.0',
      '--graceslurs:': 'yes',
      '--graceword:': 'no',
      '--gracespace: +': '6.5 8.0 12.0',
      '--gutter:': 0.00,
      '--header:': "",
      '--headerfont: +': 'Times-Roman utf-8 16.0',
      '--historyfont: +': 'Times-Roman utf-8 16.0',
      '--hyphencont:': 'yes',
      '--indent:': 0.00,
      '--infofont: +': 'Times-Italic utf-8 14.0',
      '--infoline:': 'no',
      '--infospace:': 0.00,
      '--keywarn:': 'yes',
      '--landscape:': 'no',
      '--leftmargin:': '1.80cm',
      '--lineskipfac:': 1.10,
      '--linewarn:': 'yes',
      '--maxshrink:': 0.65,
      '--maxstaffsep:': 2000.00,
      '--maxsysstaffsep:': 2000.00,
      '--measurebox:': 'no',
      '--measurefirst:': 1,
      '--measurefont: +': 'Times-Italic utf-8 14.0',
      # Always number measures, ESPECIALLY while linting.
      # This is the only setting that is altered from the parameters that
      # abcm2ps defines as defaults.
      '--measurenb:': 1,
      # '--measurenb:': '-1',
      '--micronewps:': 'no',
      '--musicfont: +': "",
      '--musicspace:': 6.00,
      '--notespacingfactor:': 1.41,
      '--oneperpage:': 'no',
      '--pageheight:': '29.70cm',
      '--pagewidth:': '21.00cm',
      '--pagescale:': 1.00,
      '--pango:': 'no',
      '--parskipfac:': 0.40,
      '--partsbox:': 'no',
      '--partsfont: +': 'Times-Roman utf-8 15.0',
      '--partsspace:': 8.00,
      '--pdfmark:': 0,
      '--rbdbstop:': 'yes',
      '--rbmax:': 4,
      '--rbmin:': 2,
      '--repeatfont: +': 'Times-Roman utf-8 13.0',
      '--rightmargin:': '1.80cm',
      '--setdefl:': 'no',
      '--shiftunison:': 0,
      '--slurheight:': 1.00,
      '--splittune:': 0,
      '--squarebreve:': 'no',
      '--staffnonote:': 1,
      '--staffsep:': 46.00,
      '--staffwidth:': '17.40cm',
      '--stemheight:': 21.00,
      '--straightflags:': 'no',
      '--stretchlast:': 0.25,
      '--stretchstaff:': 'yes',
      '--subtitlefont: +': 'Times-Roman utf-8 16.0',
      '--subtitlespace:': 3.00,
      '--sysstaffsep:': 34.00,
      '--tempofont: +': 'Times-Bold utf-8 15.0',
      '--textfont: +': 'Times-Roman utf-8 16.0',
      '--textoption:': 0,
      '--textspace:': 14.00,
      '--titlecaps:': 'no',
      '--titlefont: +': 'Times-Roman utf-8 20.0',
      '--titleformat:': "",
      '--titleleft:': 'no',
      '--titlespace:': 6.00,
      '--titletrim:': 'yes',
      '--timewarn:': 'no',
      '--topmargin:': '1.00cm',
      '--topspace:': 22.00,
      '--tuplets: +': '0 0 0 0',
      '--vocalfont: +': 'Times-Bold utf-8 13.0',
      '--vocalspace:': 10.00,
      '--voicefont: +': 'Times-Bold utf-8 13.0',
      '--wordsfont: +': 'Times-Roman utf-8 16.0',
      '--wordsspace:': 0.00,
      '--writefields:': 'CMOPQTWw'
    }
    inline_settings = None
    inline_overrides = None
    comment_re = r'(?:^r:.*)|(?:\[r:[^\r\n\]]*\])|(?:\s*%.*)'
