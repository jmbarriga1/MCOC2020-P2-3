from caso_D import caso_D
from caso_L import caso_L
from graficar3d import ver_reticulado_3d

ret_D = caso_D()
ret_L = caso_L()

peso = ret_D.calcular_peso_total()

print(f"peso = {peso}")

ver_reticulado_3d(ret_D, 
	axis_Equal=True, 
	opciones_barras={
	"ver_numeros_de_barras": False
	}, 
    llamar_show=True,
    zoom=180.,
    deshabilitar_ejes=True)


#Peso propio
ret_D.ensamblar_sistema()
ret_D.resolver_sistema()
f_D = ret_D.recuperar_fuerzas()

#Carga Viva
ret_L.ensamblar_sistema()
ret_L.resolver_sistema()
f_L = ret_L.recuperar_fuerzas()

#Combinaciones de carga
f_1 = 1.4*f_D           #Combinacion 1
f_2 = 1.2*f_D + 1.6*f_L #Combinacion 2

# Calcular factores 
FU_caso1 = ret_D.recuperar_factores_de_utilizacion(f_1)
FU_caso2 = ret_D.recuperar_factores_de_utilizacion(f_2)


import matplotlib.pyplot as plt

ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 100.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": f_1,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("Tensiones en caso 1: 1.4 D ")
plt.show()



ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 100.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": f_2,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("Tensiones en caso 1: 1.2 D + 1.6 L")
plt.show()




ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 60.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": FU_caso1,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("FU caso 1: 1.4 D ")
plt.show()



ver_reticulado_3d(ret_D, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 60.,
    },
    opciones_barras = {
        "color_barras_por_dato": True,
        "ver_numeros_de_barras": False,
        "ver_dato_en_barras": True,
        "dato": FU_caso2,
        "color_fondo": [1,1,1,0.4]
    }, 
    llamar_show=False,
    zoom=180.,
    deshabilitar_ejes=True)

plt.title("FU caso 2: 1.2 D + 1.6 L")
plt.show()


#Lista de Fu por barra
Pu = []
for i in range(len(f_1)):
    if abs(f_1[i]) > abs(f_2[i]):
        Pu.append(f_1[i])
    else:
        Pu.append(f_2[i])
print (Pu)

ret_D.rediseñar(Pu)
ret_L.rediseñar(Pu)

'''
ELEGIR 5 BARRAS A REDISEÑAR
'''
barras_red = [0,1,2,28,29]

barras_D = ret_D.obtener_barras()

for i in barras_red:
	barras_D[i].rediseñar(Pu[i])

barras_L = ret_L.obtener_barras()

for i in barras_red:
	barras_L[i].rediseñar(Pu[i])

#Peso propio
ret_D.ensamblar_sistema()
ret_D.resolver_sistema()
f_D = ret_D.recuperar_fuerzas()

#Carga Viva
ret_L.ensamblar_sistema()
ret_L.resolver_sistema()
f_L = ret_L.recuperar_fuerzas()

#Combinaciones de carga
f_1 = 1.4*f_D           #Combinacion 1
f_2 = 1.2*f_D + 1.6*f_L #Combinacion 2

# Calcular factores 
FU_caso1_red = ret_D.recuperar_factores_de_utilizacion(f_1)
FU_caso2_red = ret_D.recuperar_factores_de_utilizacion(f_2)