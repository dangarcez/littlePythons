import random

matriz = [[0]*4 for i in range(0,4)]
print(matriz)

def showGame(m):
   for linha in m:
      print(linha)

def fillcell(m):
   randomCollum = random.randint(0,3)
   randomRow = random.randint(0,3)
   while(m[randomRow][randomCollum]!=0):
      randomCollum = random.randint(0,3)
      randomRow = random.randint(0,3)
   m[randomRow][randomCollum] = 2

def goright(m):
   wongame = False
   countFusions = 0
   for row in range(0,4):
      for column in range(2,-1,-1):
         for column2 in range(column+1,4):
            if(m[row][column2]==0):
               m[row][column2]=m[row][column2-1]
               m[row][column2-1] = 0 
            elif m[row][column2]==m[row][column2-1]:
               m[row][column2] *=2
               m[row][column2-1] = 0 
               if(m[row][column2]>=2048):
                  wongame = True
               countFusions+=1
            else:
               break
   return (countFusions,wongame)

def goleft(m):
   countFusions = 0
   wongame = False
   for row in range(0,4):
      for column in range(1,4):
         for column2 in range(column-1,-1,-1):
            if(m[row][column2]==0):
               m[row][column2]=m[row][column2+1]
               m[row][column2+1] = 0 
            elif m[row][column2]==m[row][column2+1]:
               m[row][column2] *=2
               m[row][column2+1] = 0 
               if(m[row][column2]>=2048):
                  wongame = True
               countFusions+=1
            else:
               break
   return (countFusions,wongame)

def godown(m):
   countFusions = 0
   wongame = False
   for column in range(0,4):
      for row in range(2,-1,-1):
         for row2 in range(row+1,4):
            if(m[row2][column]==0):
               m[row2][column]=m[row2-1][column]
               m[row2-1][column] = 0 
            elif m[row2][column]==m[row2-1][column]:
               m[row2][column] *=2
               m[row2-1][column] = 0 
               if(m[row2][column]>=2048):
                  wongame = True
               countFusions+=1
            else:
               break
   return (countFusions,wongame)
   
def goup(m):
   countFusions = 0
   wongame = False
   for column in range(0,4):
      for row in range(1,4):
         for row2 in range(row-1,-1,-1):
            if(m[row2][column]==0):
               m[row2][column]=m[row2+1][column]
               m[row2+1][column] = 0 
            elif m[row2][column]==m[row2+1][column]:
               m[row2][column] *=2
               m[row2+1][column] = 0 
               if(m[row2][column]>=2048):
                  wongame = True
               countFusions+=1
            else:
               break
   return (countFusions,wongame)

fillcell(matriz)
fillcell(matriz)

print("Os comandos são o seguintes:")
print("w: Move up")
print("s: Move down")
print("a: Move left")
print("d: Move right")
showGame(matriz)

espacoRestante = 14

while True:
   wongame = False
   change = 0
   comando = input("\nDigite o comando:").lower()
   match comando:
      case 'w':change,wongame =goup(matriz)
      case 's':change,wongame =godown(matriz)
      case 'a':change,wongame =goleft(matriz)
      case 'd':change,wongame =goright(matriz)
      case _:break
   
   espacoRestante +=change
   fillcell(matriz)
   espacoRestante-=1
   showGame(matriz)

   if(espacoRestante==0):
      print("Game Over, you lost!")
      break
   
   if(wongame):
      print("Congratulation, you won!")
      break
