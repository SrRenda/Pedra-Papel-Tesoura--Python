# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 17:25:13 2023

@author: matheus.renda
"""
import random 
import time

options = ["Pedra","Papel","Tesoura"]
condições = ["Empate... :/","Perdeu! :(","Ganhou! :D", "Ops algo deu errado, insira apenas nº"]
log = [[],[],[]]
pontosPlayer = 0
pontosComputador = 0
start = True

def fala():
    print("\nTodos prontos?")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2..")
    time.sleep(1)
    print("1.")

def player():
    print('Escolha uma opção: \n "0" - Pedra \n "1" - Papel \n "2" - Tesoura')
    escolha = input("-> ")
    return escolha 

def validacao(opcao1,opcao2):
    a = opcao1
    b = opcao2
    if (a == "Pedra" and b == "Pedra"):
        out = 0
    elif (a == "Pedra" and b == "Papel"):
        out = 1
    elif (a == "Pedra" and b == "Tesoura"):
        out = 2
    elif (a == "Papel" and b == "Pedra"):
        out = 2
    elif (a == "Papel" and b == "Papel"):
        out = 0
    elif (a == "Papel" and b == "Tesoura"):
        out = 1
    elif (a == "Tesoura" and b == "Pedra"):
        out = 1
    elif (a == "Tesoura" and b == "Papel"):
        out = 2
    elif (a == "Tesoura" and b == "Tesoura"):
        out = 0
    else:
        out = 3
    return out 

while start == True:
    
    jogada = player()
    computador = random.choice(options)
    
    print(options[int(jogada)])
    time.sleep(1)
    
    fala()
    time.sleep(2)
    
    resultado = validacao(options[int(jogada)],computador)
    print("Ele -> " + computador + "\nVocê -> " + options[int(jogada)]+"\n\n")
    
    time.sleep(1)
    print(condições[resultado]+"\n")       
            
    log[0].append(options[int(jogada)])
    log[1].append(computador)
    log[2].append(condições[resultado])
    
    if resultado == 1:
        pontosComputador +=1
    elif resultado == 2:
        pontosPlayer += 1
    else:
        None
    
    time.sleep(2)
    print("Ele -> "+str(pontosComputador)+"\nVocê -> "+str(pontosPlayer)+"\n")
    
    if pontosComputador >= 3:
        start = False
        print("...Derrota...")
        time.sleep(5)
    elif pontosPlayer >= 3:
        start = False
        print("!!!Vitória!!!")
        time.sleep(5)
    else:
        None
        
        time.sleep(2)
        print("||>...Rebobinando...||>")
        print("-"*20)
        time.sleep(2)
