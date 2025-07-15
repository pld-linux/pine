#
# Conditional build:
%bcond_without	distributable	# build distributable package with license included
%bcond_without	utf8		# build without utf-8 support
%bcond_without	home_etc	# build without home-etc support

Summary:	MIME compliant mail reader w/ news support as well
Summary(de.UTF-8):	MIME-konformer Mail-Reader mit News-Support
Summary(es.UTF-8):	Lector de mail con soporte a MIME y news
Summary(fr.UTF-8):	Lecteur de courrier conforme à MIME avec gestion des news"
Summary(pl.UTF-8):	Klient poczty elektronicznej i newsów ze wspomaganiem dla MIME
Summary(pt_BR.UTF-8):	Leitor de mail com suporte a MIME e news
Summary(ru.UTF-8):	Совместимый с MIME почтовый редактор с поддержкой телеконференций
Summary(tr.UTF-8):	MIME uyumlu ileti okuyucusu (haber servisi desteği de vardır)
Summary(uk.UTF-8):	Сумісний з MIME почтовий редактор з підтримкою телеконференцій
Name:		pine
%define		realversion	4.64
Version:	%{realversion}N
Release:	9
%if %{with distributable}
License:	Distributable for PLD
%else
License:	Not distributable
%endif
Group:		Applications/Mail
Source0:	ftp://ftp.cac.washington.edu/pine/%{name}%{realversion}.tar.bz2
# Source0-md5:	39ca07b3d305b4cd0d6aaf4585123275
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source3-md5:	7bd233708a9621f3dfd173acb20ec0bb
Source4:	pico.desktop
Source5:	%{name}-PLD-LICENSE
Patch0:		%{name}-config.patch
Patch1:		%{name}-doc.patch
Patch2:		%{name}-makefile.patch
Patch3:		%{name}-terminfo.patch
Patch4:		%{name}-unix.patch
Patch5:		%{name}-filter.patch
Patch6:		%{name}-quote.patch
Patch7:		%{name}-fhs.patch
Patch8:		%{name}-segfix.patch
Patch9:		%{name}-libc-client.patch
Patch10:	%{name}-fixhome.patch
Patch11:	%{name}-ssl.patch
Patch12:	%{name}-non_english_man_path_fix.patch
Patch13:	%{name}-no_1777_warning.patch
Patch14:	%{name}-N_on_version.patch
Patch15:	%{name}-overflow.patch
# http://www.math.washington.edu/~chappa/pine/
Patch16:	all.patch.gz
# Patch16-md5:	105abe1481f84987c8c91635cce537d4
# Original from: http://www.signet.pl/instrukcje/pine/pine-smime-211101-fixed.diff
Patch17:	%{name}-smime.patch
Patch20:	%{name}-home_etc.patch
Patch21:	%{name}-pwd.patch
Patch22:	%{name}-address-of-register.patch
## Set of patches taken from SuSE:
## http://www.suse.de/~bk/pine/4.64/2006-04-28/RPM-source/
Patch40:	%{name}-charset-editorial.patch
Patch41:	%{name}-iconv-no-explain.patch
Patch42:	%{name}-optionally_enter.patch
Patch43:	%{name}-multipart-alternative-conversion.patch
Patch44:	%{name}-pico-ucs4all.patch
Patch45:	%{name}-pico-ucs4GetKey.patch
Patch46:	%{name}-pico-ucs4doublewidthchars.diff
Patch47:	%{name}-pico-ucs4isspace.patch
Patch48:	%{name}-utf8-1b.patch
Patch49:	%{name}-utf8-1a-pine.h.patch
Patch50:	%{name}-utf8-1a-GFHP_HANDLES.patch
Patch51:	%{name}-send-charset.patch
Patch52:	%{name}-config-options.patch
Patch53:	%{name}-utf8-mailindx.patch
Patch54:	%{name}-mailindx-plusdraw.patch
Patch55:	%{name}-gf_wrap-UTF8.patch
Patch56:	%{name}-no-stripwhitespace.patch
Patch57:	%{name}-strings-iconv.patch
Patch58:	%{name}-filter-iconv.patch
Patch59:	%{name}-rfc1522_decode.patch
Patch60:	%{name}-rfc1522_valid.patch
URL:		http://www.washington.edu/pine/
# iconv form glibc - utf-8 support
%{?with_utf8:BuildRequires:	glibc-devel >= 2.3.2}
%{?with_home_etc:BuildRequires:	home-etc-devel >= 1.0.8}
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	openssl-devel >= 0.9.7d
%{?with_home_etc:Requires:	home-etc >= 1.0.8}
Requires:	mailcap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pine is a very full featured text based mail and news client. It is
aimed at both novice and expert users. It includes an easy to use
editor, pico, for composing messages. Pico has gained popularity as a
stand alone text editor in it's own right. It features MIME support,
address books, and support for IMAP, mail, and MH style folders.

%description -l de.UTF-8
Pine ist ein kompletter textbasierender Mail- und New-Client, der sich
sowohl an Neueinsteiger als auch an Experten richtet. Er umfaßt einen
einfachen Editor (Pico), der zum Verfassen der Nachrichten dient, sich
jedoch inzwischen einen Namen als autonomer Texteditor gemacht hat.
Pine unterstützt MIME, Adreßbücher, IMAP, Mail- und HM-Ordner.

%description -l es.UTF-8
Pine es un programa cliente de mail ("lector de mail") basado en texto
y cliente de news. Está orientado tanto a principiantes como a
usuarios más expertos. Posee soporte para MINE, agendas de dirección,
y soporte para folders de estilo IMAP, mail y MH.

%description -l fr.UTF-8
pine est un client courrier et news très complet en mode texte. Il est
destiné aux débutants comme aux experts. Il comprend un éditeur simple
à utiliser, pico, pour composer les messages. pico est devenu
populaire comme éditeur de texte par lui-même. Il reconnait la gestion
MIME, les carnets d'adresse et la gestion IMAP, mail et des dossiers
du style MH.

%description -l pl.UTF-8
Pine jest doskonałym czytnikiem poczty elektronicznej i newsów,
pracującym w trybie tekstowym. W pakiecie znajduje się również łatwy w
użyciu edytor pico, wykorzystywany do pisania wiadomości. Pine jest
obecnie jednym z najbardziej popularnych czytników poczty
elektronicznej, posiada wspomaganie dla MIME i IMAP, można w łatwy
sposób tworzyć książki adresowe i skonfigurować go do współpracy z
aplikacją PGP.

%description -l pt_BR.UTF-8
Pine é um programa cliente de mail ("leitor de mail") baseado em texto
e cliente de news. Ele é dirigido tanto para novatos como para
usuários experientes. Possui suporte para MIME, agendas de endereço, e
suporte para pastas de estilo IMAP, mail e MH.

%description -l ru.UTF-8
Pine - это полноценный текст-ориентированный клиент для почты и
телеконференций. Рассчитан как на начинающих, так и на опытных
пользователей. Включает простой в использовании редактор, pico, для
редактирования почтовых сообщений. Имеет поддержку MIME, адресные
книги, поддержку IMAP, может работать с почтовыми ящиками в формате
mail и MH. Настоящая версия позволяет сконфигурировать Pine так, что
он не будет кодировать русский текст в хедерах писем.

%description -l tr.UTF-8
Pine, metin tabanlı bir ileti ve haber servisi (news) istemcisidir.
Hem acemi hem de uzman kullanıcılar için uygundur. İleti yazmak için
kullanımı oldukça kolay olan pico adlı metin düzenleyicisini kullanır.
Pico kendi başına da bir metin düzenleyici olarak ilgi görmüştür.
Pine, MIME desteği, adres defteri ve IMAP, MH gibi ileti arşivi
biçimlerini destekleme özelliklerini taşır.

%description -l uk.UTF-8
Pine - це повноцінний текст-орієнтований клієнт для пошти та
телеконференцій. Розрахований як на початківців, так і на досвідчених
користувачів. Містить простий у використанні редактор PICO для
редагування поштових повідомлень. Має підтримку MIME, адресні книги,
підтримку IMAP, може працювати з поштовими скриньками в форматах mail
та MH. Ця версія дозволяє сконфігурувати Pine так, що він не буде
кодувати кирилічний текст в хедерах листів.

%package -n pico
Summary:	Simple text editor in the style of the Pine Composer
Summary(pl.UTF-8):	Prosty edytor tekstowy w stylu pine
Summary(pt_BR.UTF-8):	Editor de textos para terminal simples e fácil de usar
Group:		Applications/Editors

%description -n pico
Pico is a simple, display-oriented text editor based on the Pine
message system composer. As with Pine, commands are displayed at the
bottom of the screen, and context-sensitive help is provided. As
characters are typed they are immediately inserted into the text.

%description -n pico -l pl.UTF-8
Pico jest prostym, zorientowanym na wyświetlanie edytorem bazującym na
pine. Tak jak w pine komendy są wyświetlane na dole ekranu oraz
dostępna jest pomoc konteksowa. Wpisywane znaki są natychmiast
włączane do tekstu.

%description -n pico -l pt_BR.UTF-8
Pico é um editor de texto baseado no compositor de mensagens do Pine.
Assim como no Pine, comandos são mostrados na parte de baixo da tela,
e ajuda de acordo com o contexto está disponível.

%package -n pilot
Summary:	Simple file system browser in the style of the Pine Composer
Summary(pl.UTF-8):	Prosta przeglądarka plików w stylu composera pine
Summary(pt_BR.UTF-8):	Navegador de sistemas de arquivos no estilo do compositor do Pine
Group:		Applications/Shells

%description -n pilot
Pilot is a simple, display-oriented file system browser based on the
Pine message system composer. As with Pine, commands are displayed at
the bottom of the screen, and context-sensitive help is provided.

%description -n pilot -l pl.UTF-8
Pilot jest prostą, zorientowaną na wyświetlanie przeglądarką plików w
stylu compsera pine. Podobnie jak w pine polecenia sa wyświetlane na
dole ekranu oraz jest dostępna pomoc kontekstowa.

%description -n pilot -l pt_BR.UTF-8
Pilot é um navegador de sistemas de arquivos baseado no Pine. Assim
como no Pine, comandos são apresentados na parte de baixo da tela, e
ajuda de acordo com o contexto está disponível.

%prep
%setup -q -a3 -n %{name}%{realversion}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%{!?with_distributable:%patch5 -p1}
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1
%{!?with_distributable:%patch13 -p1}
%patch -P14 -p1
%patch -P15 -p1
%patch -P16 -p1
# breaks pine
#%{!?with_distributable:%patch17 -p1}
%if ! %{with distributable}
%{?with_utf8:%patch22 -p1}
%{?with_utf8:%patch40 -p0}
%{?with_utf8:%patch41 -p1}
%{?with_utf8:%patch42 -p1}
%{?with_utf8:%patch43 -p1}
%{?with_utf8:%patch44 -p1}
%{?with_utf8:%patch45 -p1}
%{?with_utf8:%patch46 -p1}
%{?with_utf8:%patch47 -p1}
%{?with_utf8:%patch48 -p1}
%{?with_utf8:%patch49 -p1}
%{?with_utf8:%patch50 -p1}
%{?with_utf8:%patch51 -p1}
%{?with_utf8:%patch52 -p1}
%{?with_utf8:%patch53 -p1}
%{?with_utf8:%patch54 -p1}
%{?with_utf8:%patch55 -p1}
%{?with_utf8:%patch56 -p1}
%{?with_utf8:%patch57 -p1}
%{?with_utf8:%patch58 -p1}
%{?with_utf8:%patch59 -p1}
%{?with_utf8:%patch60 -p1}
%endif
%{?with_home_etc:%patch20 -p1}
%patch -P21 -p1

%build
./build slx \
	OPTIMIZE="%{rpmcflags}" \
	BASECFLAGS="%{rpmcflags} -DNFSKLUDGE" \
	%{!?with_utf8:EXTRACFLAGS="-DHAVE_ICONV"} \
	%{?with_home_etc:HOMEETCLIB="1"} \
	SSLTYPE="unix" \
	SSLDIR="/var/lib/openssl/certs" \
	SSLCERTS="/var/lib/openssl/certs" \
	DEBUG=" " \
	LDAPLIBS=-lldap \
	LDAPCFLAGS=-DENABLE_LDAP \
	CC="%{__cc}"

echo "%{__cc}" > ~/gcc.info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{man1,{es,fi,hu,pl}/man1}} \
	$RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_sysconfdir}}

install bin/{pine,pico,pilot} $RPM_BUILD_ROOT%{_bindir}

install doc/{pine,pico,pilot}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install es/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/es/man1
install fi/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/fi/man1
install hu/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/hu/man1
install pl/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/pl/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
%{?with_distributable:cp %{SOURCE5} .}

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
%doc CPYRIGHT README doc/*.txt doc/mailcap.unx doc/tech-notes/*.html
%{?with_distributable:%doc %{name}-PLD-LICENSE}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pine.conf
%attr(755,root,root) %{_bindir}/pine
%{_desktopdir}/pine.desktop
%{_pixmapsdir}/*

%{_mandir}/man1/pine*
%lang(es) %{_mandir}/es/man1/pine*
%lang(fi) %{_mandir}/fi/man1/pine*
%lang(hu) %{_mandir}/hu/man1/pine*
%lang(pl) %{_mandir}/pl/man1/pine*

%files -n pico
%defattr(644,root,root,755)
%{?with_distributable:%doc %{name}-PLD-LICENSE}
%attr(755,root,root) %{_bindir}/pico
%{_desktopdir}/pico.desktop
%{_mandir}/man1/pico*
%lang(es) %{_mandir}/es/man1/pico*
%lang(fi) %{_mandir}/fi/man1/pico*
%lang(hu) %{_mandir}/hu/man1/pico*
%lang(pl) %{_mandir}/pl/man1/pico*

%files -n pilot
%defattr(644,root,root,755)
%{?with_distributable:%doc %{name}-PLD-LICENSE}
%attr(755,root,root) %{_bindir}/pilot
%{_mandir}/man1/pilot*
%lang(es) %{_mandir}/es/man1/pilot*
