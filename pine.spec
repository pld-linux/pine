
Summary:	MIME compliant mail reader w/ news support as well
Summary(de):	MIME-konformer Mail-Reader mit News-Support
Summary(es):	Lector de mail con soporte a MIME y news
Summary(fr):	Lecteur de courrier conforme à MIME avec gestion des news"
Summary(pl):	Klient poczty elektronicznej i newsów ze wspomaganiem dla MIME
Summary(pt_BR):	Leitor de mail com suporte a MIME e news
Summary(ru):	óÏ×ÍÅÓÔÉÍÙÊ Ó MIME ÐÏÞÔÏ×ÙÊ ÒÅÄÁËÔÏÒ Ó ÐÏÄÄÅÒÖËÏÊ ÔÅÌÅËÏÎÆÅÒÅÎÃÉÊ
Summary(tr):	MIME uyumlu ileti okuyucusu (haber servisi desteði de vardýr)
Summary(uk):	óÕÍ¦ÓÎÉÊ Ú MIME ÐÏÞÔÏ×ÉÊ ÒÅÄÁËÔÏÒ Ú Ð¦ÄÔÒÉÍËÏÀ ÔÅÌÅËÏÎÆÅÒÅÎÃ¦Ê
Name:		pine
%define		realversion	4.56
Version:	%{realversion}L
Release:	0.2
License:	distributable
Group:		Applications/Mail
Source0:	ftp://ftp.cac.washington.edu/pine/%{name}%{realversion}.tar.bz2
# Source0-md5:	744992ab500ee265985eb078522e0604
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source3-md5:	7bd233708a9621f3dfd173acb20ec0bb
Source4:	pico.desktop
# renamed files from
# http://www.math.washington.edu/~chappa/pine/patches/pine%{realversion}/
Source5:	%{name}-rules.c.gz
# Source5-md5:	9380005dba3bb45db1fa24dbee459fea
Source6:	%{name}-rules.h.gz
# Source6-md5:	27b9833d2394b5d1826ed5f77cfa8ecb
Patch0:		%{name}-config.patch
Patch1:		%{name}-doc.patch
Patch2:		%{name}-makefile.patch
Patch3:		%{name}-terminfo.patch
Patch4:		%{name}-unix.patch
Patch5:		%{name}-filter.patch
Patch6:		%{name}-quote.patch
Patch7:		%{name}-fhs.patch
Patch8:		%{name}-maildir.patch
Patch9:		%{name}-maildirfix.patch
Patch10:	%{name}-segfix.patch
Patch11:	%{name}-whitespace.patch
Patch12:	%{name}-libc-client.patch
Patch13:	%{name}-fixhome.patch
#Patch14:	%{name}-terminit.patch
Patch15:	%{name}-ssl.patch
Patch16:	%{name}-non_english_man_path_fix.patch
Patch17:	%{name}-no_1777_warning.patch
Patch18:	%{name}-L_on_version.patch
Patch19:	%{name}-overflow.patch
# http://www.math.washington.edu/~chappa/pine/
Patch20:	http://www.math.washington.edu/~chappa/pine/patches/%{name}%{realversion}/all.patch.gz
# Original from: http://www.signet.pl/instrukcje/pine/pine-smime-211101-fixed.diff
Patch21:	%{name}-smime.patch
Patch22:	pine-css.patch
Patch23:	http://www.math.washington.edu/~chappa/pine/patches/pine4.21/blank.patch.gz
# from http://www.suse.de/~bk/pine/iconv/
Patch24:	pine-iconv-7d-2.diff
URL:		http://www.washington.edu/pine/
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	openssl-devel >= 0.9.7
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

%description -l es
Pine es un programa cliente de mail ("lector de mail") basado en texto
y cliente de news. Está orientado tanto a principiantes como a
usuarios más expertos. Posee soporte para MINE, agendas de dirección,
y soporte para folders de estilo IMAP, mail y MH.

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

%description -l pt_BR
Pine é um programa cliente de mail ("leitor de mail") baseado em texto
e cliente de news. Ele é dirigido tanto para novatos como para
usuários experientes. Possui suporte para MIME, agendas de endereço, e
suporte para pastas de estilo IMAP, mail e MH.

%description -l ru
Pine - ÜÔÏ ÐÏÌÎÏÃÅÎÎÙÊ ÔÅËÓÔ-ÏÒÉÅÎÔÉÒÏ×ÁÎÎÙÊ ËÌÉÅÎÔ ÄÌÑ ÐÏÞÔÙ É
ÔÅÌÅËÏÎÆÅÒÅÎÃÉÊ. òÁÓÓÞÉÔÁÎ ËÁË ÎÁ ÎÁÞÉÎÁÀÝÉÈ, ÔÁË É ÎÁ ÏÐÙÔÎÙÈ
ÐÏÌØÚÏ×ÁÔÅÌÅÊ. ÷ËÌÀÞÁÅÔ ÐÒÏÓÔÏÊ × ÉÓÐÏÌØÚÏ×ÁÎÉÉ ÒÅÄÁËÔÏÒ, pico, ÄÌÑ
ÒÅÄÁËÔÉÒÏ×ÁÎÉÑ ÐÏÞÔÏ×ÙÈ ÓÏÏÂÝÅÎÉÊ. éÍÅÅÔ ÐÏÄÄÅÒÖËÕ MIME, ÁÄÒÅÓÎÙÅ
ËÎÉÇÉ, ÐÏÄÄÅÒÖËÕ IMAP, ÍÏÖÅÔ ÒÁÂÏÔÁÔØ Ó ÐÏÞÔÏ×ÙÍÉ ÑÝÉËÁÍÉ × ÆÏÒÍÁÔÅ
mail É MH. îÁÓÔÏÑÝÁÑ ×ÅÒÓÉÑ ÐÏÚ×ÏÌÑÅÔ ÓËÏÎÆÉÇÕÒÉÒÏ×ÁÔØ Pine ÔÁË, ÞÔÏ
ÏÎ ÎÅ ÂÕÄÅÔ ËÏÄÉÒÏ×ÁÔØ ÒÕÓÓËÉÊ ÔÅËÓÔ × ÈÅÄÅÒÁÈ ÐÉÓÅÍ.

%description -l tr
Pine, metin tabanlý bir ileti ve haber servisi (news) istemcisidir.
Hem acemi hem de uzman kullanýcýlar için uygundur. Ýleti yazmak için
kullanýmý oldukça kolay olan pico adlý metin düzenleyicisini kullanýr.
Pico kendi baþýna da bir metin düzenleyici olarak ilgi görmüþtür.
Pine, MIME desteði, adres defteri ve IMAP, MH gibi ileti arþivi
biçimlerini destekleme özelliklerini taþýr.

%description -l uk
Pine - ÃÅ ÐÏ×ÎÏÃ¦ÎÎÉÊ ÔÅËÓÔ-ÏÒ¦¤ÎÔÏ×ÁÎÉÊ ËÌ¦¤ÎÔ ÄÌÑ ÐÏÛÔÉ ÔÁ
ÔÅÌÅËÏÎÆÅÒÅÎÃ¦Ê. òÏÚÒÁÈÏ×ÁÎÉÊ ÑË ÎÁ ÐÏÞÁÔË¦×Ã¦×, ÔÁË ¦ ÎÁ ÄÏÓ×¦ÄÞÅÎÉÈ
ËÏÒÉÓÔÕ×ÁÞ¦×. í¦ÓÔÉÔØ ÐÒÏÓÔÉÊ Õ ×ÉËÏÒÉÓÔÁÎÎ¦ ÒÅÄÁËÔÏÒ PICO ÄÌÑ
ÒÅÄÁÇÕ×ÁÎÎÑ ÐÏÛÔÏ×ÉÈ ÐÏ×¦ÄÏÍÌÅÎØ. íÁ¤ Ð¦ÄÔÒÉÍËÕ MIME, ÁÄÒÅÓÎ¦ ËÎÉÇÉ,
Ð¦ÄÔÒÉÍËÕ IMAP, ÍÏÖÅ ÐÒÁÃÀ×ÁÔÉ Ú ÐÏÛÔÏ×ÉÍÉ ÓËÒÉÎØËÁÍÉ × ÆÏÒÍÁÔÁÈ mail
ÔÁ MH. ãÑ ×ÅÒÓ¦Ñ ÄÏÚ×ÏÌÑ¤ ÓËÏÎÆ¦ÇÕÒÕ×ÁÔÉ Pine ÔÁË, ÝÏ ×¦Î ÎÅ ÂÕÄÅ
ËÏÄÕ×ÁÔÉ ËÉÒÉÌ¦ÞÎÉÊ ÔÅËÓÔ × ÈÅÄÅÒÁÈ ÌÉÓÔ¦×.

%package -n pico
Summary:	Simple text editor in the style of the Pine Composer
Summary(es):	Simple, easy-to-use text-based editor
Summary(pl):	Prosty edytor tekstowy w stylu pine
Summary(pt_BR):	Editor de textos para terminal simples e fácil de usar
Group:		Applications/Editors

%description -n pico
Pico is a simple, display-oriented text editor based on the Pine
message system composer. As with Pine, commands are displayed at the
bottom of the screen, and context-sensitive help is provided. As
characters are typed they are immediately inserted into the text.

%description -n pico -l es
Pico is a simple, display-oriented text editor based on the Pine
message system composer. As with Pine, commands are displayed at the
bottom of the screen, and context- sensitive help is provided.

%description -n pico -l pl
Pico jest prostym, zorientowanym na wy¶wietlanie edytorem bazuj±cym na
pine. Tak jak w pine komendy s± wy¶wietlane na dole ekranu oraz
dostêpna jest pomoc konteksowa. Wpisywane znaki s± natychmiast
w³±czane do tekstu.

%description -n pico -l pt_BR
Pico é um editor de texto baseado no compositor de mensagens do Pine.
Assim como no Pine, comandos são mostrados na parte de baixo da tela,
e ajuda de acordo com o contexto está disponível.

%package -n pilot
Summary:	Simple file system browser in the style of the Pine Composer
Summary(es):	Simple filesystem browser in the style of the Pine Composer
Summary(pl):	Prosta przegl±darka plików w stylu composera pine
Summary(pt_BR):	Navegador de sistemas de arquivos no estilo do compositor do Pine
Group:		Applications/Shells

%description -n pilot
Pilot is a simple, display-oriented file system browser based on the
Pine message system composer. As with Pine, commands are displayed at
the bottom of the screen, and context-sensitive help is provided.

%description -n pilot -l es
Pilot is a simple, display-oriented file system browser based on the
Pine message system composer. As with Pine, commands are displayed at
the bottom of the screen, and context-sensitive help is provided.

%description -n pilot -l pl
Pilot jest prost±, zorientowan± na wy¶wietlanie przegl±dark± plików w
stylu compsera pine. Podobnie jak w pine polecenia sa wy¶wietlane na
dole ekranu oraz jest dostêpna pomoc kontekstowa.

%description -n pilot -l pt_BR
Pilot é um navegador de sistemas de arquivos baseado no Pine. Assim
como no Pine, comandos são apresentados na parte de baixo da tela, e
ajuda de acordo com o contexto está disponível.

%prep
%setup   -q -a3 -n %{name}%{realversion}
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
# breaks keys on some terminals
##%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
# breaks pine
##%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1

zcat %{SOURCE5} >pine/rules.c
zcat %{SOURCE6} >pine/rules.h

%build
./build slx \
	OPTIMIZE="%{rpmcflags}" \
	BASECFLAGS="%{rpmcflags} -DNFSKLUDGE" \
	EXTRACFLAGS="-DHAVE_ICONV" \
	SSLTYPE="unix" \
	DEBUG=" " \
	CC="%{__cc}"

echo "%{__cc}" > ~/gcc.info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{man1,{es,fi,hu,pl}/man1}} \
	$RPM_BUILD_ROOT%{_applnkdir}/{Network/Mail,Editors} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_sysconfdir}}

install bin/{pine,pico,pilot} $RPM_BUILD_ROOT%{_bindir}

install doc/{pine,pico,pilot}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install es/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/es/man1
install fi/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/fi/man1
install hu/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/hu/man1
install pl/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/pl/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail
install %{SOURCE4} $RPM_BUILD_ROOT%{_applnkdir}/Editors
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/*.txt doc/mailcap.unx
%doc doc/tech-notes/*.html
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/pine.conf
%attr(755,root,root) %{_bindir}/pine
%{_applnkdir}/Network/Mail/pine.desktop
%{_pixmapsdir}/*

%{_mandir}/man1/pine*
%lang(es) %{_mandir}/es/man1/pine*
%lang(fi) %{_mandir}/fi/man1/pine*
%lang(hu) %{_mandir}/hu/man1/pine*
%lang(pl) %{_mandir}/pl/man1/pine*

%files -n pico
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pico
%{_applnkdir}/Editors/pico.desktop
%{_mandir}/man1/pico*
%lang(es) %{_mandir}/es/man1/pico*
%lang(fi) %{_mandir}/fi/man1/pico*
%lang(hu) %{_mandir}/hu/man1/pico*
%lang(pl) %{_mandir}/pl/man1/pico*

%files -n pilot
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pilot
%{_mandir}/man1/pilot*
%lang(es) %{_mandir}/es/man1/pilot*
