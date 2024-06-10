tareas = []
tarea1 = {"nombre": "Hacer la compra", "descripcion": "Comprar leche, pan y frutas", "estado": "pendiente"} 
tareas.insert(0, tarea1)
tarea2 = {"nombre": "Estudiar para el examen", "descripcion": "Repasar apuntes y hacer ejercicios", "estado": "en progreso"} 
tareas.insert(1, tarea2)
tarea3 = {"nombre": "Llamar al médico", "descripcion": "Pedir cita para revisión anual", "estado": "pendiente"} 
tareas.insert(2, tarea3)
tareas.pop(1) # Eliminar la tarea en la posición 1
for indice, tarea in enumerate(tareas): print(f"Tarea {indice + 1}: {tarea['nombre']} - {tarea['descripcion']} - Estado: {tarea['estado']}")