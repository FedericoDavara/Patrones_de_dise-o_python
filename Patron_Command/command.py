class Command:
    def execute(self):
        pass

class Comando_iniciar_servidor(Command):
    def __init__(self, servidor):
        self.servidor = servidor

    def execute(self):
        self.servidor.start()

class  Comando_detener_servidor(Command):
    def __init__(self, servidor):
        self.servidor = servidor

    def execute(self):
        self.servidor.stop()

class Comando_reiniciar_servidor(Command):
    def __init__(self, servidor):
        self.servidor = servidor

    def execute(self):
        self.servidor.restart()




