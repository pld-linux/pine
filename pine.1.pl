.\" {PTM/LK/0.1/30-01-1999/"program do czytania poczty"}
.\" T³umaczenie: 30-01-1999 £ukasz Kowalczyk (lukow@tempac.okwf.fuw.edu.pl)
.TH pine 1 "Wersja 4.04"
.SH NAZWA
pine \- program do czytania grup dyskusyjnych i poczty elektronicznej
.SH SK£ADNIA

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

Pine jest pe³noekranowym programem do czytania wiadomo¶ci. W swojej
domy¶lnej konfiguracji Pine prezentuje celowo ograniczony zestaw opcji
przeznaczony dla pocz±tkuj±cego u¿ytkownika. Istnieje jednak wci±¿ rosn±ca
lista opcjonalnych mo¿liwo¶ci przeznaczonych dla zaawansowanych u¿ytkowników.
.I pinef 
jest wersj± programu Pine u¿ywaj±cym klawiszy funkcyjnych zamiast
jednoliterowych poleceñ.
W podstawowym zestawie poleceñ znajduj± siê nastêpuj±ce opcje:
.IP
View (przegl±danie), Save (zapis), Export (zapis do pliku), 
Delete (usuwanie), Print (drukowanie), Reply (odpowiadanie) i 
Forward (dalsze przesy³anie wiadomo¶ci).
.IP
Tworzenie wiadomo¶ci w prostym edytorze (Pico) z automatycznym ³amaniem
linii i kontrol± pisowni. Edycja wiadomo¶ci mo¿e byæ odk³adana do
pó¼niejszej kontynuacji.
.IP
Pe³noekranowy wybór i zarz±dzanie folderami.
.IP
Ksi±¿ka adresowa, w której znajduj± siê czêsto u¿ywane lub po prostu d³ugie
adresy. Mo¿na definiowaæ w³asne listy dystrybucyjne. Adresy mog± byæ
pobierane z otrzymywanych wiadomo¶ci bez potrzeby odpowiadania na nie.
.IP
Sprawdzanie, czy otrzymano nowe wiadomo¶ci jest wykonywane co 2.5 minuty
oraz po pewnych poleceniach, np. od¶wie¿aniu ekranu (Ctrl-L).
.IP
Kontekstowa pomoc.
.PP
Pine obs³uguje MIME (Multipurpose Internet Mail Extensions), internetowy
standard reprezentacji wieloczê¶ciowych i multimedialnych danych w
wiadomo¶ciach. Pine pozwala na zapis obiektów MIME do plików i w pewnych
sytuacjach mo¿e uruchomiæ odpowiedni program do ogl±dania takich wiadomo¶ci.
Pine u¿ywa systemowego pliku konfiguracyjnego 
.I mailcap 
by uruchomiæ w³a¶ciwy program do obs³ugi poszczególnych obiektów MIME.
Wbudowany program do tworzenia wiadomo¶ci nie posiada w³a¶ciwo¶ci
multimedialnych, lecz dowolny typ danych - w³±cznie z multimedialnymi - 
mo¿e zostaæ umieszczony w wiadomo¶ci jako za³±cznik. Pozwala to posiadaczom
programów pocztowych zgodnych z MIME na wymianê sformatowanych dokumentów,
arkuszy kalkulacyjnych, plików graficznych etc. przez pocztê elektroniczn±.
.PP
Do obs³ugi lokalnych i zdalnych folderów pocztowych Pine u¿ywa interfejsu
.I c-client
(c-client messaging API).
Ta biblioteka pozwala na wykonywanie wielu niskopoziomowych funkcji obs³ugi
poczty, w³±czaj±c w to funkcje obs³ugi wielu formatów pocztowych, protoko³u
IMAP (Internet Message
Access Protocol) oraz NNTP (Network News Transport Protocol). Poczta
wychodz±ca jest zazwyczaj przekazywana programowi 
.IR sendmail ,
ale mo¿e byæ wysy³ana bezpo¶rednio przez SMTP (Simple Mail Transfer Protocol).
.SH OPCJE
.if n .ta 2.8i
.if t .ta 2.1i
Pine rozpoznaje nastêpuj±ce opcje linii poleceñ:
.IP \fIadres\fR 20
Wys³anie wiadomo¶ci na podany adres e-mailowy. Pine uruchomi siê w trybie tworzenia
wiadomo¶ci.
.IP \fB-a\fR 20
Specjalny anonimowy tryb dzia³ania dla UWIN* (* patrz ni¿ej)
.IP \fB-c\ \fInumer_kontekstu\fR 20
mumer_kontekstu jest numerem odnosz±cym siê do kolekcji folderów, do którego
powinien zostaæ zastosowany argument
.I -f
linii poleceñ. Domy¶lnie opcja
.I -f
jest stosowana do pierwszej zdefiniowanej kolekcji folderów.
.IP \fB-d\ \fIpoziom_diagnostyki\fR 20
Wypisywanie informacji diagnostycznych na poziomie 
.I poziom_diagnostyki
(0-9) do bie¿±cego pliku
.IR .pine-debug[1-4] .
Warto¶æ 0 wy³±cza informacje diagnostyczne i wstrzymuje tworzenie pliku
.IR .pine-debug .

.IP \fB-d\ \fIklucz[=warto¶æ]\fR 20
Szczegó³owy opis tworzenia informacji diagnostycznych; "flush"
powoduje zapisywanie plików diagnostycznych bez buforowania, "timestamp"
do³±cza do ka¿dego komunikatu czas jego wygenerowania, "imap=n" (gdzie n
przybiera warto¶ci od 0 do 4) powoduje do³±czanie telemetrii (ang.
telemetry) IMAP na podanym poziomie, "numfiles=n" (gdzie n przybiera
warto¶æ od 0 do 31) opisuje ilo¶æ tworzonych plików diagnostycznych i
wreszcie "verbose=n" (gdzie n przybiera warto¶ci od 0 do 9) jest odwrotnym
progiem poziomu generowania ogólnych wiadomo¶ci o dzia³aniu programu.
.IP \fB-f\ \fIfolder\fR 20
Otwarcie folderu (w pierwszej zdefiniowanej kolekcji folderów) zamiast INBOX.
.IP \fB-F\ \fIplik\fR 20
Otwarcie podanego pliku tekstowego w przegl±darce programu Pine.
.IP \fB-h\fR 20
Pomoc: lista rozpoznawanych opcji linii poleceñ.
.IP \fB-i\fR 20
Otwarcie indeksu folderów po uruchomieniu programu.
.IP \fB-I\ \fIklawisze\fR 20
Lista klawiszy (rozdzielona przecinkami), których naci¶niêcie Pine powinien
zasymulowaæ zaraz po uruchomieniu.
.IP \fB-k\fR 20
Wywo³ywanie poleceñ klawiszami funkcyjnymi. Identyczne dzia³anie ma
uruchomienie programu pinef.
.IP \fB-n\ \fInumer\fR 20
Uruchomienie programu z automatycznym otworzeniem wiadomo¶ci o podanym
numerze.
.IP \fB-nr\fR 20
Specjalny tryb dla UWIN*
.IP \fB-o\fR 20
Otwarcie pierwszego folderu w trybie tylko do odczytu.
.IP \fB-p\ \fIplik_konfiguracyjny\fR 20
U¿ycie podanego pliku w charakterze pliku konfiguracyjnego zamiast
domy¶lnego .pinerc.
.IP \fB-P\ \fIplik_konfiguracyjny\fR 20
U¿ycie podanego pliku w charakterze pliku konfiguracyjnego zamiast
domy¶lnego pliku systemowego
.IR pine.conf .
.IP \fB-r\fR 20
Uruchomienie w trybie demonstracyjnym o ograniczonej funkcjonalno¶ci. 
.I Pine
bêdzie wysy³a³ pocztê tylko do siebie samego, a funkcje typu save i export
nie bêd± dzia³a³y.
.IP \fB-z\fR 20
Udostêpnienie mo¿liwo¶ci przeniesienia programu Pine do t³a klawiszem ^Z lub
sygna³em SIGTSTP.
.IP \fB-conf\fR 20
Utworzenie wzorcowego pliku jako szablonu dla systemowego pliku
konfiguracyjnego
.I pine.conf
na standardowym wyj¶ciu. Jest to inny plik ni¿ indywidualny dla ka¿dego
u¿ytkownika 
.IR .pinerc .
.IP \fB-create_lu\ \fIksi±¿ka_adresowa\ \fIporz±dek_sortowania\fR 20
Utworzenie dodatkowego indeksu dla ksi±¿ki adresowej o podanej nazwie i
posortowanie jej w podanym porz±dku. Mo¿liwe warto¶ci dla porz±dku
sortowania, to
.IR "dont-sort (brak sortowania)" ,
.IR "nickname (skrót nazwy adresata)" ,
.IR "fullname (pe³na nazwa adresata)" ,
.IR "nickname-with-lists-last (skrót nazwy, ale listy na koñcu)" ,
or
.IR "fullname-with-lists-last (pe³na nazwa, ale listy na koñcu)" .

Jest to u¿yteczne do tworzenia globalnych lub dzielonych ksi±¿ek adresowych.
Po utworzeniu w ten sposób indeksu, plik powinien zostaæ przeniesiony lub
skopiowany w taki sposób, by zmianie nie uleg³ czas modyfikacji. Czas
modyfikacji ksi±¿ki adresowej jest zachowywany w nowotworzonym pliku z
indeksem i przy ka¿dym uruchomieniu programu sprawdzany. Je¿eli czas
modyfikacji ksi±¿ki adresowej ulegnie zmianie, pine utworzy indeks od nowa.
Innymi s³owy, po utworzeniu indeksu za pomoc± opisywanej opcji, nie kopiuj
ksi±¿ki adresowej do jej docelowego po³o¿enia w taki sposób, który zmieni
jej czas modyfikacji.
.IP \fB-pinerc\ \fIplik\fR 20
Zapisanie bie¿±cej konfiguracji programu do podanego pliku.
.IP \fB-sort\ \fIporz±dek_sortowania\fR
Posortowanie ekranu FOLDER INDEX w jednej z nastêpuj±cych kolejno¶ci:
.I arrival (czas nadej¶cia), subject (temat), from (pole from), date (data),
.I size (rozmiar), orderedsubj (pseudo w±tek)
lub
.I reverse (odwrotna kolejno¶æ). Arrival
jest domy¶lnym porz±dkiem sortowania. Porz±dek OrderedSubj symuluje
sortowanie pod k±tem w±tków. Ka¿dy porz±dek sortowania mo¿e zostaæ odwrócony
przez dodanie do niego 
.IR /reverse .

.I Reverse
bez dodatkowych opcji dzia³a jak
.IR arrival/reverse .
.IP \fI-option\=\fIwarto¶æ\fR 20
Nadanie opcji konfiguracyjnej podanej warto¶ci. Np. 
-signature-file=sig1 lub -feature-list=signature-at-bottom
(Uwaga: warto¶ci opcji feature-list s± addytywne)
.PP
* UWIN = University of Washington Information Navigator
.SH KONFIGURACJA

Istnieje kilka poziomów konfiguracji programu Pine. Warto¶ci konfiguracyjne
na danym poziomie maj± wy¿szy priorytet ni¿ te warto¶ci na ni¿szych poziomach.
W porz±dku rosn±cego priorytetu:

 o wbudowane warto¶ci domy¶lne.
.br
 o plik
.I pine.conf
dla ca³ego systemu.
.br
 o osobisty plik
.I .pinerc 
ka¿dego u¿ytkownika (warto¶ci w nim mo¿na ustawiaæ za pomoc± menu
Setup/Config).
.br
 o opcje linii poleceñ
.br
 o plik
.I pine.conf.fixed
dla ca³ego systemu.

Istnieje wyj±tek od zasady, w my¶l której warto¶ci konfiguracyjne s±
zastêpowane przez warto¶ci tych samych opcji o wy¿szym priorytecie: 
warto¶ci nadawane zmiennej feature-list s± addytywne, lecz mog± byæ
zanegowane do³±czeniem "no-" na pocz±tku danej warto¶ci dla tej zmiennej.
Pine w systemie Unix u¿ywa nastêpuj±cych zmiennych ¶rodowiskowych.

  TERM
.br
  DISPLAY     (okre¶la, czy Pine mo¿e wy¶wietlaæ za³±czniki typu IMAGE).
.br
  SHELL       (domy¶ln± warto¶ci± jest /bin/sh, je¿eli ta zmienna nie jest
ustawiona).
.br
  MAILCAPS    (lista ¶cie¿ek do plików mailcap rozdzielonych ¶rednikami).
  
.SH PLIKI
.if n .ta 2.8i
.if t .ta 2.1i

/var/mail/xxxx		Domy¶lny folder dla przychodz±cej poczty.
.br
~/mail	Domy¶lny katalog dla folderów.
.br
~/.addressbook	Domy¶lna nazwa pliku z ksi±¿k± adresow±.
.br
~/.addressbook.lu	Domy¶lna nazwa pliku z indeksem ksi±¿ki adresowej.
.br
~/.pine-debug[1-4]	Pliki, do których zapisywane s± komunikaty diagnostyczne.
.br
~/.pinerc	Osobisty plik konfiguracyjny.
.br
~/.newsrc	Opis stanu subskrybowanych grup dyskusyjnych.
.br
~/.signature	Domy¶lna nazwa pliku z sygnatur±.
.br
~/.mailcap	Osobisty plik mailcap (man mailcap(4))
.br
~/.mime.types	Osobiste rozszerzenie rozpoznawanych typów MIME
.br
/etc/mailcap	Systemowy plik mailcap (man mailcap(4))
.br
/etc/mime.types	Systemowe opis rozpoznawanych typów MIME
.br
/usr/share/info/pine.info	Lokalny wska¼nik do administratora systemu
.br
/etc/pine.conf	Systemowy plik konfiguracyjny
.br
/etc/pine.conf.fixed  Plik konfiguracyjny, którego ustawienia nie mog± byæ zmieniane
.br
/tmp/.\\var\\mail\\xxxx		Pliki blokuj±ce dla ka¿dego folderu
.br
~/.pine-interrupted-mail	Wiadomo¶æ, której tworzenie zosta³o przerwane
.br
~/mail/postponed-msgs	Wiadomo¶æ, której tworzenie zosta³o od³o¿one na pó¼niej
.br
~/mail/sent-mail	Archiwum wys³anych wiadomo¶ci
.br
~/mail/saved-messages	Domy¶lny folder na zapisywane wiadomo¶ci
.SH "ZOBACZ TAK¯E"

pico(1), binmail(1), aliases(5), mailaddr(7), sendmail(8), spell(1), imapd(8)

.br
Grupa dyskusyjna:  comp.mail.pine
.br
Pine Information Center:  http://www.washington.edu/pine
.br
Dystrybucja ¼ród³owa:  ftp://ftp.cac.washington.edu/pine/pine.tar.Z
.br
Pine Technical Notes (informacje techniczne), zawarte w dystrybucji ¼ród³owej
.br
Interfejs (API) biblioteki przesy³ania wiadomo¶ciC-Client, zawarty w
dytrybucji ¼ród³owej.
.SH PODZIÊKOWANIA
.na 
.nf

Zespó³ rozwoju programu Pine (czê¶æ UW Office 
of Computing & Communications) na Uniwersytecie w Waszyngtonie
(University of Washington):

.\" celowo nie przet³umaczone

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
Pine i Pico s± zastrze¿onymi znakami handlowymi Uniwersytetu w Waszyngtonie

98.05.06
