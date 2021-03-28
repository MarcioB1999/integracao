from sys import exit
import math
from math import exp 
from math import sqrt 


def her(f,n):
    '''
    Gauss-Hermite
    a = -inf , b = +inf
    '''
    
    '''
    Argumentos
        f - funcao lambda ou normal
        n - grau do polinomio de Hermite
    '''
   
    x = [0]*n
    w = [0]*n
    if n==2:
        x[0] = -1/sqrt(2)
        x[1] = -x[0]
        w[0] = sqrt(math.pi)/2
        w[1] = w[0]
    elif n==3:
        x[0] = -(sqrt(3/2))
        x[1] = 0
        x[2] = -x[0]
        w[0] = sqrt(math.pi)/6
        w[1] = (2*sqrt(math.pi))/3
        w[2] = w[0]
    else:
        x[0] = -(sqrt(3/2 + sqrt(3/2)))
        x[1] = -(sqrt(3/2 - sqrt(3/2)))
        x[2] = -x[1]
        x[3] = -x[0]
        w[0] = sqrt(math.pi)/(4*(3+sqrt(6)))
        w[1] = -sqrt(math.pi)/(4*(sqrt(6)-3))
        w[2] = w[1]
        w[3] = w[0]
       
    return sum([f(x[i])*w[i] for i in range(n)])     
 
        
def lag(f,n):
    '''
    Gauss-Laguerre
    a = 0 , b = +inf
    '''
    
    '''
    Argumentos
        f - funcao lambda ou normal
        n - grau do polinomio de Laguerre
    '''
    
    x = [0]*n
    w = [0]*n
    if n==2:
        x[0] = 2-sqrt(2)
        x[1] = 2+sqrt(2)
        w[0] = (1/4)*(2+sqrt(2))
        w[1] = (1/4)*(2-sqrt(2))
    elif n==3:
        x[0] = 0.4157745568
        x[1] = 2.2942803603
        x[2] = 6.2899450829
        w[0] = 0.7110930099
        w[1] = 0.2785177336
        w[2]=  0.0103892565
    else:
        x[0] = 0.32255
        x[1] = 1.7458
        x[2] = 4.5366
        x[3] = 9.3951
        w[0] = 0.603115
        w[1] = 0.357347
        w[2] = 0.0388894
        w[3] = 0.000539278
       
    return sum([f(x[i])*w[i] for i in range(n)])    
   

def cheb(f,n):
    '''
    Gauss-Chebyshev
    a = -1 , b = +1
    '''
    
    '''
    Argumentos
        f - funcao lambda ou normal
        n - grau do polinomio de Chebyshev
    '''
    
    x = [0]*n
    w = [0]*n
    if n==2:
        x[0] = -1/sqrt(2)
        x[1] = -x[0]
        w[0] = math.pi/2
        w[1] = w[0]
    elif n==3:
        x[0] = -(sqrt(3)/2)
        x[1] = 0
        x[2] = -x[0]
        w[0] = math.pi/3
        w[1] = w[0]
        w[2]=  w[0]
    else:
        x[0] = -(sqrt(2 + sqrt(2))/2)
        x[1] = -(sqrt(2 - sqrt(2))/2)
        x[2] = -x[1]
        x[3] = -x[0]
        w[0] = math.pi/4
        w[1] = w[0]
        w[2] = w[0]
        w[3] = w[0]
       
    return sum([ f(x[i])*w[i] for i in range(n)]) 
    
    
def integrate(f,grau,metodo):
    '''
    Argumentos:
        f - funcao lambda ou normal
        grau - grau do polinomio de H,L ou C
        metodo - função her,lag ou cheb
    '''
    
    if not 2<=grau<=4: 
        print('grau {} não implementado'.format(grau))
        return 
    
    resultado=metodo(f,grau)   
    return resultado


def rodar(int_metodo,funcs):    
        str_funcs = ['[1]: exp(-x^2)*x^2 \n[2]: exp(-x^2)*cos(x) \n[3]: exp(-x^2)*(x+1)^2',
                     '[1]: exp(-x)* (x-1)^3 \n[2]: exp(-x)*x^3 \n[3]: exp(-x)*x*(x^2+4)',
                     '[1]: 1/sqrt(1-x^2)* x/( (x^2+4)^(3/2)) \n[2]: 1/sqrt(1-x^2)*(2*x) / ((x**2+1)**2)  \n[3]: 1/sqrt(1-x^2)*(x+1)']
        
        if int_metodo == 1: 
            metodo = her
            funcs = funcs[0]
        elif int_metodo == 2: 
            metodo = lag
            funcs = funcs[1]
        else: 
            metodo = cheb
            funcs = funcs[2]
        
        print('\n'+str_funcs[int_metodo-1])
        int_func = int(input('Digite o número da função: '))
        print('\n')
        if not 1<=int_func<=3:
            exit('Dígito inválido')
        
        for i in range(3):
            print('Grau',i+2)
            resultado=integrate(funcs[int_func-1],i+2,metodo)
            print('Resultado=',resultado,'\n')


if __name__ == '__main__':
    f_hers = [lambda x: x**2,lambda x: math.cos(x),lambda x: (x+1)**2]
    f_lags = [lambda x : (x-1)**3,lambda x: x**3,lambda x: x*(x**2+4)]
    f_chebs = [lambda x: x/( (x**2+4)**(3/2)),lambda x: (2*x) / ((x**2+1)**2),lambda x: x+1 ]
    funcs = [f_hers,f_lags,f_chebs]
    
    print('[1] - Hermite (-inf,+inf) \n[2] - Laguerre (0,+inf) \n[3] - Chebyshev (-1,1)')
    int_metodo = int(input('Digite o número do método: '))
    if not 1<=int_metodo<=3:
        exit('Dígito inválido')
              
    rodar(int_metodo,funcs)