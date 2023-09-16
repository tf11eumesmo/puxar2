#!/usr/bin/python2
import os
import time
import json
import requests

def main:
    print('Olá me apresento como Wesley, por favor não vai achar que Eu estou fazendo crimes ilicitos ')
    print('ok ? então, Eu tenho 15 anos de idade, por favor, não me aponte como criminoso, sou do bem ')
    print(' OK. ')
    print()

    cep = input("Digite o CEP da Vítima para HACKEAR: ")
    if len(cep) != 8:
            print("ACESSO NEGADO")
            time.sleep(3)
            exit()
    
    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    address_data = request.json()

    if 'erro' not in address_data:
            print('===> CEP HACKEADO <===')

            print('CEP: {}'.format(address_data['cep']))
            print('Logradouro: {}'.format(address_data['logradouro']))
            print('Complemento: {}'.format(address_data['complemento']))
            print('DDD: {}'.format(address_data['ddd']))
            print('Gia: {}'.format(address_data['gia']))
            print('IBGE: {}'.format(address_data['ibge']))
            print('Bairro: {}'.format(address_data['bairro']))
            print('Cidade: {}'.format(address_data['cidade]))
            print('Estado: {}'.format(address_data['uf']))
            print('Siafi: {}'.format(address_data['siafi']))
                             
    else:
            print('{} ACESSO NEGADO.'.format(cep))

    print('-----------------------------------')
    option = int(input(' Voltar Novamente ?\n1. Sim\n2. Sair\n'))
    if option == 1:
            main()
    else:
            print('Saindo.....')

if __name == '__main__':
        main()
                                      
                                      
                                      

            
              
              
              
              
            


    

















