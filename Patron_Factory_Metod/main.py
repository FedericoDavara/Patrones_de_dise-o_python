from creadores_concretos import Creador_Concreto_1, Creador_Concreto_2

def client_code(creador):
    print(creador.operation())

if __name__ == "__main__":
    primer_creador = Creador_Concreto_1()
    segundo_creador= Creador_Concreto_2()

    client_code(primer_creador)
    client_code(segundo_creador)