#Questão 1

texto = """Python é uma linguagem de programação de alto nível, [5] interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. 
Foi lançada por Guido van Rossum em 1991. 
[1] Atualmente, possui um modelo de desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation. 
Apesar de várias partes da linguagem possuírem padrões e especificações formais, a linguagem, como um todo, não é formalmente especificada. 
O padrão na pratica é a implementação CPython. 
A linguagem foi projetada com a filosofia de enfatizar a importância do esforço do programador sobre o esforço computacional. Prioriza a legibilidade do código sobre a velocidade ou expressividade. 
Combina uma sintaxe concisa e clara com os recursos poderosos de sua biblioteca padrão e por módulos e frameworks desenvolvidos por terceiros."""


aux = texto.replace("P", "F",3)
print('Agora o texto está assim: \n' + aux)

#Dúvida 1: a contagem começa do zero como é no caso da contagem de letras em uma string ou começa do 1?
#Dúvida 2: por que quando eu concateno o primeiro Fython fica com um espaço que não sai nem com o método strip e, por outro lado, quando eu somo
# as strings o espaço do primeiro Fython some? 
