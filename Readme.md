# Wakacje z MD

To repozytorium zawiera kod strony [wakacjezmd.github.io](http://wakacjezmd.github.io), na której znajdują się rozwiązania kolokwiów oraz egzaminów z Matematyki Dyskretnej prowadzonej na wydziale [Matematyki, Informatyki i Mechaniki UW](http://www.mimuw.edu.pl).

## Generowanie strony

Do generowania zawartości strony potrzebny jest [jekyll](http://jekyllrb.com) i [redcarpet](https://github.com/vmg/redcarpet). Żeby je zainstalować trzeba ściągnąć ruby i wpisać:
```
(sudo) gem install jekyll
(sudo) gem install redcarpet
```
Po wprowadzeniu zmian w repozytorium dobrze jest włączyć `jekyll serve` z katalogu
głównego i przed pushem sprawdzić lokalnie czy wszystko działa.

## Błędy

Wszystkie błędy można zgłaszać na stronie [issues](https://github.com/wakacjezmd/wakacjezmd.github.io/issues).

## Pliki z rozwiązaniami

W katalogu `_solutions` znajdują się rozwiązania wszystkich egzaminów i kolokwiów podzielone podkatalogami na odpowiednie lata.

Format nazw plików egzaminów powinien spełniać poniższe reguły: `<rok>-egzamin-<nr>.md`.

## Dodawanie rozwiązań

#### LaTeX

We wszystkich plikach można używać LaTeXa. Wzory inline należy umieszczać w nawiasach `\(<wzór>\)`, a wzory mające być wyświetlane w oddzielnych liniach w znacznikach `$$<wzór>$$`.

**UWAGA**

Niestety parser markdown inaczej interpretuje tekst umieszczony w tagach HTML (np. rozwiązania), a
inaczej ten umieszczony normalnie w pliku.

* W treści zadania `_` jest interpretowany jako kursywa, więc we wszystkich wzorach trzeba
wpisywać `\_`.
* W treści zadania `\` jest interpretowany jako escapowanie kolejnego znaku, więc jeżeli chcemy dodać blok
LaTeXa inline to należy napisać `\\(<wzór>\\)`.

#### Nagłówek
Plik egzaminu bądź kolokwium powinien posiadać odpowiedni nagłówek:

```
---
layout: page
permalink: <link do strony>
---
```

Link do egzaminów powinien mieć format `/<rok>/egzamin/<nr>/`.

#### Zadania

Markdown każdego zadania powinien mieć następującą strukturę:

```
###Zadanie <NR>
<TREŚĆ>

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      <CZĘŚĆ ROZWIĄZANIA>
    </p>
    <p>
      <CZĘŚĆ ROZWIĄZANIA>
    </p>
    <p>
      <CZĘŚĆ ROZWIĄZANIA>
    </p>
  </div>
</div>

---
```

#### Nowy egzamin

Po dodaniu nowego pliku egzaminu należy dodać odpowiednie linki w `index.html`.
