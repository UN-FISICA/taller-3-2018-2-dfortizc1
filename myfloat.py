class MyFloat:

    def __init__(self,a):
        """ Define un número en términos de su parte entera y decimal por
        medio de listas"""
        self.tpl = a
        self.dec = a[1]
        self.ent = a[0]

    def __add__(self,other):
        """ Define la adición de una tupla con otra tupla, int o float """
        if isinstance(other,MyFloat):
            return fc.suma(self.tpl,other.tpl)
        elif isinstance(other,int):
            tuple_int = fc.int_to_tuple(other)            
            return fc.suma(self.tpl,tuple_int)
        elif isinstance(other,float):
            tuple_other = fc.float_to_tuple(other)
            return fc.suma(self.tpl,tuple_other)
        else:
            return NotImplemented

    def __sub__(self,other):
        """ Define la resta de una tupla con otra tupla, int o float """
        if isinstance(other,MyFloat):
            return fc.resta(self.tpl,other.tpl)
        elif isinstance(other,int):
            tuple_int = fc.int_to_tuple(other)            
            return fc.resta(self.tpl,tuple_int)
        elif isinstance(other,float):
            tuple_other = fc.float_to_tuple(other)
            return fc.resta(self.tpl,tuple_other)
        else:
            return NotImplemented

    def __mul__(self,other):
        """ Define la multiplicación de una tupla con otra tupla, int o 
        float """
        if isinstance(other,MyFloat):
            return fc.multiplicacion(self.tpl,other.tpl)
        elif isinstance(other,int):
            tuple_int = fc.int_to_tuple(other)
            return fc.multiplicacion(self.tpl,tuple_int)
        elif isinstance(other,float):
            tuple_other = fc.float_to_tuple(other)
            return fc.multiplicacion(self.tpl,tuple_other)
        else:
            return NotImplemented

    def __div__(self,other):
        """ Define la division de una tupla con otra tupla, int o float """
        if isinstance(other,MyFloat):
            return fc.division(self.tpl,other.tpl)
        elif isinstance(other,int):
            tuple_int = fc.int_to_tuple(other)            
            return fc.division(self.tpl,tuple_int)
        elif isinstance(other,float):
            tuple_other = fc.float_to_tuple(other)
            return fc.division(self.tpl,tuple_other)
        else:
            return NotImplemented

    def __radd__(self,other):
        return self.__add__(other)

    def __rsub__(self,other):
        return self.__sub__(other)

    def __rmul__(self,other):
        return self.__mul__(other)

    def __rdiv__(self,other):
        """ Define la division de una tupla con otra tupla, int o float """
        if isinstance(other,MyFloat):
            return fc.division(other.tpl,self.tpl,30)
        elif isinstance(other,int):
            tuple_int = fc.int_to_tuple(other)            
            return fc.division(tuple_int,self.tpl,30)
        elif isinstance(other,float):
            tuple_other = fc.float_to_tuple(other)
            return fc.division(tuple_other,self.tpl,30)
        else:
            return NotImplemented 

    def __str__(self):
        return fc.imprimir(self.tpl)

    def __repr__(self):
        return fc.imprimir(self.tpl)

    def __eq__(self,other):
        if isinstance(other,MyFloat):
            if(fc.comparacion(self.tpl,other.tpl) == True):
                return True
            elif(fc.comparacion(self.tpl,other.tpl) == False):
                return False
        elif isinstance(other,int):
            tuple_int = fc.int_to_tuple(other)            
            if(fc.comparacion(self.tpl,tuple_int) == True):
                return True
            elif(fc.comparacion(self.tpl,tuple_int) == False):
                return False
        elif isinstance(other,float):
            tuple_other = fc.float_to_tuple(other)
            if(fc.comparacion(self.tpl,tuple_other) == True):
                return True
            elif(fc.comparacion(self.tpl,tuple_other) == False):
                return False
        else:
            return NotImplemented

    def __ne__(self):
        if isinstance(other,MyFloat):
            if(fc.comparacion(self.tpl,other.tpl) == True):
                return False
            elif(fc.comparacion(self.tpl,other.tpl) == False):
                return True
        elif isinstance(other,int):
            tuple_int = fc.int_to_tuple(other)            
            if(fc.comparacion(self.tpl,tuple_int) == True):
                return False
            elif(fc.comparacion(self.tpl,tuple_int) == False):
                return True
        elif isinstance(other,float):
            tuple_other = fc.float_to_tuple(other)
            if(fc.comparacion(self.tpl,tuple_other) == True):
                return False
            elif(fc.comparacion(self.tpl,tuple_other) == False):
                return True
        else:
            return NotImplemented


if __name__ == "__main__":
    # Escribir aca el codigo para calcular pi. Al finalizar el calculo solo
    # debe imprimir el valor de pi, sin otros textos ni nada
    import myfloat_func as fc
    pi = MyFloat((['+',0],[0]))
    k = 0
    while(k<1000000):
        if(k%2 == 0):
            pi = MyFloat(MyFloat(pi.tpl) + 4/((2*k)+1) )
        else:
            pi = MyFloat(MyFloat(pi.tpl) - 4/((2*k)+1) )
        k += 1
    print(pi)
