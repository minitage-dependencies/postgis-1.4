import os
from minitage.core.common import substitute

def pre_make(options, buildout):
    """Custom pre-make hook for patching PostGIS."""
    rpath = os.environ['LDFLAGS']
    makefiles = [os.path.join(options['compile-directory'],'loader','Makefile'),
                 os.path.join(options['compile-directory'],'regress','Makefile'),
                 os.path.join(options['compile-directory'],'java','jdbc','Makefile'),
                 os.path.join(options['compile-directory'],'liblwgeom','examples','Makefile'),
                 os.path.join(options['compile-directory'],'liblwgeom','Makefile'),
                 os.path.join(options['compile-directory'],'liblwgeom','cunit','Makefile'),
                 os.path.join(options['compile-directory'],'extras','wkb_reader','Makefile'),
                 os.path.join(options['compile-directory'],'extras','WFS_locks','Makefile'),
                 os.path.join(options['compile-directory'],'extras','template_gis','Makefile'),
                 os.path.join(options['compile-directory'],'extras','ogc_test_suite','Makefile'),
                 os.path.join(options['compile-directory'],'postgis','Makefile'),
                 os.path.join(options['compile-directory'],'Makefile'),
                 os.path.join(options['compile-directory'],'doc','html','image_src','Makefile'),
                 os.path.join(options['compile-directory'],'doc','Makefile'),
                 os.path.join(options['compile-directory'],'utils','Makefile'),
                 os.path.join(options['compile-directory'],'topology','test','Makefile'),
                 os.path.join(options['compile-directory'],'topology','ER','Makefile'),
                 os.path.join(options['compile-directory'],'topology','Makefile'),
                ]
    open(
        os.path.join(options['compile-directory'],'Makefile.config'),
        'w'
    ).write('prefix=%s\n' % options['location'])
    for p in makefiles + [\
              os.path.join(options['compile-directory'], 'Makefile'),
              os.path.join(options['compile-directory'], 'GNUmakefile'), ]:
        substitute(p, '(.*)\\$\(DESTDIR\\)(.*)', '\\1$(prefix)\\2')
        # Put in rpath info
        substitute(p, 'LDFLAGS=-shared', 'LDFLAGS=-shared %s' % rpath)

def pre_make_deb(options, buildout):
    """Custom pre-make hook for patching PostGIS."""
    # ``make install`` fails because it tries to write files under
    # /etc. This will write under the corresponding parts directory
    # instead.
    substitute(
        os.path.join(
            options['compile-directory'],
            'loader',
        ),
        '\$\(DESTDIR\)',
        '$(prefix)')
def h(options, buildout):
    print
    print
    print
    print
    print
    print
    print
    print
    print
    print
    print
    print
    print "--------------------------------------------------------------------------------------------------------"
    print "POSTGIS INSTALL ITSELF INSIDE POSTGRESQL, SO TOUCHING POSTGRESQL == RE MINIMERGE POSTGIS    !!!!!!"
    print "--------------------------------------------------------------------------------------------------------"
    print
    print
    print
    print
    print
    print
    print
    print
    print
    print
    print
    print




