# Wakacje z MD

To repozytorium zawiera kod strony [wakacjezmd.github.io], na której znajdują
się rozwiązania kolokwiów oraz egzaminów z Matematyki Dyskretnej prowadzonej
na wydziale [Matematyki, Informatyki i Mechaniki UW].

## Generowanie strony

Do generowania zawartości strony potrzebny jest [jekyll]. Żeby je zainstalować
trzeba ściągnąć Ruby i wpisać:

```sh
(sudo) gem install jekyll
```

Po wprowadzeniu zmian w repozytorium dobrze jest włączyć `jekyll serve`
z katalogu głównego i przed pushem sprawdzić lokalnie czy wszystko działa.

## Błędy

Wszystkie błędy można zgłaszać na stronie [issues].

## Pliki z rozwiązaniami

W katalogu `_solutions` znajdują się rozwiązania wszystkich egzaminów
i kolokwiów podzielone podkatalogami na odpowiednie lata.

Format nazw plików egzaminów powinien spełniać poniższe reguły:
`<rok>-egzamin-<nr>.md`.

## Dodawanie rozwiązań

#### LaTeX

We wszystkich plikach można używać LaTeXa. Wzory inline należy umieszczać
w nawiasach `\(<wzór>\)`, a wzory mające być wyświetlane w oddzielnych liniach
w znacznikach `$$<wzór>$$`.

#### Przydatne wzory

* liczby Stirlinga I rodzaju `{ n\brack m }`
* liczby Stirlinga II rodzaju `{ n\brace m }`

#### UWAGA

Niestety parser Markdown inaczej interpretuje tekst umieszczony w tagach HTML
(np. rozwiązania), a inaczej ten umieszczony normalnie w pliku.

* W treści zadania `_` jest interpretowany jako kursywa, więc we wszystkich
wzorach trzeba wpisywać `\_`.
* W treści zadania `\` jest interpretowany jako escapowanie kolejnego znaku,
więc jeżeli chcemy dodać blok LaTeXa inline to należy napisać `\\(<wzór>\\)`.

#### Nagłówek

Plik egzaminu bądź kolokwium powinien posiadać odpowiedni nagłówek:

```md
---
layout: page
permalink: <link do strony>
---
```

Link do egzaminów powinien mieć format `/<rok>/egzamin/<nr>/`.

#### Zadania

Markdown każdego zadania powinien mieć następującą strukturę:

```md
### Zadanie <NR>

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

[issues]: https://github.com/wakacjezmd/wakacjezmd.github.io/issues
[jekyll]: http://jekyllrb.com
[Matematyki, Informatyki i Mechaniki UW]: http://www.mimuw.edu.pl
[wakacjezmd.github.io]: http://wakacjezmd.github.io


