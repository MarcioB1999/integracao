import math

def x(xi, xf, ak):
    return ((xi+xf)/2)+((xf-xi)/2)*ak

def GaussL2(a, b,f):
    c=-(1/3)**(1/2)
    d=(1/3)**(1/2)
    return ((b-a)/2)*(f(x(a, b, c))+f(x(a, b, d)))

def GaussL3(a, b,f):
    w1 = 5/9
    w2 = 8/9
    c=-(3/5)**(1/2)
    d=0
    e=(3/5)**(1/2)
    return ((b-a)/2)*((f(x(a, b, c))*w1)+(f(x(a, b, d))*w2)+(f(x(a, b, e))*w1))

def GaussL4(a, b,f):
    w1 = (1/2)-(math.sqrt(5/6))/6
    w2 = (1/36)*(18+math.sqrt(30))
    c=-((3+2*(6/5)**(1/2))/7)**(1/2)
    d=-((3-2*(6/5)**(1/2))/7)**(1/2)
    e=((3-2*(6/5)**(1/2))/7)**(1/2)
    g=((3+2*(6/5)**(1/2))/7)**(1/2)
    return ((b-a)/2)*((f(x(a, b, c))*w1+(f(x(a, b, d))*w2+(f(x(a, b, e))*w2+(f(x(a, b, g))*w1)))))



def integrate(f,grau,a,b):
    '''
    Argumentos:
        f - funcao lambda ou normal
        grau - grau do polinomio de Legendre
        a e b - limites de integração
    '''
    
    if not 2<=grau<=4: 
        print('grau {} não implementado'.format(grau))
        return 
    
    tolerancia=10E-6
    resultado=0
    diferenca=1
    n=0
    
    while(diferenca>tolerancia):
        l=0
        aux=resultado
        resultado=0
        while(l<2**n):
            if grau == 2:
                resultado=resultado+GaussL2(a+(l*(b-a)/2**n), a+((l+1)*(b-a)/2**n),f)
            elif grau ==3:
                resultado=resultado+GaussL3(a+(l*(b-a)/2**n), a+((l+1)*(b-a)/2**n),f)
            else:
                resultado=resultado+GaussL4(a+(l*(b-a)/2**n), a+((l+1)*(b-a)/2**n),f)
            l=l+1
            
        diferenca=abs(resultado-aux)
        n=n+1
        print('iteracao {} = {}'.format(n,resultado))
        
    return resultado

if __name__ == '__main__':
    #f = lambda x: x**2
    #f = lambda x: 3*x + 7     
    f = lambda x: (math.sin(2*x) + 4*x**2 + 3*x)**2  
    grau = int(input('Digite o grau do polinomio de Legendre (de 2 a 4)\n'))
    a = int(input('Digite o a\n'))
    b = int(input('Digite o b\n'))
  
    print('\n\nIntegral de (sin(2*x) + 4*x^2 + 3*x)^2 de a={} a b={} \n\n'.format(a,b))
    resultado=integrate(f,grau,a,b)
    print('\nResultado=',resultado)
