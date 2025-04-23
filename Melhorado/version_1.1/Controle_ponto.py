import datetime
import json
import os


class Dia(datetime.time):
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
            "Turno I Saida": self.turno_I_saida,
            "Turno II Entrada": self.turno_II_entrada,
            "Turno II Saida": self.turno_II_saida,
        }

def salvar_dia(obj_dia, arquivo, data):

    turnos = obj_dia.get_turnos()
    registro = {data: turnos}

    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            dados_existentes = json.load(f)
    else:
        dados_existentes = {}

    dados_existentes.update(registro)

    with open(arquivo, "w") as f:
        json.dump(dados_existentes, f, indent=4, default=str)


CAMINHO_ARQUIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ponto.json")
DATA_ATUAL = datetime.date.today().isoformat()
hoje = Dia()
hoje.set_turnos()
salvar_dia(hoje, CAMINHO_ARQUIVO, DATA_ATUAL)