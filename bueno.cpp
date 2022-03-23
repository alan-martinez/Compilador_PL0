#include <string>
#include <vector>
#include <cctype>
// #include "exceptionhelper.h"
#include <iostream>
#include <sys>
// #include <exceptionhelper>

class Analizador
{
 public:
 static int preanalisis;
 Analizador()
 {
 preanalisis = std::getwchar();
 }
 virtual void expr()
 {
 term();
 while (true)
 {
 if (preanalisis == L'+')
 {
 coincidir(L'+');
 term();
 System::out::write(L'+');
 }
 else if (preanalisis == L'−')
 {
 coincidir(L'−');
 term();
 System::out::write(L'−');
 }
 else
 {
	 return;
 }
 }
 }
 virtual void term()
 {
 if (std::isdigit(static_cast<wchar_t>(preanalisis)))
 {
 System::out::write(static_cast<wchar_t>(preanalisis));
 coincidir(preanalisis);
 }
 else
 {
	 throw Error("error de sintaxis");
 }
 }
 virtual void coincidir(int t)
 {
 if (preanalisis == t)
 {
	 preanalisis = std::getwchar();
 }
 else
 {
	 throw Error("error de sintaxis");
 }
 }
};
class Postfijo
{
 public:
 static void main(std::vector<std::wstring> &args)
 {
 Analizador *analizar = new Analizador();
 analizar->expr();
 System::out::write(L'\n');

	 delete analizar;
 }
};

//Helper class added by Java to C++ Converter:

#include <string>
#include <exception>

class Error : public std::exception
{
private:
    std::string msg;

public:
    Error(const std::string& message = "") : msg(message)
    {
    }

    const char * what() const noexcept
    {
        return msg.c_str();
    }
};

//Main function added by Java to C++ Converter:

#include <string>
#include <vector>

int main(int argc, char **argv)
{
	std::vector<std::wstring> args(argv + 1, argv + argc);
	Postfijo::main(args);
}
