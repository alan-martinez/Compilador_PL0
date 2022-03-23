import java.io.*;
class Analizador {
 static int preanalisis;
 public Analizador() throws IOException {
 preanalisis = System.in.read();
 }
 void expr() throws IOException {
 term();
 while(true) {
 if( preanalisis == ’+’ ) {
 coincidir(’+’); term(); System.out.write(’+’);
 }
 else if( preanalisis == ’−’ ) {
 coincidir(’−’); term(); System.out.write(’−’);
 }
 else return;
 }
 }
 void term() throws IOException {
 if( Character.isDigit((char) preanalisis) ) {
 System.out.write((char) preanalisis); coincidir(preanalisis);
 }
 else throw new Error("error de sintaxis");
 }
 void coincidir(int t) throws IOException {
 if(preanalisis == t ) preanalisis = System.in.read();
 else throw new Error("error de sintaxis");
 }
}
public class Postfijo {
 public static void main(String[] args) throws IOException {
 Analizador analizar = new Analizador();
 analizar.expr(); System.out.write(’\n’);
 }
}