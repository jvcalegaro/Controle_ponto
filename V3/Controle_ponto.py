import datetime


class dia(datetime):
    def __init__(self):
        self.turno_I_entrada = None
        self.turno_I_saida = None
        self.turno_II_entrada = None
        self.turno_II_saida = None
    
    def set_turnos(self):
        
        def entrada_I():
            self.turno_I_entrada(input('Entrada primeiro turno!\nInsira o horario: '))

        def saida_I():
            self.turno_I_saida(input('Saida primeiro turno!\nInsira o horario: '))

        def entrada_II():
            self.turno_II_entrada(input('Entrada segundo turno!\nInsira o horario: '))

        def saida_II():
            self.turno_II_saida(input('Saida segundo turno!\nInsira o horario: '))

        entrada_I()
        saida_I()
        entrada_II()
        saida_II()

    def get_turnos(self):

        def entrada_I():
            return self.turno_I_entrada

        def saida_I():
            return self.turno_I_saida
        
        def entrada_II():
            return self.turno_II_entrada

        def saida_II():
            return self.turno_II_saida
        
        entrada_I()
        saida_I()
        entrada_II()
        saida_II()


hoje = dia()

hoje.set_turnos()
print(hoje.get_turnos())