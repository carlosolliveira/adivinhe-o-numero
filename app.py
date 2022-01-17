from random import randint
from time import sleep
from types import prepare_class
print("""                                             
    _    ____ _____     _____ _   _ _   _ _____ 
   / \  |  _ |_ _\ \   / |_ _| \ | | | | | ____|
  / _ \ | | | | | \ \ / / | ||  \| | |_| |  _|  
 / ___ \| |_| | |  \ V /  | || |\  |  _  | |___ 
/_/   \_|____|___|  \_/  |___|_| \_|_| |_|_____|
                                                
                                                
  ___      _   _ _   _ __  __ _____ ____   ___  
 / _ \    | \ | | | | |  \/  | ____|  _ \ / _ \ 
| | | |   |  \| | | | | |\/| |  _| | |_) | | | |
| |_| |   | |\  | |_| | |  | | |___|  _ <| |_| |
 \___/    |_| \_|\___/|_|  |_|_____|_| \_\\___/                                                
""")
print("Serteando um numero enter 1 e 100...")
sleep(2)
num = randint(1, 100)
while True:
    try:
        seunum = int(input("Chute: "))
        if seunum == num:
            print(f"\nParabéns você acertou!\n\nNúmero sorteado: {num}\nSeu chute: {seunum}")
            break
        elif seunum > num:
            print("DICA: Mais menor")

        else:
            print("DICA: Mais maior")
    except:
        print("Erro! Digite apenas numeros.")