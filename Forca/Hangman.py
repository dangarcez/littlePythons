palavra = "Abrobinha"
palavraDesvendada = palavra
letraCoringa = "*"
pLista = list(letraCoringa*len(palavra))
vidas = len(palavra)+2

print(f"Hangman Game!\nA palavra é:{''.join(pLista)}\n")
while True:
   num = -1
   letra = input("Informe uma letra: ").lower()
   flag = False

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
