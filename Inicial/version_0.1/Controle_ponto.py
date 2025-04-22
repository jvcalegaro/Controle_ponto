import datetime


class dia(datetime.date):
    def __init__(self):
        self.turno_I_entrada: datetime.time
        self.turno_I_saida: datetime.time
        self.turno_II_entrada: datetime.time
        self.turno_II_saida: datetime.time
    
    def set_turno(self):
        
        def s_entrada_I(self):
            self.turno_I_entrada(input('Entrada primeiro turno!\nInsira o horario: '))

        def s_saida_I(self):
            self.turno_I_saida(input('Saida primeiro turno!\nInsira o horario: '))

        def s_entrada_II(self):
            self.turno_II_entrada(input('Entrada segundo turno!\nInsira o horario: '))

        def s_saida_II(self):
            self.turno_II_saida(input('Saida segundo turno!\nInsira o horario: '))

    def get_turno(self):

        def g_entrada_I(self):
            return self.turno_I_entrada

        def g_saida_I(self):
            return self.turno_I_saida
        
        def g_entrada_II(self):
            return self.turno_II_entrada

        def g_saida_II(self):
            return self.turno_II_saida


hoje = dia
hoje.turno_I_entrada = "07,30,00"
hoje.turno_I_saida = "11,33,00"
hoje.turno_II_entrada = "13:30:00"
hoje.turno_I_saida = "17:35:00"

print(hoje.get_turno.g_entrada_I)
print(hoje.get_turno.g_saida_I)
print(hoje.get_turno.g_entrada_II)
print(hoje.get_turno.g_saida_II)