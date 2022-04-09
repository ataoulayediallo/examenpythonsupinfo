"""
notes moyennes et appréciations
"""

def user_input():
 
 while True:
    try:
        
        pc=float(input("note pc:"))
        math=float(input("note math:"))
        svt=float(input("notes svt:"))
        crypto=float(input("note crypto:"))
        python=float(input("note python:"))
        fr=float(input("note fr:"))
        
        m=((pc*5)+(math*6)+(svt*4)+(crypto*1)+(python*2)+(fr*2))/20
        if m>20:
         print("impossible")
    except ValueError :
          print("vous devez fournir un nombre")
    else:
         print("==la moyenne est de==:",m)
    if m<10 :
          print(f"la moyenne est insuffisant")
    elif m>10 and m<12:
    
          print(f"mention assez bien")
    elif m>=12 and m<14:
    
          print(f"mention abien")
    elif m>=14 and m<16:
    
          print(f"mention bien")
    elif m>=16 and m<=20:
    
          print(f"mention excellent")
    else:
    
          print(f"===erreur la moyenne doit etre comprise de 0 à 20=== ")

    
    break
    
     
user_input()
