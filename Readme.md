# Wakacje z MD

To repozytorium zawiera kod strony [wakacjezmd.github.io](http://wakacjezmd.github.io), na której znajdują się rozwiązania kolokwiów oraz egzaminów z Matematyki Dyskretnej prowadzonej na wydziale [Matematyki, Informatyki i Mechaniki UW](http://www.mimuw.edu.pl).

## Pliki z rozwiązaniami

W katalogu `_solutions` znajdują się rozwiązania wszystkich egzaminów i kolokwiów podzielone podkatalogami na odpowiednie lata.

Format nazw plików egzaminów powinien spełniać poniższe reguły: `<rok>-egzamin-<nr>.md`.

## Dodawanie rozwiązań

#### LaTeX

We wszystkich plikach można używać LaTeXa. Wzory inline należy umieszczać w nawiasach `\(<wzór>\)`, a wzory mające być wyświetlane w oddzielnych liniach w znacznikach `$$<wzór>$$`.

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
  <div>
    <ROZWIĄZANIE>
  </div>
</div>

---
```

#### Nowy egzamin

Po dodaniu nowego pliku egzaminu należy dodać odpowiednie linki w `index.html`.
