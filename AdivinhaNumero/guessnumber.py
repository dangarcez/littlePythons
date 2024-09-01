import random
import math
print("Informe o range possivel de números:")
min = int(input("Mínimo:"))
max = int(input("Máximo:"))
guess = min-1
numSorteado = random.randint(min,max)
count = 1
totalTentativas = math.ceil(math.log(max-min+1.01,2))-1
print(f"\nValendo!\nAdivinhe um numero entre {min} e {max},vocÊ tem {totalTentativas} tentativas!")

while(guess!=numSorteado and count<=totalTentativas):
   guess = int(input(f"{count}ª Tentativa: "))
   count +=1
   if(guess < min or guess > max):
      break
   if(guess <numSorteado):
      print("Tente denovo, você chutou muito baixo!")
   if(guess >numSorteado):
      print("Tente denovo, você chutou muito alto!")
if(guess ==numSorteado):
   print(f"Parabéns, você acertou o numero({numSorteado}) na sua {count-1}ª tentativa!")
else:
   print(f"O número era {numSorteado} :(. Better luck next time!")
