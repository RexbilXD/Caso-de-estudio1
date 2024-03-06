class CuentaCorriente:
    
    saldo = 0
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    def ConsultarSaldo(self):
        return self.saldo
    
    def ConsignarMonto(self, monto):
        # #Forma 1
        # self.saldo += monto
        # # Forma 2
        # self.saldo = self.saldo + monto
        # # Forma 3
        total = self.saldo + monto
        self.saldo = total
    
    """def RetirarMonto(self, monto):
        # #Forma 1
        # self.saldo -= monto
        # # Forma 2
        # self.saldo = self.saldo - monto
        # # Forma 3
        total = self.saldo - monto
        self.saldo = total"""
    
    def RetirarMonto(self, monto):
        # Descuentas el 1% del valor retirado
        descuento = monto * 0.01
        montoConDescuento = monto + descuento
        total = self.saldo - montoConDescuento
        self.saldo = total