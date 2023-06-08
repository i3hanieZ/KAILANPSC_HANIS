jenis_komponen = ["MPPF FORM", "CONTROL HORN", "PUSH ROD WIRE", "BRUSHLESS MOTOR", "LINKAGE STOPPER", "ESC(SW5OA)", "RECIEVER (LA10B RX)", "CARBON FIBER ROD", "SERVO", "RC LIPO BATTERY", "PROPELLER", "FLYSKY-I6X REMOTE CONTROL"]
harga_komponen = [23,3,2,15.79,12,67,61,25.30,5.20,57.56,5.50,161]
jumlah = [0,1,2,3,4,5,6,7,8,9,10,11]

print("**********___________________________KEDAI RC JET 5 STAR______________________________**********")
print("CONTROL HORN (RM3=10set)", "PUSH ROD WIRE (RM2=10set)", "LINKAGE STOPPER (RM12=10set)", "CARBON FIBER ROD (RM25.30=16batang)")

print("HARGA MPPF FORM=23, CONTROL HORN=3, PUSH ROD WIRE=2, BRUSHLESS MOTOR=15.79, LINKAGE STOPPER=12, ESC(SW5OA)=67, RECIEVER (LA10B RX)=61, CARBON FIBER ROD=25.30, SERVO=5.20, RC LIPO BATTERY=57.56, PROPELLER=5.50, FLYSKY-I6X REMOTE CONTROL=161")
a=float(input("Masukkan tempahan untuk MPPF FORM:"))
b=float(input("Masukkan tempahan untuk CONTROL HORN:"))
c=float(input("Masukkan tempahan untuk PUSH ROD WIRE:"))
d=float(input("Masukkan tempahan untuk BRUSHLESS MOTOR:"))
e=float(input("Masukkan tempahan untuk LINKAGE STOPPER:"))
f=float(input("Masukkan tempahan untuk ESC (SW5OA):"))
g=float(input("Masukkan tempahan untuk RECIEVER (LA10B RX):"))
h=float(input("Masukkan tempahan untuk CARBON FIBER ROD:"))
i=float(input("Masukkan tempahan untuk SERVO:"))  
j=float(input("Masukkan tempahan untuk RC LIPO BATTERY:"))
k=float(input("Masukkan tempahan untuk PROPELLER:"))
l=float(input("Masukkan tempahan untuk FLYSKY-I6X REMOTE CONTROL:"))

tempahan = [a,b,c,d,e,f,g,h,i,j,k,l]

def jumlah_harga_jenis_komponen():
    for i in range(4):
        jumlah[i] = harga_komponen[i]*tempahan[i]
    return(jumlah)

def cetak():
    print("\n\nTempahan anda ialah:")
    print(a,"komponen", jenis_komponen[0])
    print(b,"komponen", jenis_komponen[1])
    print(c,"komponen", jenis_komponen[2])
    print(d,"komponen", jenis_komponen[3])
    print(e,"komponen", jenis_komponen[4])
    print(f,"komponen", jenis_komponen[5])
    print(g,"komponen", jenis_komponen[6])
    print(h,"komponen", jenis_komponen[7])
    print(i,"komponen", jenis_komponen[8])
    print(j,"komponen", jenis_komponen[9])
    print(k,"komponen", jenis_komponen[10])
    print(l,"komponen", jenis_komponen[11])

    print("\n Jumlah harga untuk tempahan ialah RM",sum (jumlah))
jumlah_harga_jenis_komponen()
cetak()