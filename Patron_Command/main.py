from command import Comando_iniciar_servidor, Comando_detener_servidor, Comando_reiniciar_servidor
from super_servidor import super_servidor
from control_a_distancia import Control_a_distancia

servidor = super_servidor()
Comando_iniciar = Comando_iniciar_servidor(servidor)
Comando_detener = Comando_detener_servidor(servidor)
Comando_reiniciar = Comando_reiniciar_servidor(servidor)
remote = Control_a_distancia()

remote.set_command(Comando_iniciar)
remote.press_button()

remote.set_command(Comando_detener)
remote.press_button()

remote.set_command(Comando_reiniciar)
remote.press_button()