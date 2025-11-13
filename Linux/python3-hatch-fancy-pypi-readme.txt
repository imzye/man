HATCH-FANCY-PYPI-README(1)                                                                                                                                                       HATCH-FANCY-PYPI-README(1)

NAME
       hatch-fancy-pypi-readme - render Python project README

SYNOPSIS
       hatch-fancy-pypi-readme [options] [PATH]

DESCRIPTION
       hatch-fancy-pypi-readme is a CLI tool to manually render the project README as defined in pyproject.toml and hatch.toml.  Normally, the render process is invoked as part of the hatchling build.

       The following options are recognized:

       PATH   the path to the pyproject.toml of the project. If omitted, the current directory is used.

       -o OUTPUT
              write result to OUTPUT.  If omitted, the results are written to stdout.

       --hatch-toml FILE
              Read an additional hatch.toml for rendering options.

MANUAL PAGE
       This manual page was written for the Debian distribution by Timo Röhling, and may be used without restriction.

                                                                                                                                                                                 HATCH-FANCY-PYPI-README(1)
