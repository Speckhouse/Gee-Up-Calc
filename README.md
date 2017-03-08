# Gee-Up-Calc
GUI calculator for an IVS project.

## TODO
* Kazdy ma vytvorit Doxyfile a potom porovnat (pridajte do repozitara Doxyfile-meno)

|               |         |
| --- | --- |
| *komunikacia* | jabber! |
| *framework*   | pyQT    |

## Rozdelenie uloh
Oblast   | Kto           | Datum do  | Stav
-------- | ------------- | --------- | ---
GUI      | Vasek, Michal | 21.3.2017 |
Knihovna | Simeon        | 24.3.2017 |
Testy    | Igor          | 21.3.2017 |

## Interface knihovny *mathlib.py*
| Nazov                            | Funkcia   | Poznamka        |
| -------------------------------- | --------- | --------------- |
| float add(float a, float b)      | a + b     |                 |
| float subtract(float a, float b) | a - b     |                 |
| float multiply(float a, float b) | a * b     |                 |
| float divide(float a, float b)   | a / b     |                 |
| float factorial(float a)         | a!        |                 |
| float power(float a, float b)    | a^b       | b je prirodzene |
| float root(float a, float b)     | a^(1/b)   | b je realne     |
| float logn(float a)              | log(e)(a) |                 |
