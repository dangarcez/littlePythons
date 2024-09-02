import random
with open("personagens.txt",'r') as file:
   texto = file.read()
   table = texto.maketrans("\n ",",,","1234567890.");
   texto = texto.translate(table)
   palavras = texto.split(',')

palavra = random.choice(palavras)
palavraDesvendada = palavra
letraCoringa = "_"
pLista = list(letraCoringa*len(palavra))
vidas = len(palavra)

print(f"Hangman Game! Adivinhe qual é o campeão de League of Legends\nA palavra é:{''.join(pLista)}\n")
while True:
   num = -1
   letra = input("Informe uma letra: ").lower()
   flag = False

   if(len(letra)>1):
      print("Apenas uma letra permitida!\n")
      continue
   elif len(letra)<1:
      print("Você precisa informar uma letra\n")
      continue

   while((num := palavra.lower().find(letra,num+1))!=-1):
      flag = True
      pLista[num] = letra   
   

   if(not flag):
      vidas -=1
      if(vidas==0):
         print(f"\nPerdeu! Seu personagem foi enforcado!\nA palavra era '{palavra}'")
         break
      print(f"Erro! Você tem {vidas} vidas restantes\n")
   else:
      print("Acertou!\n")
   print(''.join(pLista).capitalize())

   if(pLista.count(letraCoringa)==0):
      print("\nParabéns! Você venceu o desafio")
      break
