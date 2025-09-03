"""
---- LEDS ----
1 = 2
2 = 5
3 = 5
4 = 4
5 = 5
6 = 6
7 = 3
8 = 7
9 = 6
0 = 6 
"""

nleds = input("Digite a quantidade o número: ")
listaleds = {
    '1': '2',
    '2': '5',
    '3': '5',
    '4': '4', 
    '5': '5',
    '6': '6',
    '7': '3',
    '8': '7',
    '9': '6',
    '0': '6',

}
total = 0 
for i in nleds:
    total = int(listaleds[i]) + total

print(f'O total é {total}!')