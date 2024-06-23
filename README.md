**Projekt név: Rajkos Matchmaker**

A projekt lényegében egy "társkereső" rajkos/belsős használatra. A végeredmény egy **Streamlit** felület, amely **két funkcióval** rendelkezik: 
(1) Két legördülő menüből ki lehet választani 1-1 nevet, és egy gombnyomás után látjuk is, hány százalékban passzolnak össze (mennyire alkotnának jó párt). 
(2) Egy legördülő menüből ki lehet választani egy nevet, illetve hogy milyen típusú kapcsolatot keres (hetero, homo, mindegy), és ez alapján kiderül, ki az az 5 személy, aki az az adott illetőhöz a legjobban passzol, és hány százalékban.

Az **adatok** egy Google Form-os kérdőívből érkeznek, amely 25 db kérdést tartalmaz összesen (13 db Rajkkal kapcsolatos kérdés és 12 db személyiségteszt-jellegű kérdés). 
A kérdőívben feleletválasztós kérdések szerepeltek 1 vagy több választási lehetőséggel, illetve 1 db nyitott kérdés. Kizárólagosan a kérdőívet kitöltő kollégisták kerültek bele a Rajkos Matchmaker-be (a projekt leadásáig 71 fő). 
Az emberek "összematcheléséhez" először szubjektív módon/internetes keresgéléssel kitaláltam, mely kérdésnél milyen válaszok vagy válaszkombinációk mennyire passzolnak össze, ezután ezekre megírtam a kódokat. A logika, amit követtem az volt, hogy **a hasonló emberek** alkotnak jó párt. A kérdések különböző súllyal számítanak a végső "match-százalék" kiszámításában (1-4-7%).

Amennyiben valaki a későbbiekben **bővíteni szeretné** a projektet, az új kitöltőket is tartalmazó csv fájlt a Rajkos match-maker.ipynb fájlba kell betöltenie. Ezen felül két dolgot szükséges manuálisan elvégeznie: 
(1) Ha valaki nem a teljes nevével töltötte ki a kérdőívet, érdemes kicserélni a dataframe-ben, hogy utána a teljes név jelenjen meg a legördülő listában is. 
(2) A 2. funkció teljessége miatt a kitöltők nevét is manuálisan kell kitölteni, mert ezt sajnos a kérdőívben elfelejtettem megkérdezni. Nagyszámú kitöltő esetén erre érdemes kódot írni, vagy további használat előtt kibővíteni a Google Form-ot nemre vonatkozó kérdéssel.

Jó szórakozást! :)
