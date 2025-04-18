import datetime


class dia(datetime.time):
    def __init__(self):
        self.turno_I_entrada = None
        self.turno_I_saida = None
        self.turno_II_entrada = None
        self.turno_II_saida = None
    
    def set_turnos(self):
        
        def entrada_I():
            input_str = (input('Entrada primeiro turno (HH:MM): '))
            self.turno_I_entrada = datetime.datetime.strptime(input_str, "%H:%M").time()

        def saida_I():
            input_str = (input('Saida primeiro turno (HH:MM): '))
            self.turno_I_saida = datetime.datetime.strptime(input_str, "%H:%M").time()

        def entrada_II():
            input_str = (input('Entrada segundo turno (HH:MM): '))
            self.turno_II_entrada = datetime.datetime.strptime(input_str, "%H:%M").time()

        def saida_II():
            input_str = (input('Saida segundo turno (HH:MM): '))
            self.turno_II_saida = datetime.datetime.strptime(input_str, "%H:%M").time()

        entrada_I()
        saida_I()
        entrada_II()
        saida_II()

    def get_turnos(self):

        return {
            "Turno I Entrada": self.turno_I_entrada,
            "Turno I Saída": self.turno_I_saida,
            "Turno II Entrada": self.turno_II_entrada,
            "Turno II Saída": self.turno_II_saida,
        }
        


hoje = dia()

hoje.set_turnos()
for nome, horario in hoje.get_turnos().items():
    print(f"{nome}:  \t{horario.strftime('%H:%M')}")