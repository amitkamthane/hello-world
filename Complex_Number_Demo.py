class Complex(object):
      def __init__(self,real,imag=0.0):
            self.real = real
            self.imag = imag

      def print_Complex_Number(self):
            print('(',self.real, ' , ', self.imag,')')
         
      def __add__(self,other):
            return Complex(self.real + other.real,
                           self.imag + other.imag)
      
      def __sub__(self,other):
            return Complex(self.real - other.real,
                           self.imag - other.imag)
 

      def __mul__(self,other):
            return Complex(self.real* other.real
                           - self.imag * other.imag,
                           self.imag* other.real +
                           self.real * other.imag)
    


      def __eq__(self,other):
            return self.real == other.real and self.imag == other.imag

      def __le__(self,other):
            return self.real < other.real and self.imag < other.imag

      def __ge__(self,other):
            return self.real > other.real and self.imag > other.imag
      

C1 = Complex(2, 1)
print('Firsr Complex Number is as Follows:')
C1.print_Complex_Number()

C2 = Complex(5, 6)
print('Second Complex Number is as Follows:')
C2.print_Complex_Number()

print('Addition of two complex Nummber is as follows:')
C3 = C1 + C2
C3.print_Complex_Number()

print('Subtraction of two Complex Number is as follows:')
C4 = C1 - C2
C4.print_Complex_Number()

print('Multiplication of two Complex Number is as follows:')
C5 = C1 * C2
C5.print_Complex_Number()

print('Compare Two Complex Numbers:')
print((C1 == C2))   #Returns true if equal
                    #Returns false if not    

print('Checking if C1 is Greater than C2:')
print(C1 >= C2)   #Returns true if C1 > C2
                  

print('Checking if C1 is Less than C2:')
print(C1 <= C2)   #Returns true if equal



##def __div__(self,other):
##            s_r = self.real
##            s_i = self.imag
##            o_r = other.real
##            o_i = other.imag
##            r =  float((o_r ** 2) + (o_i ** 2))
##            return Complex(((s_r*o_r)+(s_i*o_i))/r, ((s_i*o_r-s_r*o_i))/r)




##print('Divison of two Complex Number is as follows:')
##C6 = C1/C2
##C6.print_Complex_Number()









                           
                           
                           
                           
                           







