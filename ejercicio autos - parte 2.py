def calcular_precio(marca,puertas,color):
    marcas = {'ford':10000, 'chevrolet':15000, 'fiat':20000}
    puertas = {2:5000, 4:10000, 5:15000}
    colores = {'blanco':5000, 'azul':3000, 'negro':4000}
    precio = marcas[marca] +colores[color] +puertas[puerta]
    return precio

mas_clientes = 'si'
ventas = []
marcas = ['ford', 'chevrolet','fiat']
puertas = [2,4,5]
colores = ['blanco', 'azul', 'negro']
while mas_clientes =='si':
    nombre = input ("ingrese nombre :")
    apellido = input ("ingrese apellido :")
    marca = ''
     puerta =0
    color = ''
    while marca not in marcas:
        marca = input ('ingrese marca: ')
    while puerta not in puertas:
        puerta = int (input ("ingrese cantidad de puertas :"))
    while color not in colores:
        color = input ('ingrese color: ')
    precio = calcular_precio(marca,puerta,color)
    ventas.append({'nombre':nombre, 'apellido':apellido,'marca':marca, 'puertas': puerta, 'color':color,'precio':precio})
    mas_clientes = input("hay mas clientes? ")


print("la persona: " +nombre+" "+apellido+ " compro un auto marca " + marca+ " color "+color+ " con un precio de $" +str(precio))







        
