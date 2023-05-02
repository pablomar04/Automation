import time
#NAFTA
n11 = ["X030","X030101N","1er servicio","",""]
n12 = ["X030","X030101N","1er servicio","",""]
n13 = ["X030","X030101N","1er servicio","",""]
n14 = ["X030","X030101N","1er servicio","",""]
n15 = ["X030","X030101N","1er servicio","",""]
n16 = ["X030","X030101N","1er servicio","",""]
n17 = ["X030","X030101N","1er servicio","",""]

n21 = ["X017","X017101N","2do servicio","",""]
n22 = ["X017","X017101N","2do servicio","",""]
n23 = ["X017","X017101N","2do servicio","",""]
n24 = ["X017","X017101N","2do servicio","",""]
n25 = ["X017","X017101N","2do servicio","",""]
n26 = ["X017","X017101N","2do servicio","",""]
n27 = ["X017","X017101N","2do servicio","",""]

n31 = ["X018","X018101N","3er servicio","",""]
n32 = ["X018","X018101N","3er servicio","",""]
n33 = ["X018","X018101N","3er servicio","",""]
n34 = ["X018","X018101N","3er servicio","",""]
n35 = ["X018","X018101N","3er servicio","",""]
n36 = ["X018","X018101N","3er servicio","",""]
n37 = ["X018","X018101N","3er servicio","",""]
# pensar los que solo pagan material

#DIESEL
d11 = ["X030","X0300000","1er servicio","",""]
d12 = ["X030","X0300000","1er servicio","",""]
d13 = ["X030","X0300000","1er servicio","",""]

d21 = ["X20K","X20K0000","2do servicio","",""]
d22 = ["X20K","X20K0000","2do servicio","",""]
d23 = ["X20K","X20K0000","2do servicio","",""]

d31 = ["X30K","X30K0000","3er servicio","",""]
d32 = ["X30K","X30K0000","3er servicio","",""]
d33 = ["X30K","X30K0000","3er servicio","",""]

#AMAROK
a11 = ["X030","X0300000","1er servicio","",""]
a12 = ["X030","X0300000","1er servicio","",""]
a21 = ["X20K","X20K0000","2do servicio","",""]
a21 = ["X20K","X20K0000","2do servicio","",""]
a31 = ["X30K","X30K0000","3er servicio","",""]
a32 = ["X30K","X30K0000","3er servicio","",""]
a41 = ["X40K","X40K0000","4to servicio","",""]
a42 = ["X40K","X40K0000","4to servicio","",""]
a51 = ["X50K","X50K0000","5to servicio","",""]
a52 = ["X50K","X50K0000","5to servicio","",""]

reclamo = ["orden","chasis","recepcion","kilometraje","reparacion",a31]



def reclamar (reclamo):
    time.sleep(3)
    print(reclamo[5])

reclamar(reclamo)





