# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    mes = mes + 1
    if(mes >= pago_extra_mes_comienzo) and (mes <= pago_extra_mes_fin):
        pago = pago_mensual + pago_extra
        saldo = saldo * (1+tasa/12) - pago
        total_pagado = total_pagado + pago
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    print('meses', mes, 'total pagado', round(total_pagado, 2), 'saldo', round(saldo, 2))
    if saldo <= 0:
        resto = ''
        resto = pago_mensual + saldo
        print('Ultimo mes con ajuste: ', round(resto, 2))
print ('Total Pagado: ', round(total_pagado, 2))
print ('Mes: ', mes)