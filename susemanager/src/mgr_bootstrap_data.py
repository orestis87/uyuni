#
# DO NOT EDIT !!!
#

# package list format
#
# | alternative. Example: "a|b" when package "a" cannot be found try "b". First match wins.
#                One must be available.
# * optional. Example: "a*" if "a" is available add it, otherwise ignore it

PKGLIST10 = [
    "libaugeas0",
    "libnewt0_52",
    "libzypp",
    "newt",
    "openssl",
    "perl-WWW-Curl",
    "python-dmidecode",
    "python-ethtool",
    "python-newt",
    "python-openssl",
    "python-xml",
    "python2-rhnlib",
    "rpm-python",
    "satsolver-tools",
    "spacewalk-check",
    "spacewalk-client-setup",
    "spacewalk-client-tools",
    "mgr-daemon|spacewalksd",
    "suseRegister",
    "suseRegisterInfo",
    "yast2-ncurses",
    "yast2-perl-bindings",
    "yast2-pkg-bindings",
    "yast2-qt",
    "zypp-plugin-python",
    "zypp-plugin-spacewalk",
    "zypper"
]

PKGLIST11 = [
    "dbus-1-python",
    "libcurl4",
    "libnewt0_52",
    "libnl",
    "libopenssl0_9_8",
    "libsqlite3-0",
    "libxml2-python",
    "libzypp",
    "newt",
    "openssl",
    "python",
    "python-dmidecode",
    "python-ethtool",
    "python-newt",
    "python-openssl",
    "python-xml",
    "python2-rhnlib",
    "rpm-python",
    "satsolver-tools",
    "slang",
    "spacewalk-check",
    "python2-spacewalk-check",
    "spacewalk-client-setup",
    "python2-spacewalk-client-setup",
    "spacewalk-client-tools",
    "python2-spacewalk-client-tools",
    "python2-uyuni-common-libs",
    "mgr-daemon|spacewalksd",
    "suseRegisterInfo",
    "python2-suseRegisterInfo",
    "zypp-plugin-python",
    "zypp-plugin-spacewalk",
    "python2-zypp-plugin-spacewalk",
    "zypper",
]

ENHANCE11 = [
    "libyaml-0-2",
    "libzmq3",
    "python-backports.ssl_match_hostname",
    "python-certifi",
    "python-curl",
    "python-futures",
    "python-Jinja2",
    "python-MarkupSafe",
    "python-msgpack-python",
    "python-psutil",
    "python-pycrypto",
    "python-pyzmq",
    "python-requests",
    "python-simplejson",
    "python-tornado",
    "python-yaml",
    "salt",
    "salt-minion"
]

PKGLIST11_X86_I586 = [
    "pmtools",
]

PKGLIST12 = [
    "dbus-1-python",
    "hwdata",
    "libcurl4",
    "libgudev-1_0-0",
    "libnewt0_52",
    "libnl1",
    "libopenssl1_0_0",
    "libsqlite3-0",
    "libudev1",
    "udev",
    "openssl",
    "python-libxml2",
    "libzypp",
    "newt",
    "python",
    "python-cffi",
    "python-cryptography",
    "python-dmidecode",
    "python-ethtool",
    "python-gobject2",
    "python-gudev",
    "python2-hwdata",
    "python-newt",
    "python-pyasn1",
    "python-pycparser",
    "python-pyOpenSSL",
    "python-six",
    "python-xml",
    "python-pyudev",
    "python2-rhnlib",
    "rpm-python",
    "libsolv-tools",
    "libslang2",
    "spacewalk-check",
    "python2-spacewalk-check",
    "spacewalk-client-setup",
    "python2-spacewalk-client-setup",
    "spacewalk-client-tools",
    "python2-spacewalk-client-tools",
    "python2-uyuni-common-libs",
    "mgr-daemon|spacewalksd",
    "suseRegisterInfo",
    "python2-suseRegisterInfo",
    "zypp-plugin-python",
    "zypp-plugin-spacewalk",
    "python2-zypp-plugin-spacewalk",
    "zypper",
    "yast2-packager",
    "yast2-pkg-bindings",
    "python-backports.ssl_match_hostname",
    "python-futures",
    "python-Jinja2",
    "python-MarkupSafe",
    "python-msgpack-python",
    "python-psutil",
    "python-pycrypto",
    "python-PyYAML",
    "python-pyzmq",
    "python-requests",
    "python-simplejson",
    "python-singledispatch",
    "python-tornado",
    "salt",
    "salt-minion",
    "python2-salt",
    "libgio-2_0-0",
    "libgthread-2_0-0",
    "shared-mime-info",
    "glib2-tools",
    "libelf0",
    "logrotate",
    "cron",
    "cronie"
]

ONLYSLE12 = [
    "libzmq3",
    "gio-branding-SLE",
    "wallpaper-branding-SLE"
]

PKGLIST12_X86_ARM = [
    "dmidecode",
]

ONLYOPENSUSE42 = [
    "libzmq5",
    "gio-branding-openSUSE",
    "wallpaper-branding-openSUSE",
]

ENHANCE12 = [
    "libyui-ncurses-pkg6",
    "libyui-qt-pkg6",
    "PackageKit-backend-zypp",
    "PackageKit-lang",
]

ENHANCE12SP1 = [
    "libyui-ncurses-pkg7",
    "libyui-qt-pkg7",
    "python-asn1crypto",
    "python-enum34",
    "python-idna",
    "python-ipaddress",
    "python-packaging",
    "python-pyparsing",
    "python-setuptools",
]

# This is in fact only required for now for AWS SLE12SP5 x86_64 images,
# as they do not have dbus-1-glib installed
ENHANCE12SP5_X86 = [
    "dbus-1-glib",
    "girepository-1_0",
    "libcairo2",
    "libdatrie1",
    "libdrm2",
    "libdrm_amdgpu1",
    "libdrm_intel1",
    "libdrm_nouveau2",
    "libdrm_radeon1",
    "libgbm1",
    "libgirepository-1_0-1",
    "libgobject-2_0-0",
    "libgraphite2-3",
    "libharfbuzz0",
    "libLLVM7",
    "libpango-1_0-0",
    "libpciaccess0",
    "libpixman-1-0",
    "libthai0",
    "libthai-data",
    "libX11-xcb1",
    "libxcb-dri2-0",
    "libxcb-dri3-0",
    "libxcb-glx0",
    "libxcb-present0",
    "libxcb-render0",
    "libxcb-shm0",
    "libxcb-sync1",
    "libxcb-xfixes0",
    "libXdamage1",
    "libXfixes3",
    "libXft2",
    "libXrender1",
    "libxshmfence1",
    "libXxf86vm1",
    "Mesa",
    "Mesa-dri",
    "Mesa-libEGL1",
    "Mesa-libGL1",
    "Mesa-libglapi0",
    "python-gobject",
    "typelib-1_0-Pango-1_0",
]

RES6 = [
    "salt",
    "salt-minion",
    "python-futures",
    "python-jinja2",
    "python-msgpack-python",
    "python-psutil",
    "python-pycrypto",
    "python-requests",
    "python-setuptools",
    "python-tornado",
    "python-zmq",
    "zeromq",
    "openssl",
    "python-backports-ssl_match_hostname",
    "python-backports",
    "python-certifi",
    "python-simplejson",
    "PyYAML",
    "python-markupsafe",
    "python-urllib3",
    "libyaml",
    "python-chardet",
    "python-six",
    "python-babel",
    "dbus",
    "dbus-libs",
    "yum-plugin-security",
    "yum-rhn-plugin",
    "yum",
    "python2-rhnlib",
    "rpm-python",
    "redhat-rpm-config",
    "slang",
    "spacewalk-check",
    "python2-spacewalk-check",
    "spacewalk-client-setup",
    "python2-spacewalk-client-setup",
    "spacewalk-client-tools",
    "python2-spacewalk-client-tools",
    "python2-uyuni-common-libs",
    "mgr-daemon|spacewalksd",
    "suseRegisterInfo",
    "python2-suseRegisterInfo",
    "python2-hwdata",
    "dmidecode",
    "openssh-clients",
    "libedit",
]

RES7 = [
    "salt",
    "salt-minion",
    "python2-salt",
    "python-futures",
    "python-jinja2",
    "python-msgpack-python",
    "python-psutil",
    "python-pycrypto",
    "python-requests",
    "python-setuptools|python2-setuptools", # python-setuptools is the Amazon Linux name
    "python-singledispatch",
    "python-tornado",
    "python-zmq",
    "zeromq",
    "python-backports-ssl_match_hostname",
    "python-backports",
    "python-certifi",
    "python-simplejson",
    "PyYAML",
    "python-markupsafe",
    "python-urllib3",
    "libyaml",
    "python-chardet",
    "python-six",
    "python-babel",
    "yum-rhn-plugin",
    "yum",
    "python2-rhnlib",
    "openssl",
    "openssl-libs",
    "python-ipaddress",
    "redhat-rpm-config|system-rpm-config", # system-rpm-config is the Amazon Linux name
    "rpm-python",
    "spacewalk-check",
    "python2-spacewalk-check",
    "spacewalk-client-setup",
    "python2-spacewalk-client-setup",
    "spacewalk-client-tools",
    "python2-spacewalk-client-tools",
    "python2-uyuni-common-libs",
    "mgr-daemon|spacewalksd",
    "suseRegisterInfo",
    "python2-suseRegisterInfo",
    "python2-hwdata"
]

RES7_X86 = [
    "dmidecode"
]

RES8 = [
    "redhat-rpm-config",
    "salt",
    "salt-minion",
    "python3-salt",
    "python3-babel",
    "python3-msgpack",
    "python3-tornado",
    "python3-zmq",
    "python3-jinja2",
    "python3-m2crypto",
    "python3-markupsafe",
    "python3-psutil",
    "python3-pyyaml",
    "python3-requests",
    "openpgm",
    "zeromq",
    "python3-urllib3",
    "python3-idna",
    "python3-chardet",
    "python3-pysocks",
    "python3-pytz",
    "python3-setuptools",
    "python3-distro"
]

RES8_X86 = [
    "dmidecode"
]

AMAZONLINUX2 = [
    "dwz",
    "groff-base",
    "perl",
    "perl-Carp",
    "perl-Encode",
    "perl-Exporter",
    "perl-File-Path",
    "perl-File-Temp",
    "perl-Filter",
    "perl-Getopt-Long",
    "perl-HTTP-Tiny",
    "perl-PathTools",
    "perl-Pod-Escapes",
    "perl-Pod-Perldoc",
    "perl-Pod-Simple",
    "perl-Pod-Usage",
    "perl-Scalar-List-Utils",
    "perl-Socket",
    "perl-Storable",
    "perl-Text-ParseWords",
    "perl-Time-HiRes",
    "perl-Time-Local",
    "perl-constant",
    "perl-libs",
    "perl-macros",
    "perl-parent",
    "perl-podlators",
    "perl-srpm-macros",
    "perl-threads",
    "perl-threads-shared",
    "zip"
]

PKGLIST15_SALT = [
    "libpgm-5_2-0",
    "libsodium23",
    "libzmq5",
    "openssl",
    "python3-Babel",
    "python3-certifi",
    "python3-chardet",
    "python3-distro",
    "python3-idna",
    "python3-Jinja2",
    "python3-MarkupSafe",
    "python3-M2Crypto",
    "python3-msgpack",
    "python3-psutil",
    "python3-py",
    "python3-pytz",
    "python3-PyYAML",
    "python3-pyzmq",
    "python3-requests",
    "python3-rpm",
    "python3-simplejson",
    "python3-six",
    "python3-urllib3",
    "timezone",
    "salt",
    "python3-salt",
    "salt-minion",
]

PKGLIST15SP0SP1_SALT = [
    "python3-tornado",
]

ONLYSLE15 = [
    "gio-branding-SLE",
]

PKGLIST15_TRAD = [
    "dbus-1-glib",
    "glib2-tools",
    "girepository-1_0",
    "libgudev-1_0-0",
    "libgirepository-1_0-1",
    "libgio-2_0-0",
    "libgobject-2_0-0",
    "libnewt0_52",
    "libslang2",
    "newt",
    "python3-asn1crypto",
    "python3-cffi",
    "python3-cryptography",
    "python-dmidecode",
    "python3-dbus-python",
    "python3-dmidecode",
    "python3-gobject",
    "python3-libxml2-python",
    "python3-netifaces",
    "python3-newt",
    "python3-pyasn1",
    "python3-pycparser",
    "python3-pyOpenSSL",
    "python3-pyudev",
    "python3-packaging",
    "python3-setuptools",
    "python3-appdirs",
    "python3-pyparsing",
    "hwdata",
    "python3-hwdata",
    "python3-rhnlib",
    "spacewalk-check",
    "spacewalk-client-setup",
    "spacewalk-client-tools",
    "python3-spacewalk-check",
    "python3-spacewalk-client-setup",
    "python3-spacewalk-client-tools",
    "python3-uyuni-common-libs*",
    "mgr-daemon|spacewalksd",
    "shared-mime-info",
    "suseRegisterInfo",
    "python3-suseRegisterInfo",
    "zypp-plugin-spacewalk",
    "python3-zypp-plugin",
    "python3-zypp-plugin-spacewalk",
]

PKGLIST15_X86_ARM = [
    "dmidecode",
    "libunwind",
]

PKGLIST15_PPC = [
    "libunwind",
]

PKGLIST15_Z = [
]

PKGLISTUBUNTU1604 = [
    "libsodium18",
    "dctrl-tools",
    "libzmq5",
    "python-chardet",
    "python-croniter",
    "python-crypto",
    "python-dateutil",
    "python-enum34",
    "python-ipaddress",
    "python-jinja2",
    "python-markupsafe",
    "python-minimal",
    "python-msgpack",
    "python-openssl",
    "python-pkg-resources",
    "python-psutil",
    "python-requests",
    "python-six",
    "python-systemd",
    "python-tornado",
    "python-tz",
    "python-urllib3",
    "python-yaml",
    "python-zmq",
    "python-pycurl",
    "salt-common",
    "salt-minion",
    "dmidecode",
]

PKGLISTUBUNTU1804 = [
    "dctrl-tools",
    "javascript-common",
    "libjs-jquery",
    "libjs-sphinxdoc",
    "libjs-underscore",
    "libnorm1",
    "libpgm-5.2-0",
    "libpython3.6-stdlib",
    "libpython3.6-minimal",
    "libpython3.6-stdlib",
    "libsodium23",
    "libzmq5",
    "python3",
    "python3-apt",
    "python3-asn1crypto",
    "python3-certifi",
    "python3-cffi-backend",
    "python3-chardet",
    "python3-croniter",
    "python3-crypto",
    "python3-pycryptodome",
    "python3-cryptography",
    "python3-dateutil",
    "python3-idna",
    "python3-jinja2",
    "python3-markupsafe",
    "python3-minimal",
    "python3-msgpack",
    "python3-openssl",
    "python3-pkg-resources",
    "python3-psutil",
    "python3-requests",
    "python3-singledispatch",
    "python3-six",
    "python3-systemd",
    "python3-tornado",
    "python3-tz",
    "python3-urllib3",
    "python3-yaml",
    "python3-zmq",
    "python3.6",
    "python3.6-minimal",
    "salt-common",
    "salt-minion",
    "dmidecode",
    "bsdmainutils",
    "debconf-utils",
    "iso-codes",
    "python-apt-common",
    "python3-distro",
    "python3-gnupg",
    "gnupg",
]

PKGLISTUBUNTU2004 = [
    "dctrl-tools",
    "libnorm1",
    "libpgm-5.2-0",
    "libzmq5",
    "python3-crypto",
    "python3-dateutil",
    "python3-distro",
    "python3-jinja2",
    "python3-markupsafe",
    "python3-msgpack",
    "python3-psutil",
    "python3-pycryptodome",
    "python3-zmq",
    "salt-common",
    "salt-minion",
    "gnupg",
]

PKGLISTDEBIAN9 = [
    "apt-transport-https",
    "bsdmainutils",
    "dctrl-tools",
    "debconf-utils",
    "gnupg1",
    "gnupg1-curl",
    "gnupg1-l10n",
    "javascript-common",
    "libjs-jquery",
    "libjs-sphinxdoc",
    "libjs-underscore",
    "libpgm-5.2-0",
    "libpython-stdlib",
    "libpython2.7-minimal",
    "libpython2.7-stdlib",
    "libzmq5",
    "libsodium18",
    "libyaml-0-2",
    "libcurl3-gnutls",
    "python",
    "python-apt",
    "python-backports-abc",
    "python-certifi",
    "python-cffi-backend",
    "python-chardet",
    "python-concurrent.futures",
    "python-croniter",
    "python-crypto",
    "python-cryptography",
    "python-dateutil",
    "python-enum34",
    "python-gnupg",
    "python-idna",
    "python-ipaddress",
    "python-jinja2",
    "python-mako",
    "python-markupsafe",
    "python-minimal",
    "python-msgpack",
    "python-openssl",
    "python-pkg-resources",
    "python-psutil",
    "python-requests",
    "python-singledispatch",
    "python-six",
    "python-systemd",
    "python-tornado",
    "python-tz",
    "python-urllib3",
    "python-yaml",
    "python-zmq",
    "python2.7",
    "python2.7-minimal",
    "salt-common",
    "salt-minion",
    "dmidecode",
    "gnupg",
    "gnupg1",
]


PKGLISTDEBIAN10 = [
    "dctrl-tools",
    "debconf-utils",
    "dirmngr",
    "distro-info-data",
    "dmidecode",
    "gnupg",
    "gnupg-l10n",
    "gnupg-utils",
    "gpg",
    "gpg-agent",
    "gpgconf",
    "gpgsm",
    "gpg-wks-client",
    "gpg-wks-server",
    "iso-codes",
    "libassuan0",
    "libksba8",
    "libldap-2.4-2",
    "libldap-common",
    "libnorm1",
    "libnpth0",
    "libpgm-5.2-0",
    "libsasl2-2",
    "libsasl2-modules",
    "libsasl2-modules-db",
    "libsodium23",
    "libyaml-0-2",
    "libzmq5",
    "lsb-release",
    "pinentry-curses",
    "python3-apt",
    "python3-certifi",
    "python3-chardet",
    "python3-croniter",
    "python3-crypto",
    "python3-pycryptodome",
    "python3-dateutil",
    "python3-distro",
    "python3-idna",
    "python3-jinja2",
    "python3-markupsafe",
    "python3-msgpack",
    "python3-pkg-resources",
    "python3-psutil",
    "python3-requests",
    "python3-six",
    "python3-systemd",
    "python3-tz",
    "python3-urllib3",
    "python3-yaml",
    "python3-zmq",
    "python-apt-common",
    "salt-common",
    "salt-minion",
    "gnupg",
]

PKGLISTASTRALINUXOREL = [
    "dctrl-tools",
    "dirmngr",
    "iso-codes",
    "libjs-jquery",
    "libjs-sphinxdoc",
    "libjs-underscore",
    "libpgm-5.2-0",
    "libpython-stdlib",
    "libpython2.7-minimal",
    "libpython2.7-stdlib",
    "libsodium18",
    "libyaml-0-2",
    "libzmq5",
    "python",
    "python-apt",
    "python-apt-common",
    "python-backports-abc",
    "python-cffi-backend",
    "python-chardet",
    "python-concurrent.futures",
    "python-crypto",
    "python-cryptography",
    "python-dateutil",
    "python-enum34",
    "python-idna",
    "python-ipaddress",
    "python-jinja2",
    "python-markupsafe",
    "python-minimal",
    "python-msgpack",
    "python-openssl",
    "python-pkg-resources",
    "python-pyasn1",
    "python-psutil",
    "python-requests",
    "python-setuptools",
    "python-singledispatch",
    "python-six",
    "python-systemd",
    "python-tornado",
    "python-urllib3",
    "python-yaml",
    "python-zmq",
    "python2.7",
    "python2.7-minimal",
    "salt-common",
    "salt-minion",
    "gnupg",
]

DATA = {
    'SLE-11-SP1-i586' : {
        'PDID' : 684, 'PKGLIST' : PKGLIST11 + PKGLIST11_X86_I586,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/1/bootstrap/'
    },
    'SLE-11-SP1-ia64' : {
        'PDID' : 1033, 'PKGLIST' : PKGLIST11,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/1/bootstrap/'
    },
    'SLE-11-SP1-ppc64' : {
        'PDID' : 940, 'PKGLIST' : PKGLIST11,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/1/bootstrap/'
    },
    'SLE-11-SP1-s390x' : {
        'PDID' : 745, 'PKGLIST' : PKGLIST11,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/1/bootstrap/'
    },
    'SLE-11-SP1-x86_64' : {
        'PDID' : 769, 'PKGLIST' : PKGLIST11 + PKGLIST11_X86_I586,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/1/bootstrap/'
    },
    'SLE-11-SP2-i586' : {
        'PDID' : 811, 'PKGLIST' : PKGLIST11 + PKGLIST11_X86_I586,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/2/bootstrap/'
    },
    'SLE-11-SP2-ia64' : {
        'PDID' : 1034, 'PKGLIST' : PKGLIST11,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/2/bootstrap/'
    },
    'SLE-11-SP2-ppc64' : {
        'PDID' : 946, 'PKGLIST' : PKGLIST11,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/2/bootstrap/'
    },
    'SLE-11-SP2-s390x' : {
        'PDID' : 755, 'PKGLIST' : PKGLIST11,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/2/bootstrap/'
    },
    'SLE-11-SP2-x86_64' : {
        'PDID' : 690, 'PKGLIST' : PKGLIST11 + PKGLIST11_X86_I586,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/2/bootstrap/'
    },
    'SLE-11-SP3-i586' : {
        'PDID' : 793, 'PKGLIST' : PKGLIST11 + ENHANCE11 + PKGLIST11_X86_I586,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/3/bootstrap/'
    },
    'SLE-11-SP3-ia64' : {
        'PDID' : 1037, 'PKGLIST' : PKGLIST11 + ENHANCE11,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/3/bootstrap/'
    },
    'SLE-11-SP3-ppc64' : {
        'PDID' : 949, 'PKGLIST' : PKGLIST11 + ENHANCE11,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/3/bootstrap/'
    },
    'SLE-11-SP3-s390x' : {
        'PDID' : 693, 'PKGLIST' : PKGLIST11 + ENHANCE11,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/3/bootstrap/'
    },
    'SLE-11-SP3-x86_64' : {
        'PDID' : 814, 'PKGLIST' : PKGLIST11 + ENHANCE11 + PKGLIST11_X86_I586,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/3/bootstrap/'
    },
    'SLE-11-SP4-i586' : {
        'PDID' : [1299], 'BETAPDID' : [2071], 'PKGLIST' : PKGLIST11 + ENHANCE11 + PKGLIST11_X86_I586,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/4/bootstrap/'
    },
    'SLE-11-SP4-ia64' : {
        'PDID' : 1302, 'PKGLIST' : PKGLIST11 + ENHANCE11,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/4/bootstrap/'
    },
    'SLE-11-SP4-ppc64' : {
        'PDID' : [1301], 'BETAPDID' : [2072], 'PKGLIST' : PKGLIST11 + ENHANCE11,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/4/bootstrap/'
    },
    'SLE-11-SP4-s390x' : {
        'PDID' : [1303], 'BETAPDID' : [2073], 'PKGLIST' : PKGLIST11 + ENHANCE11,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/4/bootstrap/'
    },
    'SLE-11-SP4-x86_64' : {
        'PDID' : [1300], 'BETAPDID' : [2074], 'PKGLIST' : PKGLIST11 + ENHANCE11 + PKGLIST11_X86_I586,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/4/bootstrap/'
    },
    'SLE-10-SP3-i586' : {
        'PDID' : 785, 'PKGLIST' : PKGLIST10,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/10/3/bootstrap/'
    },
    'SLE-10-SP3-ia64' : {
        'PDID' : 740, 'PKGLIST' : PKGLIST10,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/10/3/bootstrap/'
    },
    'SLE-10-SP3-ppc' : {
        'PDID' : 787, 'PKGLIST' : PKGLIST10,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/10/3/bootstrap/'
    },
    'SLE-10-SP3-s390x' : {
        'PDID' : 682, 'PKGLIST' : PKGLIST10,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/10/3/bootstrap/'
    },
    'SLE-10-SP3-x86_64' : {
        'PDID' : 721, 'PKGLIST' : PKGLIST10,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/10/3/bootstrap/'
    },
    'SLE-10-SP4-i586' : {
        'PDID' : 752, 'PKGLIST' : PKGLIST10,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/10/4/bootstrap/'
    },
    'SLE-10-SP4-ia64' : {
        'PDID' : 770, 'PKGLIST' : PKGLIST10,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/10/4/bootstrap/'
    },
    'SLE-10-SP4-ppc' : {
        'PDID' : 711, 'PKGLIST' : PKGLIST10,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/10/4/bootstrap/'
    },
    'SLE-10-SP4-s390x' : {
        'PDID' : 771, 'PKGLIST' : PKGLIST10,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/10/4/bootstrap/'
    },
    'SLE-10-SP4-x86_64' : {
        'PDID' : 832, 'PKGLIST' : PKGLIST10,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/10/4/bootstrap/'
    },
    'SLES4SAP-11-SP1-x86_64' : {
        'PDID' : 1129, 'PKGLIST' : PKGLIST11 + PKGLIST11_X86_I586,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/1/bootstrap/'
    },
    'SLES4SAP-11-SP2-x86_64' : {
        'PDID' : 1130, 'PKGLIST' : PKGLIST11 + PKGLIST11_X86_I586,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/2/bootstrap/'
    },
    'SLES4SAP-11-SP3-x86_64' : {
        'PDID' : 1131, 'PKGLIST' : PKGLIST11 + ENHANCE11 + PKGLIST11_X86_I586,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/3/bootstrap/'
    },
    'SLES4SAP-11-SP4-x86_64' : {
        'PDID' : [1329], 'BETAPDID' : [2074], 'PKGLIST' : PKGLIST11 + ENHANCE11 + PKGLIST11_X86_I586,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/4/bootstrap/'
    },
    'SLES4SAP-11-SP4-ppc64' : {
        'PDID' : [1331], 'BETAPDID' : [2072], 'PKGLIST' : PKGLIST11 + ENHANCE11,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/4/bootstrap/'
    },
    'SLE-12-ppc64le' : {
        'PDID' : 1116, 'BETAPDID' : [1745], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/0/bootstrap/'
    },
    'SLE-12-s390x' : {
        'PDID' : 1115, 'BETAPDID' : [1746], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/0/bootstrap/'
    },
    'SLE-12-x86_64' : {
        'PDID' : 1117, 'BETAPDID' : [1747], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/0/bootstrap/'
    },
    'SLES4SAP-12-x86_64' : {
        'PDID' : 1319, 'BETAPDID' : [1747], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/0/1/bootstrap/'
    },
    'SLE-12-SP1-ppc64le' : {
        'PDID' : 1334, 'BETAPDID' : [1745], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/1/bootstrap/'
    },
    'SLE-12-SP1-s390x' : {
        'PDID' : [1335, 1535], 'BETAPDID' : [1746], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/1/bootstrap/'
    },
    'SLE-12-SP1-x86_64' : {
        'PDID' : [1322, 1533], 'BETAPDID' : [1747], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/1/bootstrap/'
    },
    'SLES4SAP-12-SP1-ppc64le' : {
        'PDID' : 1437, 'BETAPDID' : [1745], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/1/0/1/bootstrap/'
    },
    'SLES4SAP-12-SP1-x86_64' : {
        'PDID' : 1346, 'BETAPDID' : [1747], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/1/0/1/bootstrap/'
    },
    'RES6-x86_64' : {
        'PDID' : [1138], 'BETAPDID' : [2064], 'PKGLIST' : RES6,
        'DEST' : '/srv/www/htdocs/pub/repositories/res/6/bootstrap/'
    },
    'RES7-x86_64' : {
        'PDID' : [1251], 'BETAPDID' : [2065], 'PKGLIST' : RES7 + RES7_X86,
        'DEST' : '/srv/www/htdocs/pub/repositories/res/7/bootstrap/'
    },
    'SLE-12-SP2-aarch64' : {
        'PDID' : 1375, 'BETAPDID' : [1744], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/2/bootstrap/'
    },
    'SLES_RPI-12-SP2-aarch64' : {
        'PDID' : 1418, 'BETAPDID' : [1744], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/2/bootstrap/'
    },
    'SLE-12-SP2-ppc64le' : {
        'PDID' : [1355, 1737], 'BETAPDID' : [1745], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/2/bootstrap/'
    },
    'SLE-12-SP2-s390x' : {
        'PDID' : [1356, 1738], 'BETAPDID' : [1746], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/2/bootstrap/'
    },
    'SLE-12-SP2-x86_64' : {
        'PDID' : [1357, 1739], 'BETAPDID' : [1747], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/2/bootstrap/'
    },
    'SLES4SAP-12-SP2-x86_64' : {
        'PDID' : 1414, 'BETAPDID' : [1747], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/2/bootstrap/'
    },
    'SLES4SAP-12-SP2-ppc64le' : {
        'PDID' : 1521, 'BETAPDID' : [1745], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/2/bootstrap/'
    },
    'SLE-12-SP3-aarch64' : {
        'PDID' : [1424, 2002], 'BETAPDID' : [1744], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/3/bootstrap/'
    },
    'SLE-12-SP3-ppc64le' : {
        'PDID' : [1422, 1930], 'BETAPDID' : [1745], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/3/bootstrap/'
    },
    'SLE-12-SP3-s390x' : {
        'PDID' : [1423, 1931], 'BETAPDID' : [1746], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/3/bootstrap/'
    },
    'SLE-12-SP3-x86_64' : {
        'PDID' : [1421, 1932], 'BETAPDID' : [1747], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/3/bootstrap/'
    },
    'SLES4SAP-12-SP3-x86_64' : {
        'PDID' : 1426, 'BETAPDID' : [1747], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/3/bootstrap/'
    },
    'SLES4SAP-12-SP3-ppc64le' : {
        'PDID' : 1572, 'BETAPDID' : [1745], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/3/bootstrap/'
    },
    'SLE-12-SP4-aarch64' : {
        'PDID' : [1628, 2114], 'BETAPDID' : [1744], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/4/bootstrap/'
    },
    'SLE-12-SP4-ppc64le' : {
        'PDID' : [1626, 2115], 'BETAPDID' : [1745], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/4/bootstrap/'
    },
    'SLE-12-SP4-s390x' : {
        'PDID' : [1627, 2116], 'BETAPDID' : [1746], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/4/bootstrap/'
    },
    'SLE-12-SP4-x86_64' : {
        'PDID' : [1625, 2117], 'BETAPDID' : [1747], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/4/bootstrap/'
    },
    'SLED-12-SP4-x86_64' : {
        'PDID' : [1629], 'BETAPDID' : [1747], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/4/bootstrap/'
    },
    'SLES4SAP-12-SP4-x86_64' : {
        'PDID' : [1755], 'BETAPDID' : [1747], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/4/bootstrap/'
    },
    'SLES4SAP-12-SP4-ppc64le' : {
        'PDID' : [1754], 'BETAPDID' : [1745], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/4/bootstrap/'
    },
    'SLE4HPC-12-SP4-x86_64' : {
        'PDID' : [1759], 'BETAPDID' : [1747], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/4/bootstrap/'
    },
    'SLE4HPC-12-SP4-aarch64' : {
        'PDID' : [1758], 'BETAPDID' : [1744], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/4/bootstrap/'
    },
    'SLE-12-SP5-aarch64' : {
        'PDID' : [1875], 'BETAPDID' : [1744], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/5/bootstrap/'
    },
    'SLE-12-SP5-ppc64le' : {
        'PDID' : [1876], 'BETAPDID' : [1745], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/5/bootstrap/'
    },
    'SLE-12-SP5-s390x' : {
        'PDID' : [1877], 'BETAPDID' : [1746], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/5/bootstrap/'
    },
    'SLE-12-SP5-x86_64' : {
        'PDID' : [1878], 'BETAPDID' : [1747], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + ENHANCE12SP5_X86 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/5/bootstrap/'
    },
    'SLES4SAP-12-SP5-x86_64' : {
        'PDID' : [1880], 'BETAPDID' : [1747], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + ENHANCE12SP5_X86 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/5/bootstrap/'
    },
    'SLES4SAP-12-SP5-ppc64le' : {
        'PDID' : [1879], 'BETAPDID' : [1745], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/5/bootstrap/'
    },
    'SLE4HPC-12-SP5-x86_64' : {
        'PDID' : [1873], 'BETAPDID' : [1747], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + ENHANCE12SP5_X86 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/5/bootstrap/'
    },
    'SLE4HPC-12-SP5-aarch64' : {
        'PDID' : [1872], 'BETAPDID' : [1744], 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/5/bootstrap/'
    },
    'OES2018-x86_64' : {
        'PDID' : 45, 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/2/bootstrap/'
    },
    'OES2018-SP1-x86_64' : {
        'PDID' : 46, 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/3/bootstrap/'
    },
    'OES2018-SP2-x86_64' : {
        'PDID' : -9, 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/5/bootstrap/'
    },
    'OES2018-SP3-x86_64' : {
        'PDID' : -21, 'PKGLIST' : PKGLIST12 + ONLYSLE12 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/5/bootstrap/'
    },
    'SLE-15-aarch64' : {
        'PDID' : [1589, 2053, 1709], 'BETAPDID' : [1925], 'PKGLIST' : PKGLIST15_TRAD + ONLYSLE15 + PKGLIST15_SALT + PKGLIST15SP0SP1_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/15/0/bootstrap/'
    },
    'SLE-15-ppc64le' : {
        'PDID' : [1588, 2054, 1710], 'BETAPDID' : [1926], 'PKGLIST' : PKGLIST15_TRAD + ONLYSLE15 + PKGLIST15_SALT + PKGLIST15SP0SP1_SALT + PKGLIST15_PPC,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/15/0/bootstrap/'
    },
    'SLE-15-s390x' : {
        'PDID' : [1587, 2055, 1711], 'BETAPDID' : [1927], 'PKGLIST' : PKGLIST15_TRAD + ONLYSLE15 + PKGLIST15_SALT + PKGLIST15SP0SP1_SALT + PKGLIST15_Z,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/15/0/bootstrap/'
    },
    'SLE-15-x86_64' : {
        'PDID' : [1576, 2056, 1712], 'BETAPDID' : [1928], 'PKGLIST' : PKGLIST15_TRAD + ONLYSLE15 + PKGLIST15_SALT + PKGLIST15SP0SP1_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/15/0/bootstrap/'
    },
    'SLES4SAP-15-ppc64le' : {
        'PDID' : [1588, 1613, 1710], 'BETAPDID' : [1926], 'PKGLIST' : PKGLIST15_TRAD + ONLYSLE15 + PKGLIST15_SALT + PKGLIST15SP0SP1_SALT + PKGLIST15_PPC,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/15/0/bootstrap/'
    },
    'SLES4SAP-15-x86_64' : {
        'PDID' : [1576, 1612, 1712], 'BETAPDID' : [1928], 'PKGLIST' : PKGLIST15_TRAD + ONLYSLE15 + PKGLIST15_SALT + PKGLIST15SP0SP1_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/15/0/bootstrap/'
    },
    'SLE-15-SP1-aarch64' : {
        'PDID' : [1769, 1709], 'BETAPDID' : [1925], 'PKGLIST' : PKGLIST15_TRAD + ONLYSLE15 + PKGLIST15_SALT + PKGLIST15SP0SP1_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/15/1/bootstrap/'
    },
    'SLE-15-SP1-ppc64le' : {
        'PDID' : [1770, 1710], 'BETAPDID' : [1926], 'PKGLIST' : PKGLIST15_TRAD + ONLYSLE15 + PKGLIST15_SALT + PKGLIST15SP0SP1_SALT + PKGLIST15_PPC,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/15/1/bootstrap/'
    },
    'SLE-15-SP1-s390x' : {
        'PDID' : [1771, 1711], 'BETAPDID' : [1927], 'PKGLIST' : PKGLIST15_TRAD + ONLYSLE15 + PKGLIST15_SALT + PKGLIST15SP0SP1_SALT + PKGLIST15_Z,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/15/1/bootstrap/'
    },
    'SLE-15-SP1-x86_64' : {
        'PDID' : [1772, 1712], 'BETAPDID' : [1928], 'PKGLIST' : PKGLIST15_TRAD + ONLYSLE15 + PKGLIST15_SALT + PKGLIST15SP0SP1_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/15/1/bootstrap/'
    },
    'SUMA-40-PROXY-x86_64' : {
        'PDID' : [1772, 1908], 'BETAPDID' : [], 'PKGLIST' : PKGLIST15_TRAD + ONLYSLE15 + PKGLIST15_SALT + PKGLIST15SP0SP1_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/15/1/bootstrap/'
    },
    'SLE-15-SP2-aarch64' : {
        'PDID' : [1943, 1709], 'BETAPDID' : [1925], 'PKGLIST' : PKGLIST15_TRAD + ONLYSLE15 + PKGLIST15_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/15/2/bootstrap/'
    },
    'SLE-15-SP2-ppc64le' : {
        'PDID' : [1944, 1710], 'BETAPDID' : [1926], 'PKGLIST' : PKGLIST15_TRAD + ONLYSLE15 + PKGLIST15_SALT + PKGLIST15_PPC,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/15/2/bootstrap/'
    },
    'SLE-15-SP2-s390x' : {
        'PDID' : [1945, 1711], 'BETAPDID' : [1927], 'PKGLIST' : PKGLIST15_TRAD + ONLYSLE15 + PKGLIST15_SALT + PKGLIST15_Z,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/15/2/bootstrap/'
    },
    'SLE-15-SP2-x86_64' : {
        'PDID' : [1946, 1712], 'BETAPDID' : [1928], 'PKGLIST' : PKGLIST15_TRAD + ONLYSLE15 + PKGLIST15_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/15/2/bootstrap/'
    },
    'SUMA-41-PROXY-x86_64' : {
        'PDID' : [1946, 2015], 'BETAPDID' : [], 'PKGLIST' : PKGLIST15_TRAD + ONLYSLE15 + PKGLIST15_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/15/2/bootstrap/'
    },
    'SLE-15-SP3-aarch64' : {
        'PDID' : [2142, 1709], 'BETAPDID' : [1925], 'PKGLIST' : PKGLIST15_TRAD + ONLYSLE15 + PKGLIST15_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/15/3/bootstrap/'
    },
    'SLE-15-SP3-ppc64le' : {
        'PDID' : [2143, 1710], 'BETAPDID' : [1926], 'PKGLIST' : PKGLIST15_TRAD + ONLYSLE15 + PKGLIST15_SALT + PKGLIST15_PPC,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/15/3/bootstrap/'
    },
    'SLE-15-SP3-s390x' : {
        'PDID' : [2144, 1711], 'BETAPDID' : [1927], 'PKGLIST' : PKGLIST15_TRAD + ONLYSLE15 + PKGLIST15_SALT + PKGLIST15_Z,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/15/3/bootstrap/'
    },
    'SLE-15-SP3-x86_64' : {
        'PDID' : [2145, 1712], 'BETAPDID' : [1928], 'PKGLIST' : PKGLIST15_TRAD + ONLYSLE15 + PKGLIST15_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/15/3/bootstrap/'
    },
    'SUMA-42-PROXY-x86_64' : {
        'PDID' : [2145, 2225], 'BETAPDID' : [], 'PKGLIST' : PKGLIST15_TRAD + ONLYSLE15 + PKGLIST15_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/sle/15/3/bootstrap/'
    },
    'openSUSE-Leap-42.3-x86_64' : {
        'BASECHANNEL' : 'opensuse_leap42_3-x86_64', 'PKGLIST' : PKGLIST12 + ONLYOPENSUSE42 + ENHANCE12SP1 + PKGLIST12_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/opensuse/42/3/bootstrap/'
    },
    'openSUSE-Leap-15-x86_64' : {
        'BASECHANNEL' : 'opensuse_leap15_0-x86_64', 'PKGLIST' : PKGLIST15_TRAD + PKGLIST15_SALT + PKGLIST15SP0SP1_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/opensuse/15/0/bootstrap/'
    },
    'openSUSE-Leap-15.1-x86_64-uyuni' : {
        'BASECHANNEL' : 'opensuse_leap15_1-x86_64', 'PKGLIST' : PKGLIST15_TRAD + PKGLIST15_SALT + PKGLIST15SP0SP1_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/opensuse/15/1/bootstrap/'
    },
    'openSUSE-Leap-15.1-aarch64-uyuni' : {
        'BASECHANNEL' : 'opensuse_leap15_1-aarch64', 'PKGLIST' : PKGLIST15_TRAD + PKGLIST15_SALT + PKGLIST15SP0SP1_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/opensuse/15/1/bootstrap/'
    },
    'openSUSE-Leap-15.1-x86_64' : {
        'PDID' : [1929], 'PKGLIST' : PKGLIST15_SALT + PKGLIST15SP0SP1_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/opensuse/15/1/bootstrap/'
    },
    'openSUSE-Leap-15.2-x86_64' : {
        'PDID' : [2001], 'PKGLIST' : PKGLIST15_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/opensuse/15/2/bootstrap/'
    },
    'openSUSE-Leap-15.2-x86_64-uyuni' : {
        'BASECHANNEL' : 'opensuse_leap15_2-x86_64', 'PKGLIST' : PKGLIST15_TRAD + PKGLIST15_SALT + PKGLIST15SP0SP1_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/opensuse/15/2/bootstrap/'
    },
    'openSUSE-Leap-15.2-aarch64-uyuni' : {
        'BASECHANNEL' : 'opensuse_leap15_2-aarch64', 'PKGLIST' : PKGLIST15_TRAD + PKGLIST15_SALT + PKGLIST15SP0SP1_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/opensuse/15/2/bootstrap/'
    },
    'openSUSE-Leap-15.3-x86_64' : {
        'PDID' : [2236], 'PKGLIST' : PKGLIST15_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/opensuse/15/3/bootstrap/'
    },
    'openSUSE-Leap-15.3-aarch64' : {
        'PDID' : [2233], 'PKGLIST' : PKGLIST15_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/opensuse/15/3/bootstrap/'
    },
    'openSUSE-Leap-15.3-x86_64-uyuni' : {
        'BASECHANNEL' : 'opensuse_leap15_3-x86_64', 'PKGLIST' : PKGLIST15_TRAD + PKGLIST15_SALT + PKGLIST15SP0SP1_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/opensuse/15/3/bootstrap/'
    },
    'openSUSE-Leap-15.3-aarch64-uyuni' : {
        'BASECHANNEL' : 'opensuse_leap15_3-aarch64', 'PKGLIST' : PKGLIST15_TRAD + PKGLIST15_SALT + PKGLIST15SP0SP1_SALT + PKGLIST15_X86_ARM,
        'DEST' : '/srv/www/htdocs/pub/repositories/opensuse/15/3/bootstrap/'
    },
    'centos-6-x86_64' : {
        'PDID' : [-11, 1682], 'BETAPDID' : [2064], 'PKGLIST' : RES6,
        'DEST' : '/srv/www/htdocs/pub/repositories/centos/6/bootstrap/'
    },
    'centos-7-x86_64' : {
        'PDID' : [-12, 1683], 'BETAPDID' : [2065], 'PKGLIST' : RES7 + RES7_X86,
        'DEST' : '/srv/www/htdocs/pub/repositories/centos/7/bootstrap/'
    },
    'centos-7-aarch64' : {
        'PDID' : [-31, 2361], 'BETAPDID' : [2363], 'PKGLIST' : RES7,
        'DEST' : '/srv/www/htdocs/pub/repositories/centos/7/bootstrap/'
    },
    'centos-8-x86_64' : {
        'PDID' : [-13, 2007], 'BETAPDID' : [2066], 'PKGLIST' : RES8 + RES8_X86,
        'DEST' : '/srv/www/htdocs/pub/repositories/centos/8/bootstrap/'
    },
    'centos-8-aarch64' : {
        'PDID' : [-30, 2362], 'BETAPDID' : [2364], 'PKGLIST' : RES8,
        'DEST' : '/srv/www/htdocs/pub/repositories/centos/8/bootstrap/'
    },
    'centos-6-x86_64-uyuni' : {
        'BASECHANNEL' : 'centos6-x86_64', 'PKGLIST' : RES6,
        'DEST' : '/srv/www/htdocs/pub/repositories/centos/6/bootstrap/'
    },
    'centos-7-x86_64-uyuni' : {
        'BASECHANNEL' : 'centos7-x86_64', 'PKGLIST' : RES7 + RES7_X86,
        'DEST' : '/srv/www/htdocs/pub/repositories/centos/7/bootstrap/'
    },
    'centos-7-ppc64le-uyuni' : {
        'BASECHANNEL' : 'centos7-ppc64le', 'PKGLIST' : RES7,
        'DEST' : '/srv/www/htdocs/pub/repositories/centos/7/bootstrap/'
    },
    'centos-7-aarch64-uyuni' : {
        'BASECHANNEL' : 'centos7-aarch64', 'PKGLIST' : RES7,
        'DEST' : '/srv/www/htdocs/pub/repositories/centos/7/bootstrap/'
    },
    'centos-8-x86_64-uyuni' : {
        'BASECHANNEL' : 'centos8-x86_64', 'PKGLIST' : RES8 + RES8_X86,
        'DEST' : '/srv/www/htdocs/pub/repositories/centos/8/bootstrap/'
    },
    'centos-8-ppc64le-uyuni' : {
        'BASECHANNEL' : 'centos8-ppc64le', 'PKGLIST' : RES8,
        'DEST' : '/srv/www/htdocs/pub/repositories/centos/8/bootstrap/'
    },
    'centos-8-aarch64-uyuni' : {
        'BASECHANNEL' : 'centos8-aarch64', 'PKGLIST' : RES8,
        'DEST' : '/srv/www/htdocs/pub/repositories/centos/8/bootstrap/'
    },
    'oracle-6-x86_64' : {
        'PDID' : [-15, 1682], 'BETAPDID' : [2064], 'PKGLIST' : RES6,
        'DEST' : '/srv/www/htdocs/pub/repositories/oracle/6/bootstrap/'
    },
    'oracle-7-x86_64' : {
        'PDID' : [-14, 1683], 'BETAPDID' : [2065], 'PKGLIST' : RES7 + RES7_X86,
        'DEST' : '/srv/www/htdocs/pub/repositories/oracle/7/bootstrap/'
    },
    'oracle-7-aarch64' : {
        'PDID' : [-28, 2361], 'BETAPDID' : [2363], 'PKGLIST' : RES7,
        'DEST' : '/srv/www/htdocs/pub/repositories/oracle/7/bootstrap/'
    },
    'oracle-8-x86_64' : {
        'PDID' : [-17, 2007], 'BETAPDID' : [2066], 'PKGLIST' : RES8 + RES8_X86,
        'DEST' : '/srv/www/htdocs/pub/repositories/oracle/8/bootstrap/'
    },
    'oracle-8-aarch64' : {
        'PDID' : [-29, 2362], 'BETAPDID' : [2364], 'PKGLIST' : RES8,
        'DEST' : '/srv/www/htdocs/pub/repositories/oracle/8/bootstrap/'
    },
    'oracle-6-x86_64-uyuni' : {
        'BASECHANNEL' : 'oraclelinux6-x86_64', 'PKGLIST' : RES6,
        'DEST' : '/srv/www/htdocs/pub/repositories/oracle/6/bootstrap/'
    },
    'oracle-7-x86_64-uyuni' : {
        'BASECHANNEL' : 'oraclelinux7-x86_64', 'PKGLIST' : RES7 + RES7_X86,
        'DEST' : '/srv/www/htdocs/pub/repositories/oracle/7/bootstrap/'
    },
    'oracle-7-aarch64-uyuni' : {
        'BASECHANNEL' : 'oraclelinux7-aarch64', 'PKGLIST' : RES7 + RES7_X86,
        'DEST' : '/srv/www/htdocs/pub/repositories/oracle/7/bootstrap/'
    },
    'oracle-8-x86_64-uyuni' : {
        'BASECHANNEL' : 'oraclelinux8-x86_64', 'PKGLIST' : RES8 + RES8_X86,
        'DEST' : '/srv/www/htdocs/pub/repositories/oracle/8/bootstrap/'
    },
    'oracle-8-aarch64-uyuni' : {
        'BASECHANNEL' : 'oraclelinux8-aarch64', 'PKGLIST' : RES8,
        'DEST' : '/srv/www/htdocs/pub/repositories/oracle/8/bootstrap/'
    },
    'amazonlinux-2-x86_64' : {
        'PDID' : [-22, 1683], 'BETAPDID' : [2065], 'PKGLIST' : RES7 + RES7_X86 + AMAZONLINUX2,
        'DEST' : '/srv/www/htdocs/pub/repositories/amzn/2/bootstrap/'
    },
    'amazonlinux-2-aarch64' : {
        'PDID' : [-28, 2361], 'BETAPDID' : [2363], 'PKGLIST' : RES7 + AMAZONLINUX2,
        'DEST' : '/srv/www/htdocs/pub/repositories/amzn/2/bootstrap/'
    },
    'amazonlinux-2-x86_64-uyuni' : {
        'BASECHANNEL' : 'amazonlinux2-core-x86_64', 'PKGLIST' : RES7 + RES7_X86 + AMAZONLINUX2,
        'DEST' : '/srv/www/htdocs/pub/repositories/amzn/2/bootstrap/'
    },
    'amazonlinux-2-aarch64-uyuni' : {
        'BASECHANNEL' : 'amazonlinux2-core-aarch64', 'PKGLIST' : RES7 + AMAZONLINUX2,
        'DEST' : '/srv/www/htdocs/pub/repositories/amzn/2/bootstrap/'
    },
    'RHEL6-x86_64' : {
        'PDID' : [-5, 1682], 'BETAPDID' : [2064], 'PKGLIST' : RES6,
        'DEST' : '/srv/www/htdocs/pub/repositories/res/6/bootstrap/'
    },
    'RHEL6-i386' : {
        'PDID' : [-6, 1681], 'BETAPDID' : [2063], 'PKGLIST' : RES6,
        'DEST' : '/srv/www/htdocs/pub/repositories/res/6/bootstrap/'
    },
    'RHEL7-x86_64' : {
        'PDID' : [-7, 1683], 'BETAPDID' : [2065], 'PKGLIST' : RES7 + RES7_X86,
        'DEST' : '/srv/www/htdocs/pub/repositories/res/7/bootstrap/'
    },
    'SLE-ES8-x86_64' : {
        'PDID' : [-8, 1921, 2007], 'BETAPDID' : [2066], 'PKGLIST' : RES8 + RES8_X86,
        'DEST' : '/srv/www/htdocs/pub/repositories/res/8/bootstrap/'
    },
    'RHEL8-x86_64' : {
        'PDID' : [-8, 2007], 'BETAPDID' : [2066], 'PKGLIST' : RES8 + RES8_X86,
        'DEST' : '/srv/www/htdocs/pub/repositories/res/8/bootstrap/'
    },
    'alibaba-2-x86_64-uyuni': {
        'BASECHANNEL': 'alibaba-2-x86_64', 'PKGLIST': RES7 + RES7_X86,
        'DEST': '/srv/www/htdocs/pub/repositories/alibaba/2/bootstrap/'
    },
    'alibaba-2-aarch64-uyuni': {
        'BASECHANNEL': 'alibaba-2-aarch64', 'PKGLIST': RES7,
        'DEST': '/srv/www/htdocs/pub/repositories/alibaba/2/bootstrap/'
    },
    'almalinux-8-x86_64' : {
        'PDID' : [-23, 2007], 'BETAPDID' : [2066], 'PKGLIST' : RES8 + RES8_X86,
        'DEST' : '/srv/www/htdocs/pub/repositories/almalinux/8/bootstrap/'
    },
    'almalinux-8-aarch64' : {
        'PDID' : [-26, 2362], 'BETAPDID' : [2364], 'PKGLIST' : RES8,
        'DEST' : '/srv/www/htdocs/pub/repositories/almalinux/8/bootstrap/'
    },    
    'almalinux-8-x86_64-uyuni' : {
        'BASECHANNEL' : 'almalinux8-x86_64', 'PKGLIST' : RES8 + RES8_X86,
        'DEST' : '/srv/www/htdocs/pub/repositories/almalinux/8/bootstrap/'
    },    
    'rockylinux-8-x86_64' : {
        'PDID' : [-24, 2007], 'BETAPDID' : [2066], 'PKGLIST' : RES8 + RES8_X86,
        'DEST' : '/srv/www/htdocs/pub/repositories/rockylinux/8/bootstrap/'
    },
    'rockylinux-8-aarch64' : {
        'PDID' : [-27, 2362], 'BETAPDID' : [2364], 'PKGLIST' : RES8,
        'DEST' : '/srv/www/htdocs/pub/repositories/rockylinux/8/bootstrap/'
    },
    'rockylinux-8-x86_64-uyuni' : {
        'BASECHANNEL' : 'rockylinux8-x86_64', 'PKGLIST' : RES8 + RES8_X86,
        'DEST' : '/srv/www/htdocs/pub/repositories/rockylinux/8/bootstrap/'
    },
    'rockylinux-8-aarch64-uyuni' : {
        'BASECHANNEL' : 'rockylinux8-aarch64', 'PKGLIST' : RES8,
        'DEST' : '/srv/www/htdocs/pub/repositories/rockylinux/8/bootstrap/'
    },
    'ubuntu-16.04-amd64' : {
        'PDID' : [-2, 1917], 'BETAPDID' : [2061], 'PKGLIST' : PKGLISTUBUNTU1604,
        'DEST' : '/srv/www/htdocs/pub/repositories/ubuntu/16/4/bootstrap/',
        'TYPE' : 'deb'
    },
    'ubuntu-18.04-amd64' : {
        'PDID' : [-1, 1918], 'BETAPDID' : [2062], 'PKGLIST' : PKGLISTUBUNTU1804,
        'DEST' : '/srv/www/htdocs/pub/repositories/ubuntu/18/4/bootstrap/',
        'TYPE' : 'deb'
    },
    'ubuntu-20.04-amd64' : {
        'PDID' : [-18, 2113], 'BETAPDID' : [2112], 'PKGLIST' : PKGLISTUBUNTU2004,
        'DEST' : '/srv/www/htdocs/pub/repositories/ubuntu/20/4/bootstrap/',
        'TYPE' : 'deb'
    },
    'ubuntu-16.04-amd64-uyuni' : {
        'BASECHANNEL' : 'ubuntu-16.04-pool-amd64-uyuni', 'PKGLIST' : PKGLISTUBUNTU1604,
        'DEST' : '/srv/www/htdocs/pub/repositories/ubuntu/16/4/bootstrap/',
        'TYPE' : 'deb'
    },
    'ubuntu-18.04-amd64-uyuni' : {
        'BASECHANNEL' : 'ubuntu-18.04-pool-amd64-uyuni', 'PKGLIST' : PKGLISTUBUNTU1804,
        'DEST' : '/srv/www/htdocs/pub/repositories/ubuntu/18/4/bootstrap/',
        'TYPE' : 'deb'
    },
    'ubuntu-20.04-amd64-uyuni' : {
        'BASECHANNEL' : 'ubuntu-20.04-pool-amd64-uyuni', 'PKGLIST' : PKGLISTUBUNTU2004,
        'DEST' : '/srv/www/htdocs/pub/repositories/ubuntu/20/4/bootstrap/',
        'TYPE' : 'deb'
    },
    'debian9-amd64' : {
        'PDID' : [-19, 2208], 'BETAPDID' : [2209], 'PKGLIST' : PKGLISTDEBIAN9,
        'DEST' : '/srv/www/htdocs/pub/repositories/debian/9/bootstrap/',
        'TYPE' : 'deb'
    },
    'debian10-amd64' : {
        'PDID' : [-20, 2210], 'BETAPDID' : [2211], 'PKGLIST' : PKGLISTDEBIAN10,
        'DEST' : '/srv/www/htdocs/pub/repositories/debian/10/bootstrap/',
        'TYPE' : 'deb'
    },
    'debian9-amd64-uyuni' : {
         'BASECHANNEL' : 'debian-9-pool-amd64-uyuni', 'PKGLIST' : PKGLISTDEBIAN9,
         'DEST' : '/srv/www/htdocs/pub/repositories/debian/9/bootstrap/',
         'TYPE' : 'deb'
     },
     'debian10-amd64-uyuni' : {
         'BASECHANNEL' : 'debian-10-pool-amd64-uyuni', 'PKGLIST' : PKGLISTDEBIAN10,
         'DEST' : '/srv/www/htdocs/pub/repositories/debian/10/bootstrap/',
         'TYPE' : 'deb'
     },
     'astralinux-orel-amd64': {
         'BASECHANNEL' : 'astralinux-orel-pool-amd64', 'PKGLIST' : PKGLISTASTRALINUXOREL,
         'DEST' : '/srv/www/htdocs/pub/repositories/astra/orel/bootstrap/',
         'TYPE' : 'deb'
     }
}
