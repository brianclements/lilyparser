LilyParser
==========

LilyParser is LilyPond parser for Python.

Directory Structure
----------

All library files are in LilyParser directory.
- Parser.py : Parser. You'd import this to parse .ly files.
- Units.py : Classes for LilyParser.
- Functions.py : Custom functions for LilyParser.
- Data.py : Custom data classes for LilyParser.

HOW TO USE?
----------

    from LilyParser import Parser
    parsed_data = Parser(lilypond_text).Parse()

Example Script
----------
You can test LilyParser with the example script, "parse.py".
The way you'd test it is like below.

Example)
<code># python parse.py test.ly</code>

Introduce Project Tsumugi
----------

This project is started as the subproject of Project Tsumugi : http://projects.yuiazu.net/tsumugi    
If you're interested in Arduino, please visit the link.

# Thanks!
