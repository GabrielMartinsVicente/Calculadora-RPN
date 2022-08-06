# Calculadora-RPN
# Calculadora aritmética capaz de realizar operações de adição, subtração, divisão e multiplicação com entrada de dados na sintaxe RPN

#  (56+)      =  11
#  (2(53+)*)  =  16
#  ((3 4 +)) (4 (1 1 +)/)*) = 14
#  ((3.16 4 +)) (4.5 (1 1.98 +)/)*) = 10.81208053691275
#  (4 2 2 /) = 1  OBS: operações com mais de dois operandos não funciona para este código


''' Descrição de funcionamento:





'''


def calculo(operador,num1,num2):
    if(operador == '+'):
        return float(num1) + float(num2)
    if(operador == '-'):
        return float(num1) - float(num2)  
    if(operador == '/'):
        return float(num1) / float(num2)
    if(operador == '*'):
        return float(num1) * float(num2)
        
        
operacao = input("Digite a operação: ")
pilha = []    #Array criado add os números e os novos números dos calculos correspondentes
numero = []   #Array criado para add numeros que não fossem do tipo int

for i in range(len(operacao)):
    if(operacao[i] != '(' and operacao[i] != ')'):

        if(operacao[i] != ' '):
            
            if(operacao[i] != '+' and operacao[i] != '-' and operacao[i] != '/' and operacao[i] != '*'):
                numero.append(operacao[i])     

        if(operacao[i] == '+' or operacao[i] == '-' or operacao[i] == '/' or operacao[i] == '*'):
            
            num1 = pilha[len(pilha)-2]
            num2 = pilha[len(pilha)-1]
            del pilha[len(pilha)-2]
            del pilha[len(pilha)-1]
            
            pilha.append(calculo(operacao[i],num1,num2))

        if(operacao[i] == ' '):
            if(numero != []):
                n = "".join(numero)
                pilha.append(n)
                numero = []
            

print("\nResultado = " + str(pilha[0]))


       

    

    
