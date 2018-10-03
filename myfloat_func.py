import copy

"""Esta función iguala el tamaño de las tuplas. Pues lo que hace es llenar con 
ceros los espacios que le hacen falta a las tuplas más pequeñas"""
def igualar(a1,b1):
    a = copy.deepcopy(a1)
    b = copy.deepcopy(b1)
    c = [a[0],a[1]]
    d = [b[0],b[1]]
    if(len(c[1]) < len(d[1])):
        c[1] = c[1] + (len(d[1])-len(c[1]))*[0]
    else:
        d[1] = d[1] + (len(c[1])-len(d[1]))*[0]

    if(len(c[0]) < len(d[0])):
        signo = [c[0][0]]
        c[0].pop(0)
        c[0] = signo + (len(d[0])-(len(c[0])+1))*[0] + c[0]
    else:
        signo = [d[0][0]]
        d[0].pop(0)
        d[0] = signo + (len(c[0])-(len(d[0])+1))*[0] + d[0]

    return (c,d)


"""Esta función imprime la tupla de forma entendible"""
def imprimir(a1):
    a = copy.deepcopy(a1)
    b = []
    i = 0
    while (i < len(a)):
        j=0
        while (j < len(a[i])):
            if(i==1 and j==0):
                b.append('.')
            b.append(str(a[i][j]))
            j = j+1
        i = i+1
    c = ''.join(b)
    return c

"""Esta función retorna al mayor o menor número sin tener en cuenta el signo"""
def may_men(a1,b1):
    a = copy.deepcopy(a1)
    b = copy.deepcopy(b1)
    j=0

    """Aquí se definen quién tiene mayor cantidad de decimales"""
    if(len(a[1])<len(b[1])):
        menor_dec = a
        mayor_dec = b
    else:
        menor_dec = b
        mayor_dec = a
    
    """Aquí se les quita sus signos para evitar problemas de comparación"""
    signo_menor = menor_dec[0].pop(0)
    signo_mayor = mayor_dec[0].pop(0)

    while(j<len(menor_dec)):
        i=0
        while(i<len(menor_dec[j])):
            if(menor_dec[j][i]<mayor_dec[j][i]):
                mayor_dec[0].insert(0,signo_mayor)
                menor_dec[0].insert(0,signo_menor)
                return [mayor_dec,menor_dec]
            elif(menor_dec[j][i]>mayor_dec[j][i]):
                mayor_dec[0].insert(0,signo_mayor)
                menor_dec[0].insert(0,signo_menor)
                return [menor_dec,mayor_dec]
            i = i+1
        j = j+1
    
    mayor_dec[0].insert(0,signo_mayor)
    menor_dec[0].insert(0,signo_menor)
    return [mayor_dec,menor_dec]


"""Esta función hace la suma de los números representados en tuplas"""
def suma_n(a1,b1):
    a = copy.deepcopy(a1)
    b = copy.deepcopy(b1)
    signo = [a[0][0]]
    [a,b] = igualar(a,b)
    extra = 0
    (d,extra) = suma_p(a[1],b[1],0)
    a[0].pop(0)
    b[0].pop(0)
    (e0,extra) = suma_p(a[0],b[0],extra)
    if(extra != 0):
        e = signo + [extra] + e0
    else:
        e = signo + e0
    return (e,d)
    
""" Aquí hace una suma de las componentes de las tuplas"""
def suma_p(a,b,auxiliar):
    suma=[]
    i=len(a)-1
    while(i>=0):
        if(a[i]+b[i]+auxiliar > 9):
            suma.insert(0,(a[i]+b[i]+auxiliar)%10)
            auxiliar = (a[i]+b[i]+auxiliar)//10
        else:
            suma.insert(0,a[i]+b[i]+auxiliar)
            auxiliar = 0
        i = i-1

    return (suma,auxiliar)


"""Aquí hace una resta de las tuplas dadas"""
def resta_n(a1,b1):
    a = copy.deepcopy(a1)
    b = copy.deepcopy(b1)

    """Aquí define qué número es mayor al otro"""
    if (len(a[0])<len(b[0])):
        signo = [b[0][0]]
        mayor = b
        menor = a
    elif (len(a[0])>len(b[0])):
          signo = [a[0][0]]
          mayor = a
          menor = b
    else:
        [mayor,menor] = may_men(a,b)
        signo = [mayor[0][0]]

    [mayor,menor] = igualar(mayor,menor)
    extra = 0
    (d,extra) = resta_p(mayor[1],menor[1],0)
    mayor[0].pop(0)
    menor[0].pop(0)
    (e0,extra) = resta_p(mayor[0],menor[0],extra)
    if(extra != 0):
        e = signo + [extra] + e0
    else:
        e = signo + e0
    return (e,d)

"""Aquí hace la resta de cada una de las componentes de las tuplas"""
def resta_p(a,b,auxiliar):
    resta=[]
    i=len(a)-1
    while(i>=0):
        if(a[i]>=b[i]):
            if(a[i]-b[i]+auxiliar > 9):
                resta.insert(0,(a[i]-b[i]+auxiliar)%10)
                auxiliar = (a[i]-b[i]+auxiliar)//10
            else:
                resta.insert(0,a[i]-b[i]+auxiliar)
                auxiliar = 0
        else:
            a[i] = a[i] + 10
            a[i-1] = a[i-1] - 1
            if(a[i]-b[i]+auxiliar > 9):
                resta.insert(0,(a[i]-b[i]+auxiliar)%10)
                auxiliar = (a[i]-b[i]+auxiliar)//10
            else:
                resta.insert(0,a[i]-b[i]+auxiliar)
                auxiliar = 0
        i = i-1

    return (resta,auxiliar)

"""Hace la multiplicación de dos tuplas"""
def multiplicacion_n(a1,b1,signo):
    a = copy.deepcopy(a1)
    b = copy.deepcopy(b1)
    signoa = [a[0].pop(0)]
    signob = [b[0].pop(0)]
    producto_a = []
    i=len(a)-1

    """Aquí guarda los resultados de multiplicar la lista b con cada elemento
    de a"""
    while(i>=0):
        j=len(a[i])-1
        while(j>=0):
            producto_a.append(multiplicacion_p(a[i][j],b))
            j = j-1
        i = i-1

    """Aquí iguala los tamaños de todos los productos anteriores, de tal forma 
    que se pueda aplicar el algoritmo de multipliación del colegio"""
    k=0
    while(k<len(producto_a)):
        producto_a[k] = (len(producto_a)-1-k)*[0] + producto_a[k] + k*[0]
        #print(producto_a[k],"\t",k)
        k = k+1

    """Aquí se van sumando todas las listas anteriores elemento a elemento"""
    l=len(producto_a[0])-1
    extra=0
    producto_t = []
    while(l>=0):
        sumad = extra
        m = 0
        while(m<len(producto_a)):
            sumad = sumad + producto_a[m][l]
            m = m+1
        #print(sumad,"hey")
        producto_t.insert(0,sumad%10)
        extra = sumad//10
        l = l-1
    #print(producto_t,"hey")

    """Aquí se separa el producto final en parte decimal y en parte entera"""
    parte_d=len(a[1])+len(b[1])-1
    d=[]
    i=len(producto_t)-1
    while(parte_d >= 0):
        d.insert(0,producto_t[i])
        parte_d = parte_d - 1
        i = i-1
    
    parte_e=(len(producto_t)-1)-(len(a[1])+len(b[1]))
    e=[]
    while(parte_e >=0):
        e.insert(0,producto_t[parte_e])
        parte_e = parte_e - 1

    return (signo + e, d)


"""Aquí se multiplica la lista b por el número a"""
def multiplicacion_p(a,b):
    producto_a = []
    auxiliar = 0
    i=len(b)-1

    while(i>=0):
        j=len(b[i])-1
        while(j>=0):
            producto_a.insert(0,((b[i][j]*a)+auxiliar)%10)
            auxiliar = ((b[i][j]*a)+auxiliar)//10
            j = j-1
        i = i-1

    producto_a.insert(0,auxiliar)
    
    #print(producto_a, "hola")
    return producto_a

"""Este algoritmo divide a las dos listas en el orden asignado"""
def division_n(a1,b1,signo,cifras):
    a = copy.deepcopy(a1)
    b = copy.deepcopy(b1)
    a[0].pop(0)
    b[0].pop(0)
    c = a[0][:] + a[1][:]
    d = b[0][:] + b[1][:]

    if(len(c) < len(d)):
        c = c + (len(d)-len(c))*[0]
    
    

"""Este algoritmo decide si la suma corresponde a una suma o a una resta"""
def suma(a, b):
    if(a[0][0]=='+'):
        if(b[0][0]=='+'):
            return suma_n(a,b)
        elif(b[0][0]=='-'):
            return resta_n(a,b)
    elif(a[0][0]=='-'):
        if(b[0][0]=='+'):
            return resta_n(a,b)
        elif(b[0][0]=='-'):
            return suma_n(a,b)
    else:
        print('Error.Lo sentimos, su número no está signado, por favor signéelo.')


"""Este algoritmo decide si la suma corresponde a una suma o a una resta"""
def resta(a, b):
    if(a[0][0]=='+'):
        if(b[0][0]=='+'):
            b[0][0] = '-'
            return resta_n(a,b)
        elif(b[0][0]=='-'):
            b[0][0] = '+'
            return suma_n(a,b)
    elif(a[0][0]=='-'):
        if(b[0][0]=='+'):
            b[0][0] = '-'
            return suma_n(a,b)
        elif(b[0][0]=='-'):
            b[0][0] = '+'
            return resta_n(a,b)
    else:
        print('Error.Lo sentimos, su número no está signado, por favor signéelo.')


"""Este define si es una multipliación que da positivo o negativo"""
def multiplicacion(a,b):
    if(a[0][0]==b[0][0]):
        return multiplicacion_n(a,b,['+'])
    elif(a[0][0]!=b[0][0]):
        return multiplicacion_n(a,b,['-'])
    else:
        print('Error.Lo sentimos, su número no está signado, por favor signéelo.')


"""Este define si es una división que da positivo o negativo"""
def division(a,b,cifras):
    if(a[0][0]==b[0][0]):
        return division_n(a,b,['+'],cifras)
    elif(a[0][0]!=b[0][0]):
        return division_n(a,b,['-'],cifras)
    else:
        print('Error.Lo sentimos, su número no está signado, por favor signéelo.')


"""Este algoritmo decide si las tuplas son iguales o no"""
def comparacion(a, b):
    i=0
    while(i<2):
        if(len(a[i]) != len(b[i])):
            print("Las tuplas ",a,", ",b," no representan el mismo número.")
            return 0
        else:
            j=0
            while(j<len(a[i])):
                if(a[i][j] != b[i][j]):
                    print("Las tuplas ",a,", ",b," no representan el mismo número.")
                    return 0
                j = j+1
        i = i+1
    print("Las tuplas ",a,", ",b," representan el mismo número.")
    return 1

""" Esta función transforma un flotante en una tupla """
def float_to_tuple(f):
    if(f >=0):
        signo = ['+']
    else:
        signo  = ['-']

    str_f = str(f)
    
    part_e = []
    i = 0
    while(str_f[i] != '.'):
        part_e.append(int(str_f[i]))
        i = i+1
    
    i = len(part_e)+1
    part_d = []
    while(i < len(str_f)):
        part_d.append(int(str_f[i]))
        i = i+1

    return (signo + part_e, part_d)
    

""" Esta función transforma un entero en tupla """
def int_to_tuple(i):
    if(i >=0):
        signo = ['+']
    else:
        signo  = ['-']

    str_i = str(i)
    
    entero = []
    k = 0
    while(k < len(str_i)):
        entero.append(int(str_i[k]))
        k = k+1

    return (signo + entero, 30*[0])



def pi():
    pass


if __name__ == "__main__":
    print(imprimir(pi()))
