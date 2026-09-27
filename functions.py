def monthly_saving(i_mensuales,porcentaje_ahorro):
    """Calcular el porcentaje de dinero que puede el usuario ahorrar cada mes."""
    return (i_mensuales * (porcentaje_ahorro / 100))

def monthly_interest(tipo_interes):
    """Calcular el interés mensual de la inversión."""
    return (tipo_interes /12)/100 #DUDA -> ¿Se dejan espacios o no?

def monthly_return(ahorro_mensual,interes_mensual):
    return (ahorro_mensual * interes_mensual)