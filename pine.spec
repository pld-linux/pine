Summary:     MIME compliant mail reader w/ news support as well
Summary(de): MIME-konformer Mail-Reader mit News-Support 
Summary(fr): Lecteur de courrier conforme à MIME avec gestion des news"
Summary(tr): MIME uyumlu ileti okuyucusu (haber servisi desteði de vardýr)
Name:        pine
Version:     4.02A
Release:     3
Copyright:   distributable
URL:         http://www.washington.edu/pine
Group:       Applications/Mail
Source0:     ftp://ftp.cac.washington.edu/pine/%{name}4.02.tar.gz
Source1:     pine.wmconfig
Patch0:      pine-4.02-glibc.patch
Patch1:      pine-4.02-filter.patch
Patch2:      pine4.02A.patch
Patch3:      pine-config.patch
Requires:    mailcap
Buildroot:   /tmp/%{name}-%{version}-root

%description
Pine is a very full featured text based mail and news client. It is
aimed at both novice and expert users. It includes an easy to use editor,
pico, for composing messages. Pico has gained popularity as a stand
alone text editor in it's own right. It features MIME support, address
books, and support for IMAP, mail, and MH style folders.

%description -l de
Pine ist ein kompletter textbasierender Mail- und New-Client, der sich 
sowohl an Neueinsteiger als auch an Experten richtet. Er umfaßt einen 
einfachen Editor (Pico), der zum Verfassen der Nachrichten dient, sich 
jedoch inzwischen einen Namen als autonomer Texteditor gemacht hat. Pine
unterstützt MIME, Adreßbücher, IMAP, Mail- und HM-Ordner. 

%description -l fr
pine est un client courrier et news très complet en mode texte. Il est
destiné aux débutants comme aux experts. Il comprend un éditeur simple à
utiliser, pico, pour composer les messages. pico est devenu populaire comme
éditeur de texte par lui-même. Il reconnait la gestion MIME, les carnets
d'adresse et la gestion IMAP, mail et des dossiers du style MH.

%description -l tr
Pine, metin tabanlý bir ileti ve haber servisi (news) istemcisidir. Hem acemi
hem de uzman kullanýcýlar için uygundur. Ýleti yazmak için kullanýmý oldukça
kolay olan pico adlý metin düzenleyicisini kullanýr. Pico kendi baþýna da bir
metin düzenleyici olarak ilgi görmüþtür. Pine, MIME desteði, adres defteri ve
IMAP, MH gibi ileti arþivi biçimlerini destekleme özelliklerini taþýr.

%prep
%setup -q -n pine4.02
%patch0 -p1 -b .glibc
%patch1 -p1 -b .filter
%patch2 -p1 -b .pat402A
%patch3 -p1 -b .config

%build
./build CC="egcs -DIGNORE_LOCK_EACCES_ERRORS" DEBUG="$RPM_OPT_FLAGS" lnx

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{usr/{bin,man/man1},etc/X11/wmconfig}

install -s bin/{pine,pico,pilot} $RPM_BUILD_ROOT/usr/bin

install doc/{pine,pico,pilot}.1 $RPM_BUILD_ROOT/usr/man/man1

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/pine

$RPM_BUILD_ROOT/usr/bin/pine -conf > $RPM_BUILD_ROOT/etc/pine.conf
cat <<EOF > $RPM_BUILD_ROOT/etc/pine.conf.fixed
#
# Pine system-wide enforced configuration file - customize as needed
#
# This file holds the system-wide enforced values for pine configuration
# settings. Any values set in it will override values set in the
# system-wide default configuration file (/etc/pine.conf) and
# the user's own configuration file (~/.pinerc).
# For more information on the format of this file, read the
# comments at the top of /etc/pine.conf

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README CPYRIGHT doc/*.txt doc/tech-notes doc/mailcap.unx
%config(missingok) /etc/X11/wmconfig/pine
%config /etc/pine.conf*
%attr(2755, root, mail) /usr/bin/pine
%attr(0755, root, root) /usr/bin/pico
%attr(0755, root, root) /usr/bin/pilot
%attr(0644, root,  man) /usr/man/man1/*

%changelog
* Mon Aug 31 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.02A-3]
- Buildroot changed to /tmp/%%{name}-%%{version}-root,
- added %defattr and %attr macros in %files (allows building package from
  non-root account),
- added using %%{name} macro %%{version} in Source and %setup,
- added %clean section,
- added "Requires: mailcap" and removed %config /usr/lib/mime.types,
- pine.conf* files moved to /etc,
- removed -DDEBUG compile time option,
- all stuff linked against libncurses instead libtermcap,
- simplification in %install,
- initial pine.conf file maked from output "pine -conf",
- removed doc/pine-ports and contrib from %doc
- fixed passing $RPM_OPT_FLAGS
- replaced "mkdir -p" with "install -d" in %install.

* Fri Aug 14 1998 Jeff Johnson <jbj@redhat.com>
- patch to 4.02A.
- disable stupid EACCESS warnings.

* Wed Jul 22 1998 Jeff Johnson <jbj@redhat.com>
- update to 4.02.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jan 15 1998 Erik Troan <ewt@redhat.com>
- added patch to fix pine filters

* Tue Dec 30 1997 Erik Troan <ewt@redhat.com>
- fixed resizing in pine and pico

* Thu Dec 18 1997 Erik Troan <ewt@redhat.com>
- removed patch for SIGCHLD race -- it shouldn't be necessary
- added patch to avoid longjmp() from SIGCHLD handler -- SIGCHLD handling
  is sane now

* Thu Dec 11 1997 Cristian Gafton <gafton@redhat.com>
- added a patch for handling a SIGCHLD race condition

* Tue Nov 04 1997 Erik Troan <ewt@redhat.com>
- fix for locks w/ long st_dev field
- use termios rather then termio

* Wed Oct 29 1997 Donnie Barnes <djb@redhat.com>
- added wmconfig entry

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- removed exec bit from /usr/doc/pine-3.96-1/contrib/utils/pwd2pine
