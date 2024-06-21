## MOVIE TRACKER:

Sustav za praćenje filmova na netu

Jednostavna web aplikacija koja prati popis omiljenih filmova korisnika. Implementira mogućnost unosa, prikaza, brisanja i uređivanja omiljenih filmova. Također, kroz jednostavne grafove vizualizira filmove kroz različite filtere.

Implementira:
-unos filma (naziv filma, godina izlaska, žanr, ocjena, status je li korisnik pogledao film ili ne).

-Uredivanje stavki filma, te brisanje određenog filma.

-Prikaz svih filmova, te prikaz najnovijih filmova i najbolje ocijenjenih.

-Prikaz ukupnog broja filmova, te broj pogledanih i nepogledanih filmova.

-Grafički prikaz filmova po žanru, po ocjeni i po godini izlaska.

## Use case dijagram

![alt text](https://github.com/brebic4/Movie-tracker/blob/main/Use%20Case%20-%20Sustav%20za%20pra%C4%87enje%20filmova%20na%20netu.png)

## Instalacija

Potrebno je ući u terminal u Visual Studio Code-u te pratiti sljedeće naredbe:

Skidanje koda s GitHub-a:

    cd ~/Downloads
    git clone https://github.com/brebic4/Movie-tracker.git
    cd Movie_tracker

Docker tutorial:

    docker build -t movietracker .
    docker run -p 5000:5000 movietracker
