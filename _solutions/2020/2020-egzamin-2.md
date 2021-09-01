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

Udowodnij, że w \\(n\\)-wierzchołkowym grafie spójnym \\(G\\) zachodzi oszacowanie:

\\[
    \chi(G) + \textrm{diam}(G) \leq n+1.
\\]

Pokaż, że dla każdego \\(d > 0\\) i dostatecznie dużego \\(n\\) istnieje graf \\(n\\)-wierzchołkowy o średnicy \\(d\\),
dla którego to oszacowanie jest dokładne.

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
  Rozważmy najdłuższą ścieżkę w grafie pomiędzy wierzchołkami \(v_s\), \(v_e\). Da się ją pokolorować na dwa kolory; w
  przeciwnym razie pomiędzy niesąsiednimi wierzchołkami na ścieżce istnieje krawędź, czyli istnieje krótsza ścieżka z
  \(v_s\) do \(v_e\) – sprzeczność. Pozostałych wierzchołków jest \(n-(\mathrm{diam}(G)+1)\), co daje nam górne
  oszacowanie na minimalną liczbę ich kolorowań, stąd otrzymujemy:

  \[
      \chi(G) + \mathrm{diam}(G) \leq 2 + n-(\mathrm{diam}(G)+1) + \mathrm{diam}(G) = n + 1.
  \]

  Przykładem grafu, dla którego to oszacowanie jest dokładne, jest ścieżka \(n\)-elementowa, którą oczywiście można
  pokolorować na minimalnie dwa kolory, a której średnica wynosi \(d=n-1\). Jeśli chcemy znaleźć taki \(n\)-graf dla
  dowolnego \(d\) i dowolnego \(n \geq d+1\), to rozważmy ścieżkę \(d+1\)-elementową, której dwa ostatnie wierzchołki są również
  wierzchołkami \((n -(d+1)+ 2)\)-kliki. Klikę w tym grafie możemy pokolorować na minimalnie \(n - d + 1\) kolorów,
  natomiast pozostałe wierzchołki ścieżki na dowolne dwa kolory, na które pokolorowana została klika. Mamy więc
  \(\chi(G) + \mathrm{diam}(G) = n - d + 1 +d - d = n+1\), czyli oszacowanie jest dokładne.
  </div>
</div>

---

### Zadanie 4


Znajdź liczbę uporządkowanych par liczb naturalnych \\(\langle a,b \rangle\\) takich, że \\(\text{NWW}(a,b) = 10!\\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Odnotujmy, że:

      \[
          10! = 2^8 \cdot 3^4 \cdot 5^2 \cdot 7^1
      \]

      Wiadomo (m.in. z wykładu), że jeśli \(a = p_1^{\alpha_1} p_2^{\alpha_2} \ldots p_k^{\alpha_k}\) oraz
      \(b = p_1^{\beta_1} p_2^{\beta_2} \ldots p_k^{\beta_k}\), to wówczas:

      \[
          \mathrm{NWW}(a,b) = p_1^{\max(\alpha_1, \beta_1)} p_2^{\max(\alpha_2, \beta_2)} \ldots\, p_k^{\max(\alpha_k, \beta_k)}.
      \]

      Czyli żadna z liczb \(\langle a,b \rangle\) nie może mieć dzielnika różnego od \(2, 3, 5, 7\), a jedna z nich musi
      mieć go w potędze takiej, jak \(10!\).
    </p>

    <p>
      Zamiast par liczb \(a, b\) możemy więc rozpatrywać więc pary ciągów
      \((q_1, q_2, q_3, q_4),\, (t_1, t_2, t_3, t_4)\) takie, że \( (\max(q_1, t_1), \ldots, \max(q_4,
      t_4)) = (8, 4, 2, 1)\). Nietrudno zauważyć, że takich ciągów jest:

      \[
          \prod_{i \in \{ 8, 4, 2, 1 \}}  \left( 2i + 1 \right) = 2295.
      \]

      (Jeśli np. liczba \(q_1 = 0\ldots7\), wówczas \(t_1 = 8\), i na odwrót, co daje nam \(2i\), a także może być \(q_1
      = t_1 = 8\), co daje nam \(1\)).
    </p>
  </div>
</div>
