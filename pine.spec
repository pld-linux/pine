Summary:	MIME compliant mail reader w/ news support as well
Summary(de):	MIME-konformer Mail-Reader mit News-Support 
Summary(fr):	Lecteur de courrier conforme à MIME avec gestion des news"
Summary(pl):	Klient poczty elektronicznej i newsów ze wspomaganiem dla MIME
Summary(tr):	MIME uyumlu ileti okuyucusu (haber servisi desteði de vardýr)
Name:		pine
Version:	4.21
Release:	5
Copyright:	distributable
Group:		Applications/Mail
Group(pt):	Aplicações/Correio Eletrônico
Group(pl):	Aplikacje/Poczta
Source0:	ftp://ftp.cac.washington.edu/pine/%{name}%{version}.tar.gz
Source1:	pine.desktop
Source2:	pine.1.pl
Patch0:		pine-config.patch
Patch1:		pine-doc.patch
Patch2:		pine-makefile.patch
Patch3:		pine-terminfo.patch
Patch4:		pine-nodebug.patch
Patch5:		pine-unix.patch
Patch6:		pine-filter.patch
Patch7:		pine-quote.patch
Patch8:		pine-noflock.patch
Patch9:		pine-fhs.patch
Patch10:	pine-maildir.patch
URL:		http://www.washington.edu/pine/
BuildRequires:	ncurses-devel >= 5.0
Requires:	mailcap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pine is a very full featured text based mail and news client. It is
aimed at both novice and expert users. It includes an easy to use
editor, pico, for composing messages. Pico has gained popularity as a
stand alone text editor in it's own right. It features MIME support,
address books, and support for IMAP, mail, and MH style folders.

%description -l de
Pine ist ein kompletter textbasierender Mail- und New-Client, der sich
sowohl an Neueinsteiger als auch an Experten richtet. Er umfaßt einen
einfachen Editor (Pico), der zum Verfassen der Nachrichten dient, sich
jedoch inzwischen einen Namen als autonomer Texteditor gemacht hat.
Pine unterstützt MIME, Adreßbücher, IMAP, Mail- und HM-Ordner.

%description -l fr
pine est un client courrier et news très complet en mode texte. Il est
destiné aux débutants comme aux experts. Il comprend un éditeur simple
à utiliser, pico, pour composer les messages. pico est devenu
populaire comme éditeur de texte par lui-même. Il reconnait la gestion
MIME, les carnets d'adresse et la gestion IMAP, mail et des dossiers
du style MH.

%description -l pl
Pine jest doskona³ym czytnikiem poczty elektronicznej i newsów,
pracuj±cym w trybie tekstowym. W pakiecie znajduje siê równie¿ ³atwy w
u¿yciu edytor pico, wykorzystywany do pisania wiadomo¶ci. Pine jest
obecnie jednym z najbardziej popularnych czytników poczty
elektronicznej, posiada wspomaganie dla MIME i IMAP, mo¿na w ³atwy
sposób tworzyæ ksi±¿ki adresowe i skonfigurowaæ go do wspó³pracy z
aplikacj± PGP.

%description -l tr
Pine, metin tabanlý bir ileti ve haber servisi (news) istemcisidir.
Hem acemi hem de uzman kullanýcýlar için uygundur. Ýleti yazmak için
kullanýmý oldukça kolay olan pico adlý metin düzenleyicisini kullanýr.
Pico kendi baþýna da bir metin düzenleyici olarak ilgi görmüþtür.
Pine, MIME desteði, adres defteri ve IMAP, MH gibi ileti arþivi
biçimlerini destekleme özelliklerini taþýr.

%prep
%setup   -q -n %{name}%{version}
%patch0  -p1 
%patch1  -p1 
%patch2  -p1 
%patch3  -p1 
%patch4  -p1 
%patch5  -p1 
%patch6  -p1 
%patch7  -p1 
%patch8  -p1 
%patch9  -p1 
%patch10 -p1 

%build
./build slx \
	OPTIMIZE="$RPM_OPT_FLAGS" \
	BASECFLAGS="$RPM_OPT_FLAGS -DNFSKLUDGE" \
	DEBUG=""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{man1,pl/man1}} \
$RPM_BUILD_ROOT{%{_applnkdir}/Network/Mail,%{_sysconfdir}}

install -s bin/{pine,pico,pilot} $RPM_BUILD_ROOT%{_bindir}

install doc/{pine,pico,pilot}.1 $RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/pl/man1/pine.1

$RPM_BUILD_ROOT%{_bindir}/pine -conf > $RPM_BUILD_ROOT%{_sysconfdir}/pine.conf
cat <<EOF > $RPM_BUILD_ROOT%{_sysconfdir}/pine.conf.fixed
#
# Pine system-wide enforced configuration file - customize as needed
#
# This file holds the system-wide enforced values for pine configuration
# settings. Any values set in it will override values set in the
# system-wide default configuration file (%{_sysconfdir}/pine/pine.conf) and
# the user's own configuration file (~/.pinerc).
# For more information on the format of this file, read the
# comments at the top of %{_sysconfdir}/pine.conf

EOF

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/{man1/*,pl/man1/*} \
	README doc/*.txt doc/mailcap.unx 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,doc/*.txt,doc/mailcap.unx}.gz
%doc doc/tech-notes/*.html

%{_applnkdir}/Network/Mail/pine.desktop

%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/pine.conf

%attr(755,root,root) %{_bindir}/pi*
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*
