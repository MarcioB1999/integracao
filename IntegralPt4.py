import math
import numpy as np
import time
from sys import exit

def X(xi, xf, ak):
    return ((xi+xf)/2)+((xf-xi)/2)*ak

def xs_simples(s,a, b):
    return ((a+b)/2)+(((b-a)/2)*math.tanh(s))

def xs_dupla(s,a, b):
    return ((a+b)/2)+(((b-a)/2)*math.tanh((math.pi/2) * math.sinh(s)))

def exp_simples(s,a, b,f):
    return (f(xs_simples(s,a,b)))*(((b-a)/2)*(1/(math.cosh(s)**2)))

def exp_dupla(s,a, b,f):
    return (f(xs_dupla(s,a,b)))*(((b-a)/2)*((math.pi/2)*(math.cosh(s)/((math.cosh((math.pi/2)*math.sinh(s)))**2))))

def GaussL4(a,b,f,lim_inf,lim_sup,simples=True):
    w1 = (1/2)-(math.sqrt(5/6))/6
    w2 = (1/36)*(18+math.sqrt(30))
    c=-((3+2*(6/5)**(1/2))/7)**(1/2)
    d=-((3-2*(6/5)**(1/2))/7)**(1/2)
    e=((3-2*(6/5)**(1/2))/7)**(1/2)
    g=((3+2*(6/5)**(1/2))/7)**(1/2)
    
    if simples:
        return ((b-a)/2)*((exp_simples(X(a, b, c),lim_inf,lim_sup,f))*w1+(exp_simples(X(a, b, d),lim_inf,lim_sup,f))*w2+(exp_simples(X(a, b, e),lim_inf,lim_sup,f))*w2+(exp_simples(X(a, b, g),lim_inf,lim_sup,f))*w1)
    else: 
        return ((b-a)/2)*((exp_dupla(X(a, b, c),lim_inf,lim_sup,f))*w1+(exp_dupla(X(a, b, d),lim_inf,lim_sup,f))*w2+(exp_dupla(X(a, b, e),lim_inf,lim_sup,f))*w2+(exp_dupla(X(a, b, g),lim_inf,lim_sup,f))*w1)


def integrate(f,c,lim_inf,lim_sup,flag_exp=True,many_c=False):
    # grau do legendre = n integra polinômios f de grau até 2n -1

    '''
    Argumentos:
        f - funcao lambda ou normal
        c - limites de integração da fórmula numérica
        lim_inf - limite inferior de integração(a)
        lim_sup - limite superior de integração(b)
        flag_exp - Se True: Exponencial Simples,se não: dupla
        many_c - Se False: Roda pra só um c, se não: roda para vários
    '''
    if many_c: intervalo = np.linspace(1,c,math.floor(c))
    else: intervalo = [c]
    
    resultados = []
    tolerancia=10E-3
    aux_c=resultado_c=0
    
    for i in intervalo:
        print('c =',i)
        aux_c=resultado_c    
        resultado=0
        diferenca=1
        n=0
        a,b = -i,i                       #limites da integral numérica
        t0=time.time()
        while(diferenca>tolerancia):
            l=0
            aux=resultado
            resultado=0
            while(l<2**n):
                if flag_exp:
                    resultado=resultado+GaussL4(a+(l*(b-a)/2**n), a+((l+1)*(b-a)/2**n),f,lim_inf,lim_sup)
                else:
                    resultado=resultado+GaussL4(a+(l*(b-a)/2**n), a+((l+1)*(b-a)/2**n),f,lim_inf,lim_sup,False)
                l=l+1
                
            diferenca=abs(resultado-aux)
            n=n+1
            print('iteracao {} = {}'.format(n,resultado))
            
            #if time.time() - t0 >= 60:
                #A partir desse ponto as iterações seguintes melhoram pouca coisa e demoram muito
            #    print('Tempo limite atingido')
            #    break
            
        resultado_c = resultado
        resultados.append((i,resultado_c))
        print('Resultado=',resultado_c)
        if many_c and i>1: print('Diferença absoluta em relacao ao c anterior= {} \n'.format(abs(aux_c-resultado_c)))
        
        
    return resultados

if __name__ == '__main__':
    int_func = int(input('Digite o número da função:\n[1]: 1/(x^(2/3))\n[2]: 1/(sqrt(4-x**2))\n'))
    if not 1<=int_func<=2:
        exit('Dígito inválido')
    if int_func == 1: f = lambda x: 1/((x**2)**(1/3))
    else: f = lambda x: 1/ (math.sqrt(4-x**2))
    
    int_exp = int(input('\n[1]: Exponenciação Simples\n[2]: Exponenciação Dupla\n'))
    if not 1<=int_exp<=2:
        exit('Dígito inválido')
 
    if int_exp == 1: 
        flag_exp = True
        print('Exponenciação Simples\nMelhor para função 1 com a=-1 e b=1 é c=4\nMelhor para função 2 com a=-2 e b=0 é c=15\n')
    else: 
        print('Exponenciação Dupla\nMelhor para função 1 com a=-1 e b=1 é c=2\nMelhor para função 2 com a=-2 e b=0 é c=3\n')
        flag_exp = False
    

    lim_inf = float(input('Digite o limite inferior de integração:\n'))
    lim_sup = float(input('Digite o limite superior de integração:\n'))
    
    
    int_c = int(input('Como quer usar o c?\n[1]: Usar só um c\n[2]: Vários c\n'))
    if int_c == 1: 
        c = float(input('Digite o c:\n'))
        t=time.time()
        resultados = integrate(f,c,lim_inf,lim_sup,flag_exp=flag_exp)
        t=time.time()-t
        print("c = {} - mean time = {} segundos \n".format(c,t / 3));

        print('resultados=\n(c,resultado) \n\n',resultados)
    elif int_c == 2:
        print('\nSerá gerada uma lista com números igualmente espaçados de 1 a c')
        c = float(input('Digite o c:\n'))
        resultados = integrate(f,c,lim_inf,lim_sup,flag_exp=flag_exp,many_c=True)
        print('resultados=\n(c,resultado) \n\n',resultados)
    else: exit('Dígito inválido')
