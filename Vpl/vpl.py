import os

class Vpl:
    def __init__(self):
        self.period = None
        self.interest = None
    
    @staticmethod
    def input_treatment(value):
        return float(value.replace(".","").replace(",","."))
    
    def set_initial_values(self):
        self.period = int(input("Digite o período (n): "))
        value_input =  str(input("Digite a taxa de juros (i): "))
        self.interest = self.input_treatment(value_input) / 100


    def compound_interest_to_present_value(self, future_value):
        '''Calcula a taxa de juros composto para valor presente (S ===> P)
        Formula: P = S * (1 / (1 + i) ** n)'''
        print("Selecionado: Taxa de juros composto para valor presente")
        print("[>>> Valor recebido:] ", future_value)
        return round(future_value * (1 / (1 + self.interest) ** self.period),
                     2)
    
    def r_to_actual_value(self, payment):
        '''Calcula o fator de valor atual para uma Série Uniforme
        de Pagamentos e/ou Recebimentos (R ===> P)
        Formula: P = R((1 - (1 / (1+i) ** n)) / i) '''
        print("[>>> Valor recebido:] ", payment)
        return round(payment * ((1 - (1 / (1 + self.interest) ** self.period))
                     / self.interest), 2)
    
    def get_vpl(self):
        self.set_initial_values()
        initial_investment_input = str(input("Digite o" +
                                       " Investimento inicial: "))
        positive_r_input = str(input("Digite a receita (R+): "))
        negative_r_input = str(input("Digite o custo (R-): "))
        residual_value_input = str(input("Digite o valor residual: "))
        initial_investment = self.input_treatment(initial_investment_input)
        positive_r = self.input_treatment(positive_r_input)
        negative_r = self.input_treatment(negative_r_input)
        residual_value = self.input_treatment(residual_value_input)
        return round((self.r_to_actual_value((positive_r-negative_r)) +
                self.compound_interest_to_present_value(residual_value)) -
                initial_investment, 2)
    

def vpl():
    try:
        result = Vpl().get_vpl()
    except:
        print("\n[!!!>>> Error]\n")
    print("=============================")
    print(f"\nO resultado é: {result}\n")
    print("=============================")
