Summary:	MIME compliant mail reader w/ news support as well
Summary(pl):	Klient poczty elektronicznej i newsów ze wspomaganiem dla MIME
Summary(de):	MIME-konformer Mail-Reader mit News-Support 
Summary(fr):	Lecteur de courrier conforme à MIME avec gestion des news"
Summary(tr):	MIME uyumlu ileti okuyucusu (haber servisi desteði de vardýr)
Name:		pine
Version:	4.10
Release:	1d
Copyright:	distributable
URL:		http://www.washington.edu/pine
Group:		Applications/Mail
Group(pl):	Aplikacje/Poczta
Source0:	ftp://ftp.cac.washington.edu/pine/%{name}%{version}.tar.gz
Source1:	pine.wmconfig
Patch0:		pine-config.patch
Patch1:		pine-doc.patch
Patch2:		pine-gssapi.patch
Patch3:		pine-makefile.patch
Patch4:		pine-terminfo.patch
Patch5:		pine-nodebug.patch
Patch6:		pine-unix.patch
Patch7:		pine-noroot.patch
Requires:	mailcap
Requires:	krb5-lib >= 1.0.5
Buildroot:	/tmp/%{name}-%{version}-root

%description
Pine is a very full featured text based mail and news client. It is
aimed at both novice and expert users. It includes an easy to use editor,
pico, for composing messages. Pico has gained popularity as a stand
alone text editor in it's own right. It features MIME support, address
books, and support for IMAP, mail, and MH style folders.

%description -l pl
Pine jest doskona³ym czytnikiem poczty elektronicznej i newsów, prcuj±cym w
trybie tekstowym. W pakiecie znajduje siê równie¿ ³atwy w u¿yciu edytor pico,
wykorzystywany do pisania wiadomo¶ci. Pine jest obecnie jednym z najbardziej 
popularnych czytników poczty elektronicznej, posiada wspomaganie dla MIME i 
IMAP, mo¿na w ³atwy sposób tworzyæ ksi±¿ki adresowe i skonfigurowaæ go do 
wspó³pracy z aplkikacj± PGP.

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
%setup -q -n %{name}%{version}
%patch0 -p1 
%patch1 -p1 
#%patch2 -p1 
%patch3 -p1 
%patch4 -p1 
%patch5 -p1 
%patch6 -p1 
%patch7 -p1 

%build
# Checking for Kerberos V
if [ -f /etc/kerberos/krb5.conf ]; then
patch -p1 < $RPM_SOURCE_DIR/%{name}-gssapi.patch
install -d krb5
ln -s /usr/lib krb5/lib
ln -s /usr/include krb5/include
fi

./build \
    OPTIMIZE="$RPM_OPT_FLAGS" \
    slx

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{usr/{bin,man/man1},etc/{pine,X11/wmconfig}}

install -s bin/{pine,pico,pilot} $RPM_BUILD_ROOT/usr/bin

install doc/{pine,pico,pilot}.1 $RPM_BUILD_ROOT/usr/man/man1

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/pine

$RPM_BUILD_ROOT/usr/bin/pine -conf > $RPM_BUILD_ROOT/etc/pine/pine.conf
cat <<EOF > $RPM_BUILD_ROOT/etc/pine/pine.conf.fixed
#
# Pine system-wide enforced configuration file - customize as needed
#
# This file holds the system-wide enforced values for pine configuration
# settings. Any values set in it will override values set in the
# system-wide default configuration file (/etc/pine/pine.conf) and
# the user's own configuration file (~/.pinerc).
# For more information on the format of this file, read the
# comments at the top of /etc/pine/pine.conf

EOF

bzip2 -9  README doc/*.txt doc/mailcap.unx
gzip -9fn $RPM_BUILD_ROOT/usr/man/man1/* 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.bz2 doc/*.txt.bz2 doc/tech-notes/*.html doc/mailcap.unx.bz2

%config(missingok) /etc/X11/wmconfig/pine

%dir /etc/pine

%config %verify(not size mtime md5) /etc/pine/pine.conf*

%attr(755,root,root) /usr/bin/pi*
%attr(644,root, man) /usr/man/man1/*

%changelog
* Mon Oct 26 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [4.05-1d]
- updated tp 4.05,
- minor changes.

* Sun Sep 13 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [4.02-3d]
- translation modified for pl,
- fixed files permissions,
- %veryfi(not size mtime md5) macro for /etc/pine/pine.conf*,
- macro %setup -q -n %%{name}%%{version},  
- build against glibc-2.1,
- macro %%{name}%%{version} in Sorce,
- pine.conf* files moved to /etc/pine,
- build with Kerberos V5 support.

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
