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



