ahorro_mensual = 0
interes_mensual = 0
rendimiento_mes_1 = 0
i_mensuales = 0
tipo_interes = 0
comprobacion = ""
datos_usuario = {}
saldo_acumulado = 0
rendimiento_anual = 0
activos ={}
valor_inmueble = 0

from functions import monthly_saving
from functions import monthly_interest
from functions import monthly_return


comprobacion = input("Bienvenido a la calculadora de interés compuesto y de ahorros. " \
"A continuación elaboraremos un estudio real según los datos que nos dé, está interesado en hacer el estudio?, responda Si o No: ")
#Se elabora un estudio del ahorro real del mes y el rendimiento mensual de la inversión que hará el usuario.

if comprobacion == "Si":
    datos_usuario["Ingresos mensuales"] = i_mensuales = float(input("¿Cuánto dinero ganas al mes?: "))
    
    # Le preguntamos cuánto de ese dinero va realmente A AHORRAR.
    datos_usuario["% Ahorro"] = porcentaje_ahorro = float(input("¿Qué porcentaje de ese dinero puedes ahorrar al mes? (ej. 10 para 10%): "))
    datos_usuario["Ahorro mensual"] = ahorro_mensual = monthly_saving(i_mensuales,porcentaje_ahorro)
    
    datos_usuario["Tipo de interés"] = tipo_interes = float(input("¿Cuál es el porcentaje de interés anual de la inversión? (ej. 8): "))
    datos_usuario["Interés mensual"] = interes_mensual = monthly_interest(tipo_interes)
    
    # El interés del primer mes se calcula sobre el dinero AHORRADO, no sobre el sueldo.
    datos_usuario["Rendimiento mensual"] = rendimiento_mes_1 = monthly_return(ahorro_mensual,interes_mensual)
    
    print(f"\nTu ahorro real al mes será de: {ahorro_mensual:,.2f}€")
    print(f"El primer mes su dinero generará: {rendimiento_mes_1:,.2f}€ de interés.")
else:
    print("El estudio ha sido cancelado, que tenga buen día")
    exit()

comprobacion = input("\nLe gustaría calcular cuánto genera su dinero al año?, responda Si o No: ")
#Se analiza el efecto compuesto y el rendimiento real que le da al usuario su dinero en un período de un año.

if comprobacion == "Si":
    #Le preguntamos si según los DATOS que subimos, le interesa hacer el RENDIMIENTO ANUAL.
    comprobacion = input(f"Según los datos que ha puesto, y sabiendo que el rendimiento mensual es de {rendimiento_mes_1:.2f}€, podremos calcularlo. Desea que utilicemos los datos anteriores?, responda Si o No: ")
    if comprobacion == "Si":
        for mes in range(1, 13):
            saldo_acumulado += datos_usuario["Ahorro mensual"]
            saldo_acumulado *= (1 + datos_usuario["Interés mensual"])
        total_ahorrado_cuerpo = datos_usuario["Ahorro mensual"] * 12
        rendimiento_anual = saldo_acumulado - total_ahorrado_cuerpo
        
        datos_usuario["Rendimiento anual"] = rendimiento_anual
        datos_usuario["Saldo total 1 año"] = saldo_acumulado
        
        print(f"El primer año su dinero habrá acumulado un total de: {saldo_acumulado:.2f}€.")
        print(f"De los cuales, la ganancia real por interés compuesto es de: {rendimiento_anual:.2f}€.")
else:
    print("El estudio ha sido cancelado, que tenga buen día.")
    exit()

comprobacion = input("\nDesea que imprima por pantalla los resultados todos de nuevo?, responda Si o No: ")

if comprobacion == "Si":
    comprobacion = input("\n¿Posee algún inmueble de inversión?, responda Si o No: ")
    if comprobacion == "Si":
        activos["Inmuebles"] = []
        while comprobacion == "Si":
            valor_inmueble = input("\n¿Podría poner el valor monetario del inmueble?: ")
            activos["Inmuebles"].append(valor_inmueble)
            comprobacion = input("¿Posee algún inmueble más?, responda Si o No: ")

        total_inmuebles = sum(activos["Inmuebles"])
else:
     print("El estudio ha sido cancelado, que tenga buen día.")
     exit()

print(f"\nEl valor total de los inmuebles es de {total_inmuebles}€")