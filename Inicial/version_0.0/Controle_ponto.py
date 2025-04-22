import datetime


class segundo:
    def __init__(self):
        self.segundos: datetime.time.second
    
    def set_segundo(self, s):
        self.segundos = s
    
    def get_segundo(self):
        return self.segundos
    pass

class minuto(segundo):
    def __init__(self):
        self.minutos: int
        self.max = 59
        pass
    def set_minuto(self, m):
        self.minutos = m

    def get_minuto(self):
        return self.minutos
    pass

class hora(minuto):
    def __init__(self):
        self.horas: int
        self.max = 23
        pass
    def set_hora(self, h):
        self.horas = h

    def get_hora(self):
        return self.horas
    pass

class dia:
    def __init__(self):
        self.turno_I_entrada: hora
        self.turno_I_saida: hora
        self.turno_II_entrada: hora
        self.turno_II_saida: hora
    
    def set_turno(self):
        
        def s_entrada_I(self):
            self.turno_I_entrada.set_hora(input('Entrada primeiro turno!\nInsira a hora: '))
            self.turno_I_entrada.horas.set_minuto(input('Insira os minutos: '))
            self.turno_I_entrada.horas.minutos.set_segundo(input('Insira os segundos'))

        def s_saida_I(self):
            self.turno_I_saida.set_hora(input('Primeiro turno!\nInsira a hora de saida: '))
            self.turno_I_saida.horas.set_minuto(input('Insira os minutos: '))
            self.turno_I_saida.horas.minutos.set_segundo(input('Insira os segundos'))

        def s_entrada_II(self):
            self.turno_II_entrada.set_hora(input('Segundo turno!\nInsira a hora de entrada: '))
            self.turno_II_entrada.horas.set_minuto(input('Insira os minutos: '))
            self.turno_II_entrada.horas.minutos.set_segundo(input('Insira os segundos'))

        def s_saida_II(self):
            self.turno_II_saida.set_hora(input('Segundo turno!\nInsira a hora de saida: '))
            self.turno_II_saida.horas.set_minuto(input('Insira os minutos: '))
            self.turno_II_saida.horas.minutos.set_segundo(input('Insira os segundos'))

    def get_turno(self):

        def g_entrada_I(self):
            return self.turno_I_entrada.get_hora
            return self.turno_I_entrada.get_minuto
            return self.turno_I_entrada.get_segundo

        def g_saida_I(self):
            return self.turno_I_saida.get_hora
            return self.turno_I_saida.get_minuto
            return self.turno_I_saida.get_segundo
        
        def g_entrada_II(self):
            return self.turno_II_entrada.get_hora
            return self.turno_II_entrada.get_minuto
            return self.turno_II_entrada.get_segundo

        def g_saida_II(self):
            return self.turno_II_saida.get_hora
            return self.turno_II_saida.get_minuto
            return self.turno_II_saida.get_segundo

class semana:
    def __init__(self):
        self.segunda: dia
        self.terca: dia
        self.quarta: dia
        self.quinta: dia
        self.sexta: dia
        self.sabado: dia
    pass

class mes:
    def __init__(self):
        self.meses: semana
    pass

hoje: dia
hoje.set_turno.s_entrada_I
hoje.set_turno.s_saida_I
hoje.set_turno.s_entrada_II
hoje.set_turno.s_saida_II

print(hoje.get_turno.g_entrada_I)
print(hoje.get_turno.g_saida_I)
print(hoje.get_turno.g_entrada_II)
print(hoje.get_turno.g_saida_II)