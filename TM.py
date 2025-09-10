class ThreeTapeTM:
    def __init__(self, config, input_tape):
        self.init_state = config['init']
        self.accept_states = set(config['accept'])
        self.delta = config['delta']  # Diccionario mapeando tuplas a trasiciones
        
        # Inicializacion de cabezas y tiras
        self.tapes = [
            input_tape.copy(),        # Tira 1 (Input del usuario)
            ['_'] * max(100, len(input_tape)),  # Tira 2
            ['_'] * max(100, len(input_tape))   # Tira 3
        ]
        self.heads = [0, 0, 0]
        self.state = self.init_state

    def step(self):
        # Leer simbolo bajo la cabeza en cada tira
        symbols = tuple(self.tapes[i][self.heads[i]] if self.heads[i] < len(self.tapes[i]) else '_' for i in range(3))
        key = (self.state,) + symbols
        
        if key not in self.delta:
            return False  # Salir de no tener transiciones
        
        # Aplicar transiciones
        new_state, write_symbols, moves = self.delta[key]
        self.state = new_state
        for i in range(3):
            if self.heads[i] >= len(self.tapes[i]):
                self.tapes[i].append('_')
            self.tapes[i][self.heads[i]] = write_symbols[i]
            if moves[i] == '>':
                self.heads[i] += 1
            elif moves[i] == '<':
                self.heads[i] -= 1
                if self.heads[i] < 0:
                    self.tapes[i].insert(0, '_')
                    self.heads[i] = 0
        return True

    def run(self, max_steps=1000):
        steps = 0
        while self.state not in self.accept_states and steps < max_steps:
            if not self.step():
                break
            steps += 1
        return self.state in self.accept_states, self.tapes


# Ejemplo de configuracion
config_example = {
    'init': 'q0',
    'accept': ['q1'],
    'delta': {
        #(estado_actual, simbolo_leido_cinta_1,...,simbolo_leido_cinta_3):(estado_nuevo, simbolo_leido_cinta_1,...,simbolo_leido_cinta_3, movimiento_cinta_1,...,movimiento_cinta_3)
        ('q0','0','_','_'):('q0', ['0','_','_'], ['>','-','-']),
        ('q0','1','_','_'): ('q0', ['1','_','_'], ['>','-','-']),
        ('q0','#','_','_'): ('q1', ['_','_','_'], ['>','-','-']),
    }
}

# Corre la maquina de turing
tape_1 = list('1000#10')
tm = ThreeTapeTM(config_example, tape_1)
accepted, final_tapes = tm.run(max_steps=1000)

# Imprimir la cinta que contenga los resultados
tape1_result = ''.join(final_tapes[0]).rstrip('_')

print(''.join(tape_1) + f" = {tape1_result}")

