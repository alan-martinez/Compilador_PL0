package main

import "fmt"
import "reflect"

type Parse struct {
    l Lexer
}

func NewParser(l Lexer) *Parse {    
    return &Parse{l: l}
}

func (p *Parse) Expr() error {    
    if err := p.Term(); err != nil {        
        return err    
    }    
    return p.Add()
}

func (p *Parse) match(id TokId) (Tok, error, bool) {    
    t, err := p.l.Peek()    
    if err == io.EOF {        
        return Tok{}, nil, false    
    }    
    if err != nil {        
        return Tok{}, err, false   
    }    
    if t.Id != id {       
        return t, nil, false    
    }   
    t, err = p.l.Scan()    
    return t, err, true    // matches
}

func (p *Parse) Add() error {    
    if _, err, found := p.match(Add); err != nil || !found {
            return err    
        }    
        if err := p.Term(); err != nil {        
            return err    
        }    
        err := p.Add()    
        if err == io.EOF {        
            err = nil    
        }    
        return err
}

func (p *Parse) Term() error {    
    if err := p.Fact(); err != nil {        
        return err    
    }    
    return p.Mul()
}

func (p *Parse) Mul() error {    
    if _, err, found := p.match(Mul); err != nil || !found {
        return err    
    }    
    if err := p.Fact(); err != nil {        
        return err    
    }    
    err := p.Mul()    
    if err == io.EOF {        
        err = nil    
    }    
    return err
}

func (p *Parse) Fact() error {    
    tok, err := p.l.Peek()    
    if err != nil {        
        return err    
    }    
    switch tok.Id {    
        case Pi:        
        p.l.Scan()        
        return nil    
    case Num:        
        p.l.Scan()        
        return nil    
    case Abs:       
        p.l.Scan()        
        fallthrough    
    case Lparen:        
        p.l.Scan()        
        if err := p.Expr(); err != nil {            
            return  err        
        }        
        if _, _, found := p.match(Rparen); !found {            
            return fmt.Errorf("')' expected")        
        }        
        return nil    
    default:        
        return fmt.Errorf("syntax error")    
    }
}

func (p *Parse) Parse() error {    
    if err := p.Expr(); err != nil {        
        return err    
    }    
    if _, err := p.l.Scan(); err != io.EOF {        
        return fmt.Errorf("syntax error")    
    }    
    return nil
}

func main() {    
    text := `3 + (41.32 * abs(1 * pi))`    
    fmt.Printf("parsing %s\n", text)    
    l := NewLex(NewStrText(text))    
    debuglex = true    
    p := NewParser(l)    
    if err := p.Parse(); err != nil {        
        fmt.Printf("failed: %s\n", err)    
    }else {        
        fmt.Printf("success\n")    
    }
}