#Prueba_Parcial_4_R_Zuniga

#Diccionario de compradores
compradores = {}

#Función de validación del código de confirmación
def valid_cod(codigo):
    if len (codigo) < 6:
        return False
    if ' ' in codigo:
        return False

#Verificación de mayúscula y número
    mayusc = any(c.isupper() for c in codigo)
    numer = any(c.isdigit() for c in codigo)
    return mayusc and numer

#Usuario ingresa su nombre de comprador
def compra_entradas():
    nombre_original = input('Ingrese su nombre de comprador: ').strip()
    nombre = nombre_original.lower()
    if nombre in compradores:
        print('Este nombre de comprador ya fue registrado')
        return

#Usuario ingresa tipo de entrada
    tipo_entr = input('Ingrese tipo de entrada (G para general, V para VIP): ').strip().upper()
    if tipo_entr not in['G', 'V']:
        print('Tipo de entrada inválido: sólo se permite G o V')
        return

#Usuario ingresa código de confirmación
    codigo = input('Ingrese código de confirmación: ').strip()
    if not valid_cod(codigo):
        print('Código inválido. Debe tener al menos 6 caracteres, una mayúscula, un número y sin espacios')
        return

#Actualización de diccionario
    compradores[nombre] = {'tipo': tipo_entr, 'código': codigo}
    print('¡Entrada registrada con éxito! Disfrute su espectáculo')

#Función de consulta de comprador
def consult_compr():
    nombre_ingr = input('Ingrese nombre del comprador a consultar: ').strip().lower()
    comprador = compradores.get(nombre_ingr)

    if comprador:
        print(f'Nombre: {comprador['nombre']}')
        print(f'Tipo entrada: {comprador['tipo']}')
        print(f'Código confirmación: {comprador['código']}')
    else:
        print('El comprador no se encuentra')

#Función cancelación de compra
def cancel_compr():
    nombre_ingr = input('Ingrese nombre del comprador para cancelar compra: ').strip().lower()
    if nombre_ingr in compradores:
        del compradores[nombre_ingr]
        print('¡Compra cancelada!')
    else:
        print('No se pudo cancelar su compra')

#Función de compra de entradas (Menú Principal)
def user():
    while True:
        print('Hola, bienvenido al vendedor online de entradas'
          'para el Concierto de Trap con el Conejo Simpático')
        print('\n MENÚ PRINCIPAL')
        print('1.- Comprar entrada')
        print('2.- Consultar comprador')
        print('3.- Cancelar compra')
        print('4.- Salir')
        opcion = input('Por favor, elija una opción: ').strip()
        if opcion == '1':
            compra_entradas()
        elif opcion == '2':
            consult_compr()
        elif opcion == '3':
            cancel_compr()
        elif opcion == '4':
            print('Programa terminado...')
            break
        else:
            print('Debe ingresar una opción válida!!')

#Ejecución del programa
user()


