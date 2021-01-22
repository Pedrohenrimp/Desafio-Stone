#definir quantidade de emails e quantidade de itens da lista.
listaDeCompras = []
listaDeEmails = []
QUANTIDADE_DE_ITENS = 10
QUANTIDADE_DE_EMAILS = 4

#criar um objeto do tipo item com atributos nome, preço unitário e quantidade.
class Item:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.precoUnitario = preco
        self.quantidade = quantidade

#criar os itens e adicioná-los à lista de compras.
for i in range(0, QUANTIDADE_DE_ITENS):
    item = Item('item ' + str(i + 1), 100 + i, i + 1)
    listaDeCompras.append(item)
    

#criar os emails os quais serão utilizados para receber a conta dividida.
for i in range(0, QUANTIDADE_DE_EMAILS):
    email = 'email_' + str(i + 1) + '@email.com'
    listaDeEmails.append(email)




#criar a função responsável por dividir a conta da lista de compras.
def dividir_conta(lista, emails):
    listaCompras = lista
    listaEmails = emails
    dicionarioContaDividida = {}
    valorTotal = 0

    #calcular o valor total da conta
    for i in range(0, len(listaCompras)):
        valorTotal += listaCompras[i].precoUnitario * listaCompras[i].quantidade

    #calcular o valor restante da divisão exata e o valor da divisão exata.
    if listaEmails != []:
        valorRestante = valorTotal % len(listaEmails)
        valorParcial = (valorTotal - valorRestante) / len(listaEmails)

    #adicionar os valores da conta dividida e seus respectivos emails ao dicionário
    for i in range(0, len(listaEmails)):
        #verificar se existe resto na divisão da conta, para distribuir entre os emails
        if valorRestante > 0:
            dicionarioContaDividida[listaEmails[i]] = int(valorParcial + 1)
            valorRestante -= 1
        else:
            dicionarioContaDividida[listaEmails[i]] = int(valorParcial)

    return dicionarioContaDividida

print(dividir_conta(listaDeCompras, listaDeEmails))


'''Eu decidi criar os dados (lista de compras e lista de emails) diretamente no código, para deixá-los
manipuláveis dinâmicamente para facilitar a testagem dos casos.
 Para fazer os testes, basta manipular os valores QUANTIDADE_DE_ITENS e QUANTIDADE_DE_EMAILS,
assim como os laços for responsáveis pela crianção dos mesmos, como forma a simular um valor esperado e
verificar no final se os valores estão de acordo com o esperado.'''
