# StopIteration

#idk

# regB = 1
# regC = 0

# def INB():
#   regB = regB + 1


def compile():
  with open('textfiles/default.txt', 'r') as archivo:
    regB = 0
    regC = 0
    acumul = 0
    for linea in archivo:
      # Increment,decrement and move B and C
      if 'INB' in linea:
        regB += 1
      if 'INC' in linea:
        regC += 1
      if 'DEB' in linea:
        regB -= 1
      if 'DEC' in linea:
        regC -= 1
      if 'MVBC' in linea:
        regC = regB
      if 'MVCB' in linea:
        regB = regC
      # acumulator operations
      if 'TACI' in linea:
        acumul += 10
      if 'TACD' in linea:
        acumul -= 10
      if 'HACI' in linea:
        acumul += 100
      if 'HACD' in linea:
        acumul -= 100
      if 'MACI' in linea:
        acumul += 1000
      if 'MACD' in linea:
        acumul -= 1000
      #Move from a to b and move from a to c
      if 'MVAB' in linea:
        regB = acumul
      if 'MVAC' in linea:
        regC = acumul

      if 'PRINT' in linea:
        #Yes,to many if statments :/
        print("--------------------")
        print(f'-B:: {regB}         -')
        print("--------------------")
        print(f'-C:: {regC}         -')
        print("--------------------")
        print(f'-A:: {acumul}         -')
        print("--------------------")
        print("END")
      if 'CUSTOM' in linea:
        print("Still working")
