import datetime


class dia(datetime):
    def __init__(self):
        self.turno_I_entrada = None
        self.turno_I_saida = None
        self.turno_II_entrada = None
        self.turno_II_saida = None
    
    def set_turnos(self):
        
        def entrada_I():
            input_str = (input('Entrada primeiro turno!\nInsira o horario (HH:MM): '))
            self.turno_I_entrada = datetime.datetime.strptime(input_str, "%H:%M").time()

        def saida_I():
            input_str = (input('Saida primeiro turno!\nInsira o horario (HH:MM): '))
            self.turno_I_saida = datetime.datetime.strptime(input_str, "%H:%M").time()

        def entrada_II():
            input_str = (input('Entrada segundo turno!\nInsira o horario: '))
            self.turno_II_entrada = datetime.datetime.strptime(input_str, "%h:%M").time()

        def saida_II():
            input_str = (input('Saida segundo turno!\nInsira o horario: '))
            self.turno_II_saida = datetime.datetime.strptime(input_str, "%H:%M").time()

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