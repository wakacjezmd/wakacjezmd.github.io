---
layout: page
permalink: /2020/kolokwium/1/
---

## 2020 Kolokwium 1

### Zadanie 1

<div>
Niech \(p_{n,k}\) oznacza liczbę \(n\)-permutacji mających dokładnie \(k\)
punktów stałych i niech \(r\) będzie ustaloną liczbą naturalną. Uprość sumę:
\[
    \sum_k \binom{k}{r} p_{n,k}
\]
</div>

---

### Zadanie 2

<div>
Niech \(a_n\) oznacza liczbę sposobów pomalowania płotu składającego się z
\(n>0\) sztachet przy pomocy farb w trzech kolorach tak, żeby każdy maksymalny
jednokolorowy spójny fragment płotu składał się z nieparzystej liczby sztachet
(np. \(a_1 = 3 \), \(a_2 = 6\), \(a_3 = 15\)). Znajdź funkcję tworzącą i zwarty
wzór na \(a_n\).
</div>

---

### Zadanie 3

Udowodnij, że liczba podziałów \\(n\\) na składniki dające resztę \\(1\\) lub \\(5\\) z dzielenia przez \\(6\\),
jest równa liczbie podziałów \\(n\\) na różne składniki niepodzielne przez \\(3\\).

<style>
  li { margin-top: 10px }
  ul { margin-bottom: 10px }
</style>

<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    Zdefiniujmy:
    <ul>
      <li> <p> \(F(x)\) – funkcja tworząca podziału \(n\) na składniki dające resztę \(1\) lub \(-1\) modulo \(6\); </p> </li>
      <li> <p> \(G(x)\) – funkcja tworząca podziału \(n\) na <em>różne</em> składniki dające resztę \(1\) lub \(-1\) modulo \(3\). </p> </li>
    </ul>

    Mamy:
    <ul style="margin-bottom:20px">
      <li> <p> \(F(x) = \prod_{k=1}^{\infty} [k \equiv \pm 1 \bmod 6] (1 + x^k + x^{2k} + x^{3k} + \ldots)
                      = \prod_{k=0}^{\infty} \frac{1}{(1 - x^{6k+1})(1 - x^{6k+5})}\) </p> </li>
      <li> <p> \(G(x) = \prod_{k=1}^{\infty} [k \equiv \pm 1 \bmod 3] (1 + x^k)
                      = \prod_{k=0}^{\infty} (1 + x^{3k+1})(1 + x^{3k+2})\) </p> </li>
    </ul>
    Przy \(H(x) = \prod_{k=0}^{\infty} (1 - x^k)\) otrzymujemy równość \(F(x) H(x) = G(x) H(x)\) po prostych
    przekształceniach algebraicznych, co dowodzi tezy.
  </div>
</div>
