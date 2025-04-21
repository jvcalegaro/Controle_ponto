import datetime
import json


class dia(datetime.time):
    def __init__(self):
        self.turno_I_entrada = None
        self.turno_I_saida = None
        self.turno_II_entrada = None
        self.turno_II_saida = None
    
    def set_turnos(self):

        def ler_horarios(mensagem):
            input_str = input(mensagem)
            return datetime.datetime.strptime(input_str, "%H:%M").time()
        
        self.turno_I_entrada = ler_horarios('Entrada primeiro turno (HH:MM): ')
        self.turno_I_saida = ler_horarios('Saida primeiro turno (HH:MM): ')
        self.turno_II_entrada = ler_horarios('Entrada segundo turno (HH:MM): ')
        self.turno_II_saida = ler_horarios('Saida segundo turno (HH:MM): ')

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

turnos = hoje.get_turnos()

with open("ponto.json", "w") as f:
    json.dump(turnos, f, indent=4, default=str)

with open("ponto.json", "r") as f:
    dados = json.load(f)
    print(dados)