# GateProject
A python project that allows an administrator to sign up employees and track their work hours in a data base.

for the project to work, you must have a 'GmailPassw.txt' file with your own gmail key generated and change the sender's email adress in 'Details.py'.

Context:

Scrieti un program python care permite monitorizarea orelor lucrate de angajatii unei companii. Datele pe care le primiti ca parametru provin de la punctele de access dintr-o cladire de birouri. Orice persoana, pentru a intra in cladire, sau pentru a iesi, trebuie sa valideze cardul de acces. Prin validare, se obtine id-ul persoanei care detine cartela, ora validarii precum si sensul (intrare sau iesire). 
In cladire pot exista 2 tipuri de porti prin care se face accesul. Primul tip salveaza toate aceste date intr-un fisier text sau csv care au aceeasi structura precum exemplele atasate. Al doilea tip de poarta, transmite in timp real catre server intrarile si iesirile prin internet, in format json. 
Cerinte: 
•	Creati un repository pe github (trebuie sa il faceti public pentru a incepe un portofoliu de aplicatii care va poate fi util la viitoare interviuri de angajare). Incarcati acolo tot codul pe care il dezvoltati. Va fi nevoie de un pull request pentru fiecare functionalitate implementata. 
•	In cadrul dezvoltarii folositi conceptele POO (incapsulare, mostenire, polimorfism, abstractizare)
•	Creati o functionalitate prin care un administrator poate inregistra utilizatori. Utilizatorii vor fi salvati intr-o tabela a bazei de date unde vom inregistra ID,Nume,Prenume, Companie, IdManager. Aceste detalii sunt transmise prin intermediul unui request prin care se transmit toate detaliile necesare. 
•	Primul tip de poarta: In cadrul proiectului va exista un folder numit “intrari” in care administratorii cladirii vor incarca fisierele generate de primul tip de porti. Programul va citi fiecare fisier din acel director, va incarca datele in baza de date, in tabela “access” si apoi va muta fisierul intr-un director numit backup_intrari. Numele fisierelor va avea formatul Poarta[numar_poarta].[tip_fisier] (de exemplu Poarta1.csv). Numele portii pe care se face fiecare intrare trebuie salvat in baza. Programul trebuie sa citeasca fisierul imediat ce acesta apare. (Verifica la fiecare iteratie daca exista fisiere noi in folderul intrari).
•	Al doilea tip de poarta: La nivelul programului, creati un endpoint care primeste ca parametru un json cu urmatorul format si il salveaza in baza de date: 
{
     “data”:”2023-05-21T13:49:51.141Z”,
     “sens”:”in”,
     “idPersoana”:10,
     “idPoarta”:3
}
•	Creati o functionalitate care sa ruleze zilnic, dupa ora 20:00, care sa calculeze numarul de ore lucrate de fiecare angajat, pe baza intrarilor si iesirilor inregistrate la porti. Pentru fiecare angajat care nu a lucrat 8 ore intr-o zi, un email va fi transmis catre managerul acestuia. De asemenea, lista cu numele angajatilor va fi scrisa si in directorul backup cu numele <data_curenta>_chiulangii.csv si <data_curenta>_chiulangii.txt si va contine angajatii in formatul Nume,OreLucrate atat in csv cat si in txt ( in txt nu va avea header) 
•	Adaugati orice functionalitate pe care o considerate interesanta sau utila. 

Hint: O persoana poate intra si iesi pe diferite porti. Toate intrarile si iesirile trebuie luate in calcul. 
