# Tratamento de erros e excessões
# caso use o try = tentar se não de erro ele irá imprimir se não caira no except = excessão

# tentar
try:
    print('Paulo')

# caso o try de erro ele entra na exceção    
except:
    print('Algo deu errado')

# caso de erro em try= tentar
# caso de erro em except = excessão
# ai caira no else     
else:
    print('Deu tudo certo')




# usando o finally

# tentar
try:
    print(x)

# caso o try de erro ele entra na exceção    
except:
    print('Algo deu errado')

# caso de erro em try= tentar
# caso de erro em except = excessão
# ai caira no else     
#else:
    #print('Deu tudo certo')

# Dando certo ou dando errrado será executado essa linhabde comando
finally:
    print('Deu certo ou errado')
