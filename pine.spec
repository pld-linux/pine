Summary:	MIME compliant mail reader w/ news support as well
Summary(de):	MIME-konformer Mail-Reader mit News-Support 
Summary(fr):	Lecteur de courrier conforme � MIME avec gestion des news"
Summary(pl):	Klient poczty elektronicznej i news�w ze wspomaganiem dla MIME
Summary(tr):	MIME uyumlu ileti okuyucusu (haber servisi deste�i de vard�r)
Name:		pine
Version:	4.33
Release:	12
License:	Distributable
Group:		Applications/Mail
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplica��es/Correio Eletr�nico
Source0:	ftp://ftp.cac.washington.edu/pine/%{name}%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.1.pl
Patch0:		%{name}-config.patch
Patch1:		%{name}-doc.patch
Patch2:		%{name}-makefile.patch
Patch3:		%{name}-terminfo.patch
Patch4:		%{name}-nodebug.patch
Patch5:		%{name}-unix.patch
Patch6:		%{name}-filter.patch
Patch7:		%{name}-quote.patch
Patch8:		%{name}-noflock.patch
Patch9:		%{name}-fhs.patch
Patch10:	%{name}-maildir.patch
Patch11:	%{name}-maildirfix.patch
Patch12:	%{name}-time.patch
Patch13:	%{name}-segfix.patch
Patch14:	%{name}-whitespace.patch
Patch15:	%{name}-ssl.patch
Patch16:	%{name}-libc-client.patch
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
sowohl an Neueinsteiger als auch an Experten richtet. Er umfa�t einen
einfachen Editor (Pico), der zum Verfassen der Nachrichten dient, sich
jedoch inzwischen einen Namen als autonomer Texteditor gemacht hat.
Pine unterst�tzt MIME, Adre�b�cher, IMAP, Mail- und HM-Ordner.

%description -l fr
pine est un client courrier et news tr�s complet en mode texte. Il est
destin� aux d�butants comme aux experts. Il comprend un �diteur simple
� utiliser, pico, pour composer les messages. pico est devenu
populaire comme �diteur de texte par lui-m�me. Il reconnait la gestion
MIME, les carnets d'adresse et la gestion IMAP, mail et des dossiers
du style MH.

%description -l pl
Pine jest doskona�ym czytnikiem poczty elektronicznej i news�w,
pracuj�cym w trybie tekstowym. W pakiecie znajduje si� r�wnie� �atwy w
u�yciu edytor pico, wykorzystywany do pisania wiadomo�ci. Pine jest
obecnie jednym z najbardziej popularnych czytnik�w poczty
elektronicznej, posiada wspomaganie dla MIME i IMAP, mo�na w �atwy
spos�b tworzy� ksi��ki adresowe i skonfigurowa� go do wsp�pracy z
aplikacj� PGP.

%description -l tr
Pine, metin tabanl� bir ileti ve haber servisi (news) istemcisidir.
Hem acemi hem de uzman kullan�c�lar i�in uygundur. �leti yazmak i�in
kullan�m� olduk�a kolay olan pico adl� metin d�zenleyicisini kullan�r.
Pico kendi ba��na da bir metin d�zenleyici olarak ilgi g�rm��t�r.
Pine, MIME deste�i, adres defteri ve IMAP, MH gibi ileti ar�ivi
bi�imlerini destekleme �zelliklerini ta��r.

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
%patch11 -p1 
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

%build
./build slx \
	OPTIMIZE="%{rpmcflags}" \
	BASECFLAGS="%{rpmcflags} -DNFSKLUDGE" \
	DEBUG="" \
	CC="%{__cc}"

echo "%{__cc}" > ~/gcc.info
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{man1,pl/man1}} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Network/Mail,%{_sysconfdir}}

install bin/{pine,pico,pilot} $RPM_BUILD_ROOT%{_bindir}

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

gzip -9nf README doc/*.txt doc/mailcap.unx 

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
