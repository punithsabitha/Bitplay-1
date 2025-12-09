def setorNot(number , n):
   mask = 1 <<(n - 1)
   if number & mask:
      print("SET")
   else:
      print("NOT SET")

      number = int(input("Enter the number :"))
      n = int(input("Enetr the bit position:"))
      setorNot(number , n)