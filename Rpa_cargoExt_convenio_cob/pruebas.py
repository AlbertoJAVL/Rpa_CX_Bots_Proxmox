monto = '$1849.50'
saldo_pendiente = 1849.50

if '$' in monto:
    monto = monto.replace('$', '')

masMenos = saldo_pendiente - float(monto)

if masMenos >= -1.0 and masMenos <= 1.0:
    print('Pago correcto')