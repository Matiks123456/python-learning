"""
Zadanie 1

1. Zadeklaruj 5 roznych zmiennych uzywajac typow danych ktore poznales
2. Wykonaj 3 operacje arytmetyczne z uzyciem zmiennych z pkt1 (wypisz wynik na ekran)
3. Zademonstruj instrukcje warunkowa z uzyciem zmiennych z pkt1
"""

# 1!!!

liczba = 1
liczba_zmiennoprzecinkowa = 1.0
srting = maslo
bool = True
(po sprawdzeniu, bo zapomniałem)
nic = None
# 2!!!

print(liczba + liczba_zmiennoprzecinkowa)
# 2.0
print(string + " " + string)
# maslo maslo
print(liczba + nic)
 # 1 albo error?

# 3!!!
bool = True
liczba = 1
if(bool):
  print("Posiadamy zupę grzybową")
  if liczba >= 20 and <= 28:
    print("Zupa grzybowa w idealnej temperaturze :)")
  elif liczba == 0:
    print("Zupa grzybowa zamarzła!")
  elif liczba < 0:
    print("¯\_(ツ)_/¯")
  elif liczba > 0 and < 20:
    print("Zupa grzybowa jest zbyt zimna!!!")
  else:
    print("Zupa grzybowa jest zbyt gorąca!")
  
