# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 14:38:21 2021

@author: jpm20
"""

"21 Fósforos"
import random
def xii():
    a=input("Bem vindo! Quer jogar contra um jogador(j) ou contra o computador(c):")
    if a =="c" or a=="computador" or a=="Computador" or a=="C":
        n=21
        ordem=input("Pretende jogar primeiro? Sim(s) ou Não(n):")
        if ordem=="Sim" or ordem=="s" or ordem=="sim" or ordem=="S":
            while n >1:
                jogada=int(input("Quantos fósforos quer tirar? 1, 2, 3, 4?"))
                if jogada>=1 and jogada<=4:
                    n=n-jogada
                    print("Restam", n, "fósforos!")
                    if jogada==1:
                        n=n-4
                        print("A jogada do computador é retirar 4 fósforos.")
                        print("Restam", n, "fósforos!")
                    if jogada==2:
                        n=n-3
                        print("A jogada do computador é retirar 3 fósforos.")
                        print("Restam", n, "fósforos!")
                    if jogada==3:
                        n=n-2
                        print("A jogada do computador é retirar 2 fósforos.")
                        print("Restam", n, "fósforos!")    
                    if jogada==4:
                        n=n-1
                        print("A jogada do computador é retirar 1 fósforos.")
                        print("Restam", n, "fósforos!")
                if jogada<1 or jogada>4:
                    print("Erro!")
                
            print("Fim de jogo. Jogador perde! :(")  
        
        if ordem=="Não" or ordem=="não" or ordem=="n" or ordem=="N":
            jogada_cpu=random.randint(1,4)
            n=n-jogada_cpu
            print("A jogada do computador é retirar", jogada_cpu, "fósforos.")
            print("Restam", n, "fósforos!")
            while n>1:
                jogada=int(input("Quantos fósforos quer tirar? 1, 2, 3, 4?"))
                if jogada>=1 and jogada<=4:    
                    n=n-jogada
                    print("Restam", n, "fósforos!")   
                    if n==1:
                        print("Jogador ganha!Parabéns!")
                    if n==2:
                        jogada_cpu=1
                        n=n-jogada_cpu
                        print("A jogada do computador é retirar", jogada_cpu, "fósforos.")
                        print("Restam", n, "fósforos!")
                        print("O Jogador perdeu!")
                    if n==3:
                        jogada_cpu=2
                        n=n-jogada_cpu
                        print("A jogada do computador é retirar", jogada_cpu, "fósforos.")
                        print("Restam", n, "fósforos!")
                        print("O Jogador perdeu!")
                    if n==4:
                        jogada_cpu=3
                        n=n-jogada_cpu
                        print("A jogada do computador é retirar", jogada_cpu, "fósforos.")
                        print("Restam", n, "fósforos!")
                        print("O Jogador perdeu!")
                    if n==5:
                        jogada_cpu=4
                        n=n-jogada_cpu
                        print("A jogada do computador é retirar", jogada_cpu, "fósforos.")
                        print("Restam", n, "fósforos!")
                        print("O Jogador perdeu!")
                    if n==6:
                        jogada_cpu=random.randint(1,4)
                        n=n-jogada_cpu
                        print("A jogada do computador é retirar", jogada_cpu, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==7:
                        jogada_cpu=1
                        n=n-jogada_cpu
                        print("A jogada do computador é retirar", jogada_cpu, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==8:
                        jogada_cpu=2
                        n=n-jogada_cpu
                        print("A jogada do computador é retirar", jogada_cpu, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==9:
                        jogada_cpu=3
                        n=n-jogada_cpu
                        print("A jogada do computador é retirar", jogada_cpu, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==10:
                        jogada_cpu=4
                        n=n-jogada_cpu
                        print("A jogada do computador é retirar", jogada_cpu, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==11:
                        jogada_cpu=random.randint(1,4)
                        n=n-jogada_cpu
                        print("A jogada do computador é retirar", jogada_cpu, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==12:
                        jogada_cpu=1
                        n=n-jogada_cpu
                        print("A jogada do computador é retirar", jogada_cpu, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==13:
                        jogada_cpu=2
                        n=n-jogada_cpu
                        print("A jogada do computador é retirar", jogada_cpu, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==14:
                        jogada_cpu=3
                        n=n-jogada_cpu
                        print("A jogada do computador é retirar", jogada_cpu, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==15:
                        jogada_cpu=4
                        n=n-jogada_cpu
                        print("A jogada do computador é retirar", jogada_cpu, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==16:
                        jogada_cpu=random.randint(1,4)
                        n=n-jogada_cpu
                        print("A jogada do computador é retirar", jogada_cpu, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==17:
                        jogada_cpu=1
                        n=n-jogada_cpu
                        print("A jogada do computador é retirar", jogada_cpu, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==18:
                        jogada_cpu=2
                        n=n-jogada_cpu
                        print("A jogada do computador é retirar", jogada_cpu, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==19:
                        jogada_cpu=3
                        n=n-jogada_cpu
                        print("A jogada do computador é retirar", jogada_cpu, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==20:
                        jogada_cpu=4
                        n=n-jogada_cpu
                        print("A jogada do computador é retirar", jogada_cpu, "fósforos.")
                        print("Restam", n, "fósforos!")
                if jogada<1 or jogada>4:
                    print("Erro!")
    
    if a =="j" or a=="jogador" or a=="J":
       n=21
       contador=0
       if n>1:
           while n>1:
               jogada1=int(input("Quantos fósforos quer o jogador 1 tirar? 1, 2, 3, 4?"))
               if jogada1>=1 and jogada1<=4:
                   n=n-jogada1
                   contador=contador+1
                   if n>1:
                       print("Restam", n, "fósforos!")
                       jogada2=int(input("Quantos fósforos quer o jogador 2 tirar? 1, 2, 3, 4?"))
                       if jogada2>=1 and jogada2<=4:
                           contador=contador+1
                           n=n-jogada2
                           print("Restam", n, "fósforos!")
                       if jogada2<1 or jogada2>4:
                           print("Erro!")
                   if n<=1:
                       if contador%2==0:
                           print("Jogador 2 ganha!")
                       if contador%2==1:
                           print("Jogador 1 ganha!")
               if jogada1<1 or jogada1>4:
                    print("Erro!")
xii()
