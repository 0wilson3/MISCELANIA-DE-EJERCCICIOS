#nuevo.py
import os



while True:
    print( "   MENU: \n\
     1. Operaciones \n \
     2. Condicionales \n \
     6. Ciclos \n \
     0. Salir ")
    opcion= int(input('-->'))
    if(opcion== 1):
    
     #operadores
        print('menu de operadores')
        while True:
         print( "  que desea realizar: \n"),
         print("    1. area de un triangulo \n    2. suma \n    3.elevar al cuadrad \n    4. coversion de euros a dolares \n \
      5. area y perimetro\n\
      6. area y volumen de un cilindro\n\
      7.radio de una sircunferncia\n\
      8. calcular el promedio\n")

         opcion = int(input( '--> '))
         if(opcion==1):
            print( " area de un traingulo:" )
            base = int(input('escriba la base de un triangulo: '))
            altura = int(input('escriba la altura de un triangulo: '))
            area= (altura*base)/2
            print('el area del triangulo es: '+ str(area))
            
            
        
         elif(opcion== 2):
            print( f"  suma de dos numeros: ")
            numero = int(input('escriba un numero: '))
            numero2 = int(input('escriba un numero: '))

            suma=(numero + numero2)
            print('la suma de los numeros es:',suma)
         elif(opcion==3):
            print( f" numero elevado al cuadrado:" )
            numero=int(input('escriba un numero:'))
            print('el cuadrado de',numero,' es:',numero**2)


            
         elif(opcion==4):
            print( f" coversion de euro a dolar:" )
            num=int(input('digite el euro:'))
            dolar=(num*0.90)
            print('su euro vale:',dolar, 'dolares')
           
         elif(opcion==5):
             print( f" Calcular Area y Perimetro:" )
             lado=int(input("digite eel lado de uncuadrado:"))
             perimetro=lado*4
             area= lado*lado

             print("el perimetro del cuadrado es:",perimetro,)
             print("el area del cuadrado es:",area,)
        break
      


      

    
    
    if(opcion==2):
      
       #condicionales
       print("esta en la opcion de condicinales:")
       print( "   MENU: \n\
     1. numero positivo o negativo \n \
     2. calcular cual es el mayor y menor \n \
     3. mayor y menor de 3 numeros \n \
     4. suma y resta depediendo si es positivo o negativo\n\
     5. encontar cociente\n\
     6. suma y multiplicacion de A Y B \n\
     7. determinar year biciestos")
    opcion= int(input('-->'))
    if(opcion==1):
       
       numero=int(input("digite un numero:"))
       if(numero>0):

          print("el numero es positivo")
       elif(numero<0):
         print("el numero es negativo")
       else:
         print("numero es neutro")
       input("presione cualquier tecla")
    if(opcion==2):
       n1=int(input("digite numero:"))
       n2=int(input("digite otro numero:"))
       if(n1>n2):
          print(f"el numero {n1} es mayor que {n2}")
          print(f"el numero {n2} es menor que {n1}")

       elif(n1<n2):
             print(f"el numero {n1} es menor que {n2}")
             print(f"el numero {n2} es mayor que {n1}")
    if(opcion==3):
       print(" mayor y menor de 3 numeros:")
       n1=int(input("escriba el primer numero:"))
       n2=int(input("escriba el segundo numero:"))  
       n3=int(input("escriba el tercer numero:"))   

       if(n2<n1>n3):
          print(f"el numero mayor es:{n1}y el menor es {n2}") 
       elif(n1<n2>n3):
          print(f"el numero mayor es:{n2}y el menor es {n1}") 
       elif(n1<n3>n2):
          print(f"el numero mayor es:{n2}y el menor es {n1}")

    if (opcion==4):
      A=int(input("digite el valor de A:"))
      B=int(input("digite el valor de B:"))

      if(A<B):
         suma=(A+B)
         print(f"la suma de los numeros es:",suma)
      else:

         resta=(A-B)
         print(f"la resta de los numero es:",resta)

      if(opcion==5):
         c=int(input("digite el valor de A:"))
         d=int(input("digite el valor de B:"))
         division=(c//d)
         print("el cociente de los valores ingrados es :",division)

      elif(c==0 and d==0):
         print("la divisiion entre 0 no esta definida!!")

    if(opcion==6):

   #menu de  ciclos 
       print("esta en la opcion de ciclos :")
       print( "   MENU: \n\
     1. multiplos de 3  1 al 100 \n \
     2. numero impares entere 0 y 100\n \
     3. numeros pares del 1 al 100\n \
     4. cuadrados del 1 al 30\n\
     5. cuadrado de los naturales\n\
     6. secuencia ascendente de naturales \n\
     7. suma de todos los numeros por teclado")
    opcion= int(input('-->'))
    if (opcion==1):
       print("multiplos de 3 entre  1 y  100")
       for i in range(3,100,3):
          print(i)
    if (opcion==2):
       print("numeros impares de 0 a 100:")
       x = 1
       while x <= 100:
          if x % 2==1:
             print(x)
          x +=1
    if(opcion==3):
        print("numeros pares de 0 a 100:")
        x = 1
        while x <= 100:
          if x % 2==0:
             print(x)
          x =x +1

       
    


   













          


       




      

   

   
     



             
             

   

    