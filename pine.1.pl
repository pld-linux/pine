.\" {PTM/LK/0.1/30-01-1999/"program do czytania poczty"}
.\" T�umaczenie: 30-01-1999 �ukasz Kowalczyk (lukow@tempac.okwf.fuw.edu.pl)
.TH pine 1 "Wersja 4.04"
.SH NAZWA
pine \- program do czytania grup dyskusyjnych i poczty elektronicznej
.SH SK�ADNIA

.B pine
[
.I opcje
] [
.I adres
,
.I adres
] 

.B pinef
[
.I opcje
] [
.I adres
,
.I adres
]
.SH OPIS

Pine jest pe�noekranowym programem do czytania wiadomo�ci. W swojej
domy�lnej konfiguracji Pine prezentuje celowo ograniczony zestaw opcji
przeznaczony dla pocz�tkuj�cego u�ytkownika. Istnieje jednak wci�� rosn�ca
lista opcjonalnych mo�liwo�ci przeznaczonych dla zaawansowanych u�ytkownik�w.
.I pinef 
jest wersj� programu Pine u�ywaj�cym klawiszy funkcyjnych zamiast
jednoliterowych polece�.
W podstawowym zestawie polece� znajduj� si� nast�puj�ce opcje:
.IP
View (przegl�danie), Save (zapis), Export (zapis do pliku), 
Delete (usuwanie), Print (drukowanie), Reply (odpowiadanie) i 
Forward (dalsze przesy�anie wiadomo�ci).
.IP
Tworzenie wiadomo�ci w prostym edytorze (Pico) z automatycznym �amaniem
linii i kontrol� pisowni. Edycja wiadomo�ci mo�e by� odk�adana do
p�niejszej kontynuacji.
.IP
Pe�noekranowy wyb�r i zarz�dzanie folderami.
.IP
Ksi��ka adresowa, w kt�rej znajduj� si� cz�sto u�ywane lub po prostu d�ugie
adresy. Mo�na definiowa� w�asne listy dystrybucyjne. Adresy mog� by�
pobierane z otrzymywanych wiadomo�ci bez potrzeby odpowiadania na nie.
.IP
Sprawdzanie, czy otrzymano nowe wiadomo�ci jest wykonywane co 2.5 minuty
oraz po pewnych poleceniach, np. od�wie�aniu ekranu (Ctrl-L).
.IP
Kontekstowa pomoc.
.PP
Pine obs�uguje MIME (Multipurpose Internet Mail Extensions), internetowy
standard reprezentacji wielocz�ciowych i multimedialnych danych w
wiadomo�ciach. Pine pozwala na zapis obiekt�w MIME do plik�w i w pewnych
sytuacjach mo�e uruchomi� odpowiedni program do ogl�dania takich wiadomo�ci.
Pine u�ywa systemowego pliku konfiguracyjnego 
.I mailcap 
by uruchomi� w�a�ciwy program do obs�ugi poszczeg�lnych obiekt�w MIME.
Wbudowany program do tworzenia wiadomo�ci nie posiada w�a�ciwo�ci
multimedialnych, lecz dowolny typ danych - w��cznie z multimedialnymi - 
mo�e zosta� umieszczony w wiadomo�ci jako za��cznik. Pozwala to posiadaczom
program�w pocztowych zgodnych z MIME na wymian� sformatowanych dokument�w,
arkuszy kalkulacyjnych, plik�w graficznych etc. przez poczt� elektroniczn�.
.PP
Do obs�ugi lokalnych i zdalnych folder�w pocztowych Pine u�ywa interfejsu
.I c-client
(c-client messaging API).
Ta biblioteka pozwala na wykonywanie wielu niskopoziomowych funkcji obs�ugi
poczty, w��czaj�c w to funkcje obs�ugi wielu format�w pocztowych, protoko�u
IMAP (Internet Message
Access Protocol) oraz NNTP (Network News Transport Protocol). Poczta
wychodz�ca jest zazwyczaj przekazywana programowi 
.IR sendmail ,
ale mo�e by� wysy�ana bezpo�rednio przez SMTP (Simple Mail Transfer Protocol).
.SH OPCJE
.if n .ta 2.8i
.if t .ta 2.1i
Pine rozpoznaje nast�puj�ce opcje linii polece�:
.IP \fIadres\fR 20
Wys�anie wiadomo�ci na podany adres e-mailowy. Pine uruchomi si� w trybie tworzenia
wiadomo�ci.
.IP \fB-a\fR 20
Specjalny anonimowy tryb dzia�ania dla UWIN* (* patrz ni�ej)
.IP \fB-c\ \fInumer_kontekstu\fR 20
mumer_kontekstu jest numerem odnosz�cym si� do kolekcji folder�w, do kt�rego
powinien zosta� zastosowany argument
.I -f
linii polece�. Domy�lnie opcja
.I -f
jest stosowana do pierwszej zdefiniowanej kolekcji folder�w.
.IP \fB-d\ \fIpoziom_diagnostyki\fR 20
Wypisywanie informacji diagnostycznych na poziomie 
.I poziom_diagnostyki
(0-9) do bie��cego pliku
.IR .pine-debug[1-4] .
Warto�� 0 wy��cza informacje diagnostyczne i wstrzymuje tworzenie pliku
.IR .pine-debug .

.IP \fB-d\ \fIklucz[=warto��]\fR 20
Szczeg�owy opis tworzenia informacji diagnostycznych; "flush"
powoduje zapisywanie plik�w diagnostycznych bez buforowania, "timestamp"
do��cza do ka�dego komunikatu czas jego wygenerowania, "imap=n" (gdzie n
przybiera warto�ci od 0 do 4) powoduje do��czanie telemetrii (ang.
telemetry) IMAP na podanym poziomie, "numfiles=n" (gdzie n przybiera
warto�� od 0 do 31) opisuje ilo�� tworzonych plik�w diagnostycznych i
wreszcie "verbose=n" (gdzie n przybiera warto�ci od 0 do 9) jest odwrotnym
progiem poziomu generowania og�lnych wiadomo�ci o dzia�aniu programu.
.IP \fB-f\ \fIfolder\fR 20
Otwarcie folderu (w pierwszej zdefiniowanej kolekcji folder�w) zamiast INBOX.
.IP \fB-F\ \fIplik\fR 20
Otwarcie podanego pliku tekstowego w przegl�darce programu Pine.
.IP \fB-h\fR 20
Pomoc: lista rozpoznawanych opcji linii polece�.
.IP \fB-i\fR 20
Otwarcie indeksu folder�w po uruchomieniu programu.
.IP \fB-I\ \fIklawisze\fR 20
Lista klawiszy (rozdzielona przecinkami), kt�rych naci�ni�cie Pine powinien
zasymulowa� zaraz po uruchomieniu.
.IP \fB-k\fR 20
Wywo�ywanie polece� klawiszami funkcyjnymi. Identyczne dzia�anie ma
uruchomienie programu pinef.
.IP \fB-n\ \fInumer\fR 20
Uruchomienie programu z automatycznym otworzeniem wiadomo�ci o podanym
numerze.
.IP \fB-nr\fR 20
Specjalny tryb dla UWIN*
.IP \fB-o\fR 20
Otwarcie pierwszego folderu w trybie tylko do odczytu.
.IP \fB-p\ \fIplik_konfiguracyjny\fR 20
U�ycie podanego pliku w charakterze pliku konfiguracyjnego zamiast
domy�lnego .pinerc.
.IP \fB-P\ \fIplik_konfiguracyjny\fR 20
U�ycie podanego pliku w charakterze pliku konfiguracyjnego zamiast
domy�lnego pliku systemowego
.IR pine.conf .
.IP \fB-r\fR 20
Uruchomienie w trybie demonstracyjnym o ograniczonej funkcjonalno�ci. 
.I Pine
b�dzie wysy�a� poczt� tylko do siebie samego, a funkcje typu save i export
nie b�d� dzia�a�y.
.IP \fB-z\fR 20
Udost�pnienie mo�liwo�ci przeniesienia programu Pine do t�a klawiszem ^Z lub
sygna�em SIGTSTP.
.IP \fB-conf\fR 20
Utworzenie wzorcowego pliku jako szablonu dla systemowego pliku
konfiguracyjnego
.I pine.conf
na standardowym wyj�ciu. Jest to inny plik ni� indywidualny dla ka�dego
u�ytkownika 
.IR .pinerc .
.IP \fB-create_lu\ \fIksi��ka_adresowa\ \fIporz�dek_sortowania\fR 20
Utworzenie dodatkowego indeksu dla ksi��ki adresowej o podanej nazwie i
posortowanie jej w podanym porz�dku. Mo�liwe warto�ci dla porz�dku
sortowania, to
.IR "dont-sort (brak sortowania)" ,
.IR "nickname (skr�t nazwy adresata)" ,
.IR "fullname (pe�na nazwa adresata)" ,
.IR "nickname-with-lists-last (skr�t nazwy, ale listy na ko�cu)" ,
or
.IR "fullname-with-lists-last (pe�na nazwa, ale listy na ko�cu)" .

Jest to u�yteczne do tworzenia globalnych lub dzielonych ksi��ek adresowych.
Po utworzeniu w ten spos�b indeksu, plik powinien zosta� przeniesiony lub
skopiowany w taki spos�b, by zmianie nie uleg� czas modyfikacji. Czas
modyfikacji ksi��ki adresowej jest zachowywany w nowotworzonym pliku z
indeksem i przy ka�dym uruchomieniu programu sprawdzany. Je�eli czas
modyfikacji ksi��ki adresowej ulegnie zmianie, pine utworzy indeks od nowa.
Innymi s�owy, po utworzeniu indeksu za pomoc� opisywanej opcji, nie kopiuj
ksi��ki adresowej do jej docelowego po�o�enia w taki spos�b, kt�ry zmieni
jej czas modyfikacji.
.IP \fB-pinerc\ \fIplik\fR 20
Zapisanie bie��cej konfiguracji programu do podanego pliku.
.IP \fB-sort\ \fIporz�dek_sortowania\fR
Posortowanie ekranu FOLDER INDEX w jednej z nast�puj�cych kolejno�ci:
.I arrival (czas nadej�cia), subject (temat), from (pole from), date (data),
.I size (rozmiar), orderedsubj (pseudo w�tek)
lub
.I reverse (odwrotna kolejno��). Arrival
jest domy�lnym porz�dkiem sortowania. Porz�dek OrderedSubj symuluje
sortowanie pod k�tem w�tk�w. Ka�dy porz�dek sortowania mo�e zosta� odwr�cony
przez dodanie do niego 
.IR /reverse .

.I Reverse
bez dodatkowych opcji dzia�a jak
.IR arrival/reverse .
.IP \fI-option\=\fIwarto��\fR 20
Nadanie opcji konfiguracyjnej podanej warto�ci. Np. 
-signature-file=sig1 lub -feature-list=signature-at-bottom
(Uwaga: warto�ci opcji feature-list s� addytywne)
.PP
* UWIN = University of Washington Information Navigator
.SH KONFIGURACJA

Istnieje kilka poziom�w konfiguracji programu Pine. Warto�ci konfiguracyjne
na danym poziomie maj� wy�szy priorytet ni� te warto�ci na ni�szych poziomach.
W porz�dku rosn�cego priorytetu:

 o wbudowane warto�ci domy�lne.
.br
 o plik
.I pine.conf
dla ca�ego systemu.
.br
 o osobisty plik
.I .pinerc 
ka�dego u�ytkownika (warto�ci w nim mo�na ustawia� za pomoc� menu
Setup/Config).
.br
 o opcje linii polece�
.br
 o plik
.I pine.conf.fixed
dla ca�ego systemu.

Istnieje wyj�tek od zasady, w my�l kt�rej warto�ci konfiguracyjne s�
zast�powane przez warto�ci tych samych opcji o wy�szym priorytecie: 
warto�ci nadawane zmiennej feature-list s� addytywne, lecz mog� by�
zanegowane do��czeniem "no-" na pocz�tku danej warto�ci dla tej zmiennej.
Pine w systemie Unix u�ywa nast�puj�cych zmiennych �rodowiskowych.

  TERM
.br
  DISPLAY     (okre�la, czy Pine mo�e wy�wietla� za��czniki typu IMAGE).
.br
  SHELL       (domy�ln� warto�ci� jest /bin/sh, je�eli ta zmienna nie jest
ustawiona).
.br
  MAILCAPS    (lista �cie�ek do plik�w mailcap rozdzielonych �rednikami).
  
.SH PLIKI
.if n .ta 2.8i
.if t .ta 2.1i

/var/mail/xxxx		Domy�lny folder dla przychodz�cej poczty.
.br
~/mail	Domy�lny katalog dla folder�w.
.br
~/.addressbook	Domy�lna nazwa pliku z ksi��k� adresow�.
.br
~/.addressbook.lu	Domy�lna nazwa pliku z indeksem ksi��ki adresowej.
.br
~/.pine-debug[1-4]	Pliki, do kt�rych zapisywane s� komunikaty diagnostyczne.
.br
~/.pinerc	Osobisty plik konfiguracyjny.
.br
~/.newsrc	Opis stanu subskrybowanych grup dyskusyjnych.
.br
~/.signature	Domy�lna nazwa pliku z sygnatur�.
.br
~/.mailcap	Osobisty plik mailcap (man mailcap(4))
.br
~/.mime.types	Osobiste rozszerzenie rozpoznawanych typ�w MIME
.br
/etc/mailcap	Systemowy plik mailcap (man mailcap(4))
.br
/etc/mime.types	Systemowe opis rozpoznawanych typ�w MIME
.br
/usr/share/info/pine.info	Lokalny wska�nik do administratora systemu
.br
/etc/pine.conf	Systemowy plik konfiguracyjny
.br
/etc/pine.conf.fixed  Plik konfiguracyjny, kt�rego ustawienia nie mog� by� zmieniane
.br
/tmp/.\\var\\mail\\xxxx		Pliki blokuj�ce dla ka�dego folderu
.br
~/.pine-interrupted-mail	Wiadomo��, kt�rej tworzenie zosta�o przerwane
.br
~/mail/postponed-msgs	Wiadomo��, kt�rej tworzenie zosta�o od�o�one na p�niej
.br
~/mail/sent-mail	Archiwum wys�anych wiadomo�ci
.br
~/mail/saved-messages	Domy�lny folder na zapisywane wiadomo�ci
.SH "ZOBACZ TAK�E"

pico(1), binmail(1), aliases(5), mailaddr(7), sendmail(8), spell(1), imapd(8)

.br
Grupa dyskusyjna:  comp.mail.pine
.br
Pine Information Center:  http://www.washington.edu/pine
.br
Dystrybucja �r�d�owa:  ftp://ftp.cac.washington.edu/pine/pine.tar.Z
.br
Pine Technical Notes (informacje techniczne), zawarte w dystrybucji �r�d�owej
.br
Interfejs (API) biblioteki przesy�ania wiadomo�ciC-Client, zawarty w
dytrybucji �r�d�owej.
.SH PODZI�KOWANIA
.na 
.nf

Zesp� rozwoju programu Pine (cz�� UW Office 
of Computing & Communications) na Uniwersytecie w Waszyngtonie
(University of Washington):

.\" celowo nie przet�umaczone

 Project Leader:           Mike Seibel.
 Principal authors:        Mike Seibel, Steve Hubert, Laurence Lundblade.
 C-Client library & IMAPd: Mark Crispin.
 Pico, the PIne COmposer:  Mike Seibel.
 Bug triage, user support: David Miller.
 Port integration:         David Miller.
 Documentation:            David Miller, Stefan Kramer, Kathryn Sharpe.
 PC-Pine for DOS:          Mike Seibel.
 PC-Pine for Windows:      Tom Unger.
 Project oversight:        Terry Gray.
 Principal Patrons:        Ron Johnson, Mike Bryant.
 Additional support:       NorthWestNet.
 Initial Pine code base:   Elm, by Dave Taylor & USENET Community Trust.
 Initial Pico code base:   MicroEmacs 3.6, by Dave G. Conroy.
 User Interface design:    Inspired by UCLA's "Ben" mailer for MVS.
 Suggestions/fixes/ports:  Folks from all over!

.\"Copyright 1989-1996 by the University of Washington.
.\"Pine and Pico are trademarks of the University of Washington.
Copyright 1989-1996 by the University of Washington.
Pine i Pico s� zastrze�onymi znakami handlowymi Uniwersytetu w Waszyngtonie

98.05.06
