# FizzBuzz : Si le nombre est 0 -> Une erreur est levée.
# Si le nombre est négatif -> Une erreur est levée.
# Si le nombre est un multiple de 3 -> Fizz.
# Si le nombre est un multiple de 5 -> Buzz.
# Si le nombre est un multiple de 3 et de 5 -> FizzBuzz.
# Si aucun des cas précédents, répète le nombre de Alice.


print("Taper un chiffre pour jouer au FizzBuzz")
print("Taper '404' pour sortir du programme")
x=int(input())
while x != 404:
    if (x<=0):
        print("erreur")
        x=int(input())
    elif (x%3) == 0 and (x%5 != 0):
        print("Fizz")
        x=int(input())
    elif x%5 == 0 and (x%3 != 0):
        print("Buzz")
        x=int(input())
    elif (x%3 == 0) and (x%5 == 0):
        print("FizzBuzz")
        x=int(input())
    else: 
        print(x)
        x=int(input())
print("Sortie du programme")
    
      