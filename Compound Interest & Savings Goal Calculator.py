i_anuales = 0
i_mensuales = 0
tipo_interes = 0
años = 0
comprobacion = ""

comprobacion = input("Bienvenido a la calculadora de interés compuesto y de ahorros. A continuación elaboraremos un estudio real según los datos que nos dé, está interesado en hacer el estudio?, ponga Si o No: ")

if comprobacion == "Si":
    i_mensuales = float(input("¿Podría añadir la cantidad de dinero que percibe mensualmente?: "))
    i_anuales = (i_mensuales * 12)
    tipo_interes = float(input(f"Hemos calculado que sus ingresos anuales son de: {i_anuales}. Ahora seguiremos calculando el interés generado en un año y en un mes. ¿Cuál es el porcentaje de interés que su banco le ofrece?: "))
    rendimiento_mensual = (((tipo_interes/100)/12) * i_mensuales)
    rendimiento_anual = ((tipo_interes/100) * i_anuales)
    print(f"El rendimiento que generarían tus ingresos en un mes sería de: {rendimiento_mensual}")
