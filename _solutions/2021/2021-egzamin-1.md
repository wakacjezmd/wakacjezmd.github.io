---
layout: page
permalink: /2021/egzamin/1/
---

## 2021 Egzamin - Pierwszy termin

### Zadanie 1

Dla \\(k,m,r \in \mathbb{N}\\), \\(r > 0\\), udowodnij tożsamość:

\\[ \sum_{i=1}^{k}\sum_{j=0}^{m}\binom{m}{j}{r\brace i}{m-j\brace k-i} i^j = {m+r\brace k} \\]

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      <em>Interpretacja.</em> Bierzemy zbiór, który jest sumą rozłącznych zbiorów wielkości \(m\) i
      \(r\), a następnie dzielimy go na \(k\) niepustych bloków.
    </p>
    <p>
      <em>Prawa strona.</em> Zsumowany (\(m+r\))-zbiór dzielimy na \(k\) niepustych bloków.
    </p>
    <p>
      <em>Lewa strona.</em><br/>
      <ul>
        <li style="margin-bottom: 7px">
            \({r \brace i}\) – \(r\)-zbiór dzielimy na \(i\) bloków (gdzie \(i = 1{\ldots}k\));
        </li>
        <li style="margin-bottom: 7px">
            \(\binom{m}{j} \cdot i^j\) – wybieramy \(j\) elementów z \(m\)-zbioru, które rozdzielamy do \(i\) bloków (gdzie \(j = 1{\ldots}m\));
        </li>
        <li style="margin-bottom: 7px">
            \({m-j \brace k-j}\) – pozostałe \(m-j\) elementów z \(m\)-zbioru rozdzielamy do \(k-i\) bloków.
        </li>
      </ul>
    </p>
    <p>
      Czy w ten sposób uzyskamy wszystkie podziały i każdy dokładnie raz? Weźmy dowolny podział sumy
      \(m\) i \(r\) zbiorów. Zaznaczmy te bloki, w których występują elementy z \(r\) zbioru.
      Wyznacza nam to jednoznacznie wartość \(i\) z powyższego wzoru. Policzmy, ile w tych blokach
      znajduje się dołączonych elementów z \(m\) zbioru. Wyznacza nam to jednoznacznie wartość
      \(j\).
    </p>
  </div>
</div>

---

### Zadanie 2

Udowodnij, że współczynnikiem \\(x^k\\) w rozwinięciu \\((1+x+x^2+x^3)^n\\) jest \\(\sum_{j=0}^{n} \binom{n}{j} \binom{n}{k-2j}\\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Odnotujmy, że \((1+x+x^2+x^3)^n = (1+x^2)^n (1+x)^n\). Na ile sposobów możemy uzyskać \(x^k\)
      z tego iloczynu? Jeśli z pierwszego nawiasu wybierzemy \(j\) razy czynnik \(x^2\), to
      pozostanie nam brakujący czynnik \(x^{k-2j}\). Możemy go uzyskać, wybierając \(k-2j\) razy
      czynnik \(x\) z drugiego nawiasu. Różnych sposobów wyboru z pierwszego nawiasu jest
      \(\binom{n}{j}\); z drugiego – \(\binom{n}{k-2j}\).
    </p>
  </div>
</div>

---

### Zadanie 3

Niech \\(\mathrm{fr}(x) = x− \lfloor x \rfloor\\) oznacza *część ułamkową* liczby rzeczywistej \\(x\\). Oblicz (bez wspomagania komputerowego) \\(\mathrm{fr}(998!/101^{10})\\).

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Odnotujmy, że \( \mathrm{fr}\big( \frac{998!}{101^{10}} \big) = \mathrm{fr}\big(\frac{q}{101}\big) 
                     = \mathrm{fr}\big(\frac{q \bmod 101}{101}\big) \). Dalej rozpatrujemy kongruencję \(\text{mod }
                     101\) z licznika.

      \[ \begin{align*}
          q &\equiv \textstyle \frac{998!}{101^{9}} \\[3pt]
          q &\equiv (1 \cdots 100) \cdot 1 \cdot (102 \cdots 201) \cdot 2 \cdots 9 \cdot (910 \cdots 1009) \cdot (1009^{-1} \cdots 999^{-1}) \\[5pt]
          q &\equiv (1 \cdots 100)^{10} (1 \cdot 2 \cdots 9) (-1)^{-1} (-2)^{-1} \cdots (-11)^{-1}   \\[5pt]
         \end{align*}
      \]

    Liczba \(101\) jest pierwsza, więc z twierdzenia Wilsona mamy, że \(1 \cdots 100 \equiv -1 \; (\text{mod } 101)\). Z
    pierwszości \(101\) wynika też, że dla każdej liczby \(a \in \{1, 2, \ldots, 100\}\) istnieje jednoznaczna
    odwrotność \(\text{mod } 101\) z tego samego zbioru. Obydwa te fakty zostały dowiedzione na ćwiczeniach. Odnotujmy
    dodatkowo, że \(x^{-1} y^{-1} = (xy)^{-1}\) (co bardzo łatwo pokazać).

      \[ \begin{align*}
          q &\equiv (-1)^{20} \cdot (12 \cdot 34 \cdot 56 \cdot 78) \cdot (12 \cdot 34 \cdot 56 \cdot 78)^{-1} \cdot (9) \cdot (-9 \cdot 10 \cdot 11)^{-1} \\[3pt]
          q &\equiv 9 (20)^{-1} \\[3pt]
         \end{align*}
      \]

    Odwrotność \(\text{mod } 101\) liczby \(20\) możemy wyznaczyć, korzystając z rozszerzonego algorytmu Euklidesa.
    Otrzymujemy \( 1 = (-5) \cdot 20 + 101 \), więc odwrotność wynosi \( -5 \). Stąd \(q \equiv 9 \cdot (-5) \equiv 56 \; (\text{mod } 101)\).
      \[
         \mathrm{fr}\left(\frac{998!}{101^{10}}\right) = \frac{56}{101}.
      \]
    </p>
  </div>
</div>

