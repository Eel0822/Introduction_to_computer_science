#統計116 H24126094 李繕安
𝐺=6.67*(10**(-11))
#the gravitational constant
c=299792458
#the speed of light
force=float(input("Input the force: "))
#input the force and turn it into float
mass_m1=float(input("Input the mass of m1: "))
#input mass1 and turn it into float
distance=float(input("Input the distance: "))
#input distance and turn it into float
mass_m2=force*(distance**2)/(mass_m1*G)
#culculate mass2
energy_m2=mass_m2*(int(c)**2)
#culculate energy of mass2
print("The mass of m2=" , mass_m2)
print("The energy of m2=" , energy_m2)
#print the result