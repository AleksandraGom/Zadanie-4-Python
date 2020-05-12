import math

n = int(input("Podaj liczbę kul białych: "))
m = int(input("Podaj liczbę kul czarnych: "))
k = int(input("Podaj ile chcesz wylosować kul: "))

kombinacje = math.factorial(n+m)/(math.factorial(k)*math.factorial(n+m-k))


if (n-k) < 0:
    kombinajceBiałe = 0
elif (n-k) ==0:
    kombinacjeBiałe = 1
else:
    kombinacjeBiałe = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

if (m-k) < 0:
    kombinacjeCzarne = 0
elif (m-k) ==0:
    kombinacjeCzarne = 1
else:
    kombinacjeCzarne = math.factorial(m) / (math.factorial(k) * math.factorial(m - k))


prawdopodobieństwo = (kombinacjeBiałe + kombinacjeCzarne)/kombinacje
print(round(prawdopodobieństwo,2))








