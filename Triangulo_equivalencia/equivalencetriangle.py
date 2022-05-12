import os

class EquivalenceTriangle:
    def __init__(self):
        self.option = self.options()
        self.period = None
        self.interest = None
    
    @staticmethod
    def input_treatment(value):
        return float(value.replace(".","").replace(",","."))

    def options(self):
        print("Opções:\n"+\
            "1: (P ===> S)\n" +\
            "2: (S ===> P)\n" +\
            "3: (R ===> P)\n" +\
            "4: (P ===> R)\n" +\
            "5: (R ===> S)\n" +\
            "6: (S ==> R)\n"+\
            "7: Limpar a tela\n"+\
            "Qualquer outra coisa: Sair\n")
        option = str(input("Digite uma das opção: "))
        if option not in [str(i) for i in [1, 2, 3, 4, 5, 6, 7]]:
            return 0
        else:
            return option

    def switch(self):
        if not self.option:
            return -1
        elif self.option == "7":
            os.system('cls')
            return "Screen cleaned"
        else:
            self.set_initial_values()
            return getattr(self, 'case_' + self.option)()
    
    def set_initial_values(self):
        self.period = int(input("Digite o período (n): "))
        value_input =  str(input("Digite a taxa de juros (i): "))
        self.interest = self.input_treatment(value_input) /100
        
    def case_1(self):
        '''Calcula a taxa de juros composto para valor futuro (P ===> S)
        Formula: S=P * (1 + i) ** n'''
        print("Selecionado: Taxa de juros composto para valor futuro")
        value_input = str(input("Digite o valor presente(P): "))
        present_value = self.input_treatment(value_input)
        print("[>>> Valor recebido:] ", present_value)
        return round(present_value * (1 + self.interest) ** self.period, 2)
    
    def case_2(self):
        '''Calcula a taxa de juros composto para valor presente (S ===> P)
        Formula: P = S * (1 / (1 + i) ** n)'''
        print("Selecionado: Taxa de juros composto para valor presente")
        value_input = str(input("Digite o valor futuro (S): "))
        future_value = self.input_treatment(value_input)
        print("[>>> Valor recebido:] ", future_value)
        return round(future_value * (1 / (1 + self.interest) ** self.period),
                     2)
    
    def case_3(self):
        '''Calcula o fator de valor atual para uma Série Uniforme
        de Pagamentos e/ou Recebimentos (R ===> P)
        Formula: P = R((1 - (1 / (1+i) ** n)) / i) '''
        print("Selecionado: Valor atual para uma Série Uniforme" +
              " de Pagamentos e ou Recebimentos")
        value_input = str(input("Digite o pagamento (R): "))
        payment = self.input_treatment(value_input)
        print("[>>> Valor recebido:] ", payment)
        return round(payment * ((1 - (1 / (1 + self.interest) ** self.period))
                                / self.interest), 2)
    
    def case_4(self):
        '''Calcula o fator de recuperação de capital (P ===> R)
        Formula: R = P * (i / (1  -(1 / (1 + i) ** n)))'''
        print("Selecionado: Recuperação de capital")
        value_input = str(input("Digite o valor presente(P): "))
        present_value = self.input_treatment(value_input)
        print("[>>> Valor recebido:] ", present_value)
        return round(present_value * (self.interest /
                     (1 - (1 / (1 + self.interest) ** self.period))), 2)
    
    def case_5(self):
        '''Calcula o fator de valor futuro para uma série Uniforme de
        Pagamentos e/ou Recebimentos (R ===> S)
        Formula: S = R * (((1 + i) ** n) - 1 / i)'''
        print("Selecionado: Valor futuro para uma série Uniforme" +
              " de Pagamentos e/ou Recebimentos")
        value_input = str(input("Digite o pagamento (R): "))
        payment = self.input_treatment(value_input)
        print("[>>> Valor recebido:] ", payment)
        return round(payment * (((1 + self.interest) ** self.period - 1) /
                     self.interest), 2)
    
    def case_6(self):
        '''Calcula o fator de fundo de Amortização (S ==> R)
        Formula: S * (i/((1+i)**n)-1)'''
        print("Selecionado: Calcula o fator de fundo de Amortização")
        value_input = str(input("Digite o valor futuro (S): "))
        future_value = self.input_treatment(value_input)
        print("[>>> Valor recebido:] ", future_value)
        return round(future_value * (self.interest /
                     (((1 + self.interest) ** self.period) - 1)) ,2)

def equivalence_triangle():
    while True:
        try:
            result = EquivalenceTriangle().switch()
            if result == -1:
                break
            print("=============================")
            print(f"\nO resultado é: {result}\n")
            print("=============================")
        except:
            print("\n[!!!>>> Error]\n")
            continue
    
    


