Summary:	MIME compliant mail reader w/ news support as well
Summary(de):	MIME-konformer Mail-Reader mit News-Support 
Summary(fr):	Lecteur de courrier conforme à MIME avec gestion des news"
Summary(pl):	Klient poczty elektronicznej i newsów ze wspomaganiem dla MIME
Summary(tr):	MIME uyumlu ileti okuyucusu (haber servisi desteði de vardýr)
Name:		pine
Version:	4.44
Release:	1
License:	distributable
Group:		Applications/Mail
Source0:	ftp://ftp.cac.washington.edu/pine/%{name}%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-config.patch
Patch1:		%{name}-doc.patch
Patch2:		%{name}-makefile.patch
Patch3:		%{name}-terminfo.patch
Patch4:		%{name}-nodebug.patch
Patch5:		%{name}-unix.patch
Patch6:		%{name}-filter.patch
Patch7:		%{name}-quote.patch
Patch8:		%{name}-fhs.patch
Patch9:		%{name}-maildir.patch
Patch10:	%{name}-maildirfix.patch
Patch11:	%{name}-time.patch
Patch12:	%{name}-segfix.patch
Patch13:	%{name}-whitespace.patch
Patch14:	%{name}-libc-client.patch
Patch15:	%{name}-fixhome.patch
Patch16:	%{name}-terminit.patch
Patch17:	%{name}-ssl.patch
Patch18:	%{name}-non_english_man_path_fix.patch
URL:		http://www.washington.edu/pine/
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	openssl-devel
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
%setup   -q -a3 -n %{name}%{version}
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
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
#%patch16 -p1
%patch17 -p1
%patch18 -p1 

%build
./build slx \
	OPTIMIZE="%{rpmcflags}" \
	BASECFLAGS="%{rpmcflags} -DNFSKLUDGE" \
	SSLTYPE="unix" \
	DEBUG="" \
	CC="%{__cc}"

echo "%{__cc}" > ~/gcc.info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{man1,{es,fi,hu,pl}/man1}} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Network/Mail,%{_pixmapsdir},%{_sysconfdir}}

install bin/{pine,pico,pilot} $RPM_BUILD_ROOT%{_bindir}

install doc/{pine,pico,pilot}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install es/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/es/man1
install fi/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/fi/man1
install hu/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/hu/man1
install pl/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/pl/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

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

gzip -9nf README doc/*.txt doc/mailcap.unx 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,doc/*.txt,doc/mailcap.unx}.gz
%doc doc/tech-notes/*.html
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/pine.conf
%attr(755,root,root) %{_bindir}/pi*
%{_applnkdir}/Network/Mail/pine.desktop
%{_pixmapsdir}/*

%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(pl) %{_mandir}/pl/man1/*
