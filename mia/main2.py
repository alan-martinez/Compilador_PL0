def exp():
    term_t = term()
    return resto_expr(term_t)
    
def resto_expr(her):
    if preanalisis == '+':
        coincidir('+')
        return resto_expr(her + term() + '+')
    elif preanalisis == '-':
        coincidir('-')
        return resto_expr(her + term() + '-')
    else:
        return her

def term():
    if preanalisis == '0':
        coincidir('0')
        return '0'
    elif preanalisis == '1':
        coincidir('1')
        return '1'
    elif preanalisis == '2':
        coincidir('2')
        return '2'
    elif preanalisis == '3':
        coincidir('3')
        return '3'
    elif preanalisis == '4':
        coincidir('4')
        return '4'
    elif preanalisis == '5':
        coincidir('5')
        return '5'
    elif preanalisis == '6':
        coincidir('6')
        return '6'
    elif preanalisis == '7':
        coincidir('7')
        return '7'
    elif preanalisis == '8':
        coincidir('8')
        return '8'
    elif preanalisis == '9':
        coincidir('9')
        return '9'
    else:
        raise "No coincidio"

def coincidir(self, cad):
    self.cad = cad
    if cad == '1':
        return '1'
    elif cad == '2':
        return '2'        
    elif cad == '3':
        return '3'        
    elif cad == '4':
        return '4'        
    elif cad == '5':
        return '5'        
    elif cad == '6':
        return '6'        
    elif cad == '7':
        return '7'        
    elif cad == '8':
        return '8'        
    elif cad == '9':
        return '9'        
    elif cad == '0':
        return '0'  
    else:
        raise "No"      
    
    