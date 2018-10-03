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

    def __rsub__(self):
        return self.__sub__(other)

    def __rmul__(self):
        return self.__mul__(other)

    def __rdiv__(self):
        return self.__div__(other)

    def __str__(self):
        return fc.imprimir(self.tpl)

    def __repr__(self):
        pass

    def __eq__(self):
        pass

    def __ne__(self):
        pass

if __name__ == "__main__":
    # Escribir aca el codigo para calcular pi. Al finalizar el calculo solo
    # debe imprimir el valor de pi, sin otros textos ni nada
    pass