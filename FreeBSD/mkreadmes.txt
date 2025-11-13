MKREADMES(1)            FreeBSD General Commands Manual           MKREADMES(1)

NAME
     mkreadmes – high performance replacement for ports(8) “make readmes”.

SYNOPSIS
     mkreadmes [options] [pathname-list]

DESCRIPTION
     mkreadmes creates README.html files for one or more ports, just as “make
     readmes” from ports(8) does.

     Just a tad bit faster.  Like in “order of magnitude” faster, since it is
     specially built for the purpose.

     Without options, mkreadmes will recursively create README.html files for
     all ports found either in /usr/ports, or the directory pointed to by
     PORTSDIR, resulting in a browseable hierarchy of README.html files.

OPTIONS
     -h      Display help.

     -n      Do not reparent paths given in pathname-list.  See -p for more
             information.

     -p pathname
             Set toplevel directory to pathname.  mkreadmes expects the ports
             tree's INDEX file to be in this directory, and will work its way
             down from here.  Relative paths in pathname-list will have their
             parent set to pathname, unless -n is used.

             Without -p, mkreadmes defaults to /usr/ports, unless PORTSDIR is
             defined.

     -q      Just print errors, be quiet otherwise.

     -t pathname
             Template files should be read from pathname, instead of the
             default /usr/local/share/mkreadmes/Templates.

     -v      Be more verbose, reporting more detailed progress information.
             May be repeated to obtain progressively more lower-level details.

     -V      Display version information.

     pathname-list
             Optional list of port and/or category pathnames separated by
             whitespace. If pathname-list is omitted, mkreadmes defaults to
             work on the entire ports tree.

ENVIRONMENT
     PORTSDIR
             If not given, mkreadmes defaults to using /usr/ports.

EXAMPLES
     Three ways for creating README.html for the port sysutils/froxlor:
           # mkreadmes /usr/ports/sysutils/froxlor
           # mkreadmes -vp /usr/ports sysutils/froxlor
           # mkreadmes -qnp /usr/ports /usr/ports/sysutils/froxlor

     Mimic “make readmes” from ports(8), creating README.html for all ports
     and categories in /usr/ports or the directory pointed to by PORTSDIR:
           # mkreadmes

DIAGNOSTICS
     The mkreadmes utility exits 0 on success, and >0 if an error occurs.

SEE ALSO
     The mkreadmes homepage at: http://mkreadmes.sourceforge.net.

AUTHOR
     mkreadmes was written by Conrad J. Sabatier <conrads@cox.net>.

     This man page was written by Marco Steinbach
     <coco@executive-computing.de>.

                                 March 4, 2012
