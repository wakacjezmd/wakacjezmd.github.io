---
layout: page
permalink: /2020/egzamin/2/
---

## 2020 Egzamin poprawkowy

### Zadanie 1

---

### Zadanie 2

Znajdź współczynnik \\(x_1 x_2 \cdots x_6\\) przy wyrażeniu:

\\[
    (X - x_2) (X - x_5) \prod_{i=1}^{5} (X - x_{i-1} - x_{i+1}),
\\]

gdzie \\( X = x_1 + x_2 + \cdots + x_6 \\). *Uwaga:* to zadanie należy rozwiązać bez wspomagania komputerowego.

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Przyjmijmy \(D := X\). Po rozpisaniu otrzymujemy:

      \[
          \underbrace{(D-x_2)(D-x_2-x_4)(D-x_4-x_6)}_{\text{grupa } A} \; \underbrace{(D-x_5)(D-x_1-x_3)(D-x_3-x_5)}_{\text{grupa } B}.
      \]

      Rozpiszmy składniki jednej grupy, w każdym kroku usuwając jednak składniki, w których zmienne się dublują (np. \(x_4 x_4\)),
      co uniemożliwia <q>zwinięcie</q> się do szukanego wyrażenia.

      \[
          \begin{align}
                  &\; (D-x_2)(D-x_2-x_4)(D-x_4-x_6) \\
          \approx &\; (D - x_2)(D^2 - D[2x_2 + 2x_4 + x_6] + x_2 x_4 + x_2 x_6 + x_4 x_6) \\
          \approx &\; (D^3 - D^2[2x_2 + 2x_4 + x_6] + D[3 x_4 x_2 + 2 x_6 x_2 + x_4 x_6] - x_2 x_4 x_6)
          \end{align}
      \]

      Szczęśliwie dla nas, grupy \(A\) i \(B\) są <q>symetryczne</q>, mamy więc \(x_2 \mapsto x_5\), \(x_4 \mapsto
      x_3\), \(x_6 \mapsto x_1\). Czyli szukamy współczynnika przy \(x_1 x_2 \cdots x_6\) w poniższym wyrażeniu.

      \[
          \begin{align}
                &\; (D^3 - D^2[2x_2 + 2x_4 + x_6] + D[3 x_4 x_2 + 2 x_6 x_2 + x_4 x_6] - x_2 x_4 x_6) \\
          \cdot &\; (D^3 - D^2[2x_5 + 2x_3 + x_1] + D[3 x_3 x_5 + 2 x_1 x_5 + x_3 x_1] - x_5 x_3 x_1)
          \end{align}
      \]

      Dalej możemy po prostu obliczyć współczynniki przy szukanym iloczynie, patrząc na ile sposobów (i z jakim znakiem) można go uzyskać
      w kolejnych parach (np. dla \(D^3 D^3\) jest to \(6!\)).

      \[
          \begin{align}
            &6! + 2(- 5 \cdot 5! + (3+2+1) 4! - 3!)                     \\
          +\; &4! \cdot 5^2 + 2(-(3+2+1) \cdot 5 \cdot 3! + 5 \cdot 2!) \\
          +\; &(3+2+1)^2 \cdot 2! - 2 \cdot 6                           \\
          +\; &1                                                        \\
          \end{align}
      \]

      Wynikiem tego długiego wyrażenia jest \(117\). Dla potwierdzenia <a href="/downloads/2020_egzamin2_3.py" download>brut w Pythonie</a>.
    </p>
  </div>
</div>

---

### Zadanie 3

---

### Zadanie 4


