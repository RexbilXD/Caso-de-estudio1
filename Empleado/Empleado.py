from Fecha import Fecha

class Empleado:
    #aqui va el codigo del empleado
    """--------------------------------------------
    #Atributos
    --------------------------------------------"""
    nombre= ""
    apellido= ""

    """--------------------------------------------
    #1 para Masculino y 2 para Femenino
    --------------------------------------------"""
    sexo= 0
    salario= 0

    """--------------------------------------------
    #Asociaciones
    --------------------------------------------"""

    fechaNacimiento= Fecha()
    fechaIngreso= Fecha()

    """--------------------------------------------
    #metodos
    --------------------------------------------"""
    def CambiarSalario(self,nuevoSalario):
        #Aqui va el codigo del metodo cambiar salario
        return 0
    
    def CambiarEmpleado(self,nNombre,nApellido, nSexo, nSalario):
        #Aqui va el codigo del metodo cambiar apellido del empleado
        return None
    
    def ConsultarSalario(self):
        #Aqui va el codigo de consultar salario
        return self.salario
    
    def ConsultarSexo(self):
        #Aqui va el codigo de consultar sexo
        return self.sexo
    
    def ConsultarNombre(self):
        #Aqui va el codigo de consultar nombre
        return self.nombre
    
    def ConsultarApellido(self):
        #Aqui va el codigo de consultar apellido
        return self.apellido
    
    def ConsultarNombreCompleto(self):
        #Aqui va el codigo de consultar nombre
        return self.nombre +" "+ self.apellido
    
    def AumentoSalario(self):
        nSalario= self . salario * 0.05
        nSalario= nSalario + self. salario
        self.salario= nSalario

        return "El nuevo salario es de : "+self.salario
    def CambiarNombre(self,nNombre):

        return "El nuevo nombre es"+ self.nombre
    def CambiarApellido(self,nApellido):
        return "El nuevo apellido es"+ self.apellido
    
    def DuplicarSalario(self):
        #Aqui va el dodigo de para duplicar el salario

        #Forma 1
        #self.salario = self.salario*2

        #Forma 2
        self.salario *=2

    def CalcularSalarioAnual(self):
        #Aqui va el salario anual del empleado
        salarioAnual = self.salario *12
        #Forma1
        #return salarioAnual
        #Forma 2
        return self.salario*12
    
    def ConsultarDiaCumpleanios(self):
        return "el dia de su coumpleños es: "+self.fechaNacimiento.consultarDia()
    
    def CalcularImpuesto(self):
         #Forma 1
        total = self.CalcularSalarioAnual()
        return total * 19.5 /100
    
        #Forma 2
        #return self.CalcularSalarioAnual()* 0.195