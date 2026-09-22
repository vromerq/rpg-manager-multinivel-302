def validar_personaje(nombre, clase, nivel, vida=0):
    errores = []

    # 1. Validar nombre no vacío
    if not nombre or nombre.strip() == "":
        errores.append("El nombre no puede estar vacío.")

    # 2. Validar nivel entre 1 y 100
    if nivel < 1 or nivel > 100:
        errores.append("El nivel debe estar entre 1 y 100.")

    # 3. Validar vida entre 10 y 50
    if vida < 10 or vida > 50:
        errores.append("La vida debe estar entre 10 y 50.")

    # 4. Validar clase (Guerrero, Mago, Arquero)
    clase_formateada = clase.capitalize() if clase else ""
    if clase_formateada not in ["Guerrero", "Mago", "Arquero"]:
        errores.append("La clase debe ser Guerrero, Mago o Arquero.")

    return errores