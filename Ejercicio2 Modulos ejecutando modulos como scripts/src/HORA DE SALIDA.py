import time

# Obtener la hora actual del sistema en formato de hora local
hora_actual = time.localtime().tm_hour

# Definir la hora límite para ir a casa
hora_limite = 19

if hora_actual >= hora_limite:
    print("Es hora de ir a casa")
else:
    # Obtener la hora y minutos actuales
    minutos_actuales = time.localtime().tm_min
    hora_actual = time.localtime().tm_hour

    # Calcular el tiempo restante de trabajo
    minutos_restantes = (hora_limite - hora_actual - 1) * 60 + (60 - minutos_actuales)

    # Mostrar el tiempo restante de trabajo
    print("Quedan {} minutos para ir a casa".format(minutos_restantes))
