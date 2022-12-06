
operacion= input("Indica la operacion que quieres:")
print("Digite el primer número: ")
num1=float(input())
print("Digite el segundo numero: ")
num2=float(input())



if operacion=="+":
    print(num1+num2)
    resultado=num1+num2
    print("El resultado de  la suma es :", resultado)
    
elif operacion=="-":
    print(num1-num2)
    resultado=num1-num2
    print("El resultado de  la suma es :", resultado)
elif operacion=="*":
    resultado=num1*num2
    print(num1*num2)
    print("El resultado de  la suma es :", resultado)

elif operacion=="/":
    resultado=num1/num2
    print(num1/num2)
    print("El resultado de  la suma es :", resultado)

print("¿Desea realizar otra operacion?")
respuesta = input()


if respuesta == "si" :
    operacion = input("Ingrese una operacion")
    print("Ingrese numero1")
    num1 = int(input())

    print("Ingrese numero2")
    num2 = int(input())

    
    if operacion == "+":
        resultado = num1 + num2
        print("El resultado de la suma es: ",resultado)
    elif operacion == "-" :
        resultado = num1 - num2
        print("el resultado de la resta es: ", resultado)
    elif operacion == "*" :
        resultado = num1 * num2
        print("el resultado de la Multiplicacion es: ", resultado)

else :
    print("No se puede realizar operacion")

