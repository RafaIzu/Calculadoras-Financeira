class InterestConverter:
    def __init__(self):
        self.option = self.options()
        self.interest = None
        self.period = None

    def options(self):
        print("Opção    Calculo:\n"+\
            "1:       Juros Simples: Compor (ex: dia para ano)\n" +\
            "2:       Juros Simples: Decompor (ex: ano para dia)\n" +\
            "3:       Juros Composto: Compor (ex: dia para ano)\n" +\
            "4:       Juros Composto: Decompor (ex: ano para dia)\n" +\
            "Qualquer outra coisa: Sair\n")
        option = str(input("Digite uma das opção: "))
        if option not in [str(i) for i in [1, 2, 3, 4]]:
            return 0
        else:
            return option

    def switch(self):
        if not self.option:
            return -1
        else:
            self.set_initial_values()
            return getattr(self, 'case_' + self.option)()

    def set_initial_values(self):
        self.period = int(input("Digite o período (n): "))
        self.interest = float(input("Digite a taxa de juros (i): "))

    def case_1(self):
        '''Juros simples Menor para Maior
        Exemplo: Dia para Ano'''
        return self.interest * self.period
    
    def case_2(self):
        '''Juros simples Maior para Menor
        Exemplo: Ano para dia'''
        return self.interest / self.period
    
    def case_3(self):
        '''Juros simples Menor para Maior
        Exemplo: Dia para Ano'''
        return  round(((1 + self.interest / 100) ** self.period - 1) * 100, 2)
    
    def case_4(self):
        '''Juros Composto Maior para Menor
        Exemplo: Ano para dia'''
        return round(((1 + (self.interest / 100)) ** (1 / self.period) - 1) * 100, 2)

def interest_converter():
        while True:
            try:
                result = InterestConverter().switch()
                if result == -1:
                    break
                print("=============================")
                print(f"\nO resultado é: {result} %\n")
                print("=============================")
            except:
                print("\n[!!!>>> Error]\n")
                continue
           