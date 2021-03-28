import math

def int_fechada_grau1(a,b,h):
    return (h/2) * (a+b)

def int_aberta_grau1(a,b,h):
    return ((3*h)/2) * (a+b)

def int_fechada_grau2(a, b, c, h):
    return (h/3) * (a + 4*b + c)  

def int_aberta_grau2(a,b, c,h):
    return (4/3)*h*(2*a - b + 2*c)
                    
def int_fechada_grau3(a, b, c, d,h):
    return (3/8)*h * (a + 3*b + 3*c + 1*d)

def int_aberta_grau3(a,b, c, d, h):
    return (5/24)*h * (11*a + b + c + 11*d)

def int_fechada_grau4(a, b, c, d, e, h):
    return ((2*h)/45) * (7*a + 32*b + 12*c + 32*d + 7*e)

def int_aberta_grau4(a,b, c, d,e, h):
    return (3/5)*h*( (11/2)*a - 7*b + 13*c - 7*d + (11/2)*e)
    

def integrate(f,grau,fechada,a,b):
    '''
    Argumentos:
        f - funcao lambda ou normal
        grau - numero com o grau do polinomio
        fechada - Valor booleano, True = Fechada e False = Aberta
        a e b - limites de integração
    '''
    
    if not 1<=grau<=4: 
        print('Grau {} não implementado'.format(grau))
        return 
    
    tolerancia=10E-6
    resultado=0
    diferenca=1
    n=0
    
    while(diferenca>tolerancia):
        l=0
        aux=resultado
        resultado=0
        
        if fechada: h = ((b-a)/(2**n)) / grau
        else: h = ((b-a)/(2**n)) / (grau +2)
    
        while(l<2**n):
            xi = a+l*((b-a)/2**n)
            
            if fechada:
                if grau==4: 
                    resultado = resultado + int_fechada_grau4(f(xi),f(xi+h),f(xi+2*h),f(xi+3*h),f(xi+4*h),h)
                elif grau==3:
                    resultado = resultado + int_fechada_grau3(f(xi),f(xi+h),f(xi+2*h),f(xi+3*h),h)
                elif grau==2:
                    resultado = resultado + int_fechada_grau2(f(xi),f(xi+h),f(xi+2*h),h)
                else:
                    resultado = resultado + int_fechada_grau1(f(xi),f(xi+h),h)   
            else:
                if grau==4:
                    resultado = resultado + int_aberta_grau4(f(xi+h),f(xi+2*h),f(xi+3*h),f(xi+4*h),f(xi+5*h),h)
                elif grau==3:
                    resultado = resultado + int_aberta_grau3(f(xi+h),f(xi+2*h),f(xi+3*h),f(xi+4*h),h)
                elif grau==2:
                    resultado = resultado + int_aberta_grau2(f(xi+h),f(xi+2*h),f(xi+3*h),h)
                else:
                    resultado = resultado + int_aberta_grau1(f(xi+h),f(xi+2*h),h)  
                    
            l=l+1
            
        diferenca=abs(resultado-aux)
        n=n+1
        print('iteracao {} = {}'.format(n,resultado))
        
    return resultado
    
if __name__ == '__main__':
    #f = lambda x: x**2
    #f = lambda x: 3*x + 7     
    f = lambda x: (math.sin(2*x) + 4*x**2 + 3*x)**2  
    
    grau = int(input('Digite o grau do polinômio de substituição\n'))
    abordagem = str(input('Digite a abordagem\n'))
    abordagem = abordagem.lower()
    
    if abordagem == 'fechada': bol = True
    else: bol = False
  
    print('\n\nIntegral de (sin(2*x) + 4*x^2 + 3*x)^2 de a=0 a b=1 \n\n')
    resultado=integrate(f,grau,bol,0,1)
    print('\nResultado=',resultado)