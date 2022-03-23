# Análisis gramatical-análisis predictivo no recursivo
import pandas as pd
# Tabla de análisis de pronósticos con marca de sincronización
data={'id':['E→TE\'','','T→FT\'','','F→id'],
      '+':['','E\'→+TE\'','t','T\'→ε','t'],
      '*':['','','','T\'→*FT\'','t'],
      '(':['E→TE\'','','T→FT\'','','F→(E)'],
      ')':['t','E\'→ε','t','T\'→ε','t'],
      '#':['t','E\'→ε','t','T\'→ε','t']}
frame=pd.DataFrame(data,index=['E','E\'','T','T\'','F'])
stk="#E"#Simula la pila con cadenas
ahead=""# Fichas de entrada actualmente pendientes
sub=""   # La entrada después de que se procese el token pendiente actual
def nextToken():# Consigue el siguiente token léxico
    global sub
    if(sub[0:2]=="id"):
         sub=sub[2:]
         return "id"
    else:
        s=sub[0:1]
        sub=sub[1:]
        return s
def empty():# Está la pila vacía
    if(len(stk)==0):
        return True
    return False
def top():# Obtenga el elemento superior de la pila
    global stk
    if(stk[-1:]=='\''or stk[-1:]=='d'):
        return stk[-2:]
    else:
        return stk[-1:]
def pop():# Elemento superior de Popup
    global stk
    if(stk[-1:]=='\''or stk[-1:]=='d'):
        stk=stk[:-2];
    else:
        stk=stk[:-1]
def push(s):# Producción → Orden inverso a la derecha
    global stk
    while s[-1:]!='→':
        if(s[-1:]=='\'' or s[-1:]=='d'):
            stk+=s[-2:]
            s=s[0:-2]
        else:
            stk+=s[-1:]
            s=s[0:-1]
def  handle(top,head):# Programa de análisis predictivo
    global ahead
    if top==head :
        if head!='#':# No hay coincidencias de salida #
            print('Partido',head)
        ahead=nextToken()
        pop()
    else:
        s=frame[head][top]# Obtener producción de la tabla de análisis de pronósticos
        if s=='':# Error, omita el token actual
            ahead = nextToken()
        elif s=='t':# Error, no hay necesidad de omitir ningún token en este conjunto de tokens de sincronización no terminal, el terminal aparece
            pop()
        else:
            print(s)
            pop()
            if(s[-1:]!='ε'):#Para producciones que producen cadenas vacías, solo revienta la pila, no la pila
                push(s)
if __name__ == '__main__':
    print('____________________________')
    sub=input()
    print('____________________________')
    sub+='#'
    ahead=nextToken()
    while(empty()==False):#Cuando la pila no está vacía
        t=top()# Obtenga el elemento superior de la pila
        handle(t,ahead)# Llame al programa de análisis predictivo
    print('____________________________')