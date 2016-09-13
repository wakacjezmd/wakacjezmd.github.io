---
layout: page
permalink: /2006/egzamin/2/
---

## 2006 Drugi termin

### Zadanie 3

Udowodnij tożsamość:
$$
\frac{z^n}{(1-z)(1-2z)...(1-nz)}=\sum_{k}{ k\brace n }z^k
$$


<div data-collapse>
  <h4 class="collapsible">Rozwiązanie</h4>
  <div class="solution">
    <p>
      Zadanie polega na tym, by udowodnić, że lewa strona to funkcja tworząca
      liczb \({ k\brace n }\) dla ustalonego \(n\). Można to zrobić przez
      indukcję.
    </p>
    <p>
      Zauważmy, że dla \(n=0\) lewa strona to \(1\), czyli funkcja jest
      tworząca dla \({ k\brace 0 } = [k = 0]\). Warunek bazowy jest spełniony.
      Teraz załóżmy, że funkcja \(\frac{z^{n-1}}{(1-z)(1-2z)...(1-(n-1)z)}\), to
      funkcja tworząca \({ k\brace n-1 }\) (założenie indukcyjne). Wtedy:
      $$
      \sum_{k}{ k\brace n }z^k =
      \sum_{k}(n { k-1\brace n } + { k-1\brace n-1 })z^k =
      nz\sum_{k}{ k-1\brace n}z^{k-1}+z\sum_{k}{ k-1\brace n-1}z^{k-1} =
      $$
      $$
      = nz\sum_{k}{ k\brace n}z^{k}+z\sum_{k}{ k\brace n-1}z^{k}
      $$
    </p>
    <p>
      W przejściu pierwszym skorzystaliśmy z rekurencji dla liczb Stirlinga.
      Oznaczmy teraz \(\sum_{k}{ k\brace n }z^k = f(z)\). Wtedy (założenie
      indukcyjne):
      $$
      f(z)=nzf(z)+z\frac{z^{n-1}}{(1-z)(1-2z)...(1-(n-1)z)} \iff
      (1-nz)f(z)=\frac{z^{n}}{(1-z)(1-2z)...(1-(n-1)z)}
      $$
      Po przerzuceniu \((1-nz)\) na prawą stronę otrzymujemy szukaną tożsamość.
    </p>
  </div>
</div>

---
