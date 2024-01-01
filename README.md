# Tolerancje i pasowania wg. PN-EN ISO 286-1:2011P

## użycie
Import pakietu
```
from odchylki import isotol
```
### funkcja isotol
```
print(f'29h7 {isotol("29h7")}')  # retuns 29h7 (-21, 0, 28.979, 29.0)
```
```
print(f'29h7 {isotol("29h7",Dictionary=True)}')  # returns 29h7 {'ei': -21, 'es': 0, 'A': 28.979, 'B': 29.0}
```
```
print(f'29H7 {isotol("29H7",Dictionary=True)}')  #returns 29H7 {'EI': 0, 'ES': 21, 'A': 29.0, 'B': 29.021}
```
```
print(f'29H7/h8 {isotol("29H7/h8",Dictionary=True )}') #return 29H7/h8 {'T': 54, 'L_min': 0, 'L_max': 54} 
```
