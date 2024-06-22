#統計116 H24126094 李繕安
c=299792458
velocity=float(input("Input velocity: "))
percentage=velocity/c
print("percentage of light speed" , percentage )
r=1/((1-((velocity**2)/(c**2)))**(1/2))
Alpha_Centauri=4.3
Barnards_Star=6.0
Betelgeuse=309
Andromeda=2000000
Alpha_Centauri_T=round(Alpha_Centauri/r,6)
Barnards_Star_T=round(Barnards_Star/r,6)
Betelgeuse_T=round(Betelgeuse/r,6)
Andromeda_T=round(Andromeda/r,6)
print("Travel time to Alpha Centauri = ", Alpha_Centauri_T)
print("Travel time to Barnard's Star = ", Barnards_Star_T)
print("Travel time to Betelgeuse (in the Milky way) = ", Betelgeuse_T)
print("Travel time to Andromeda Galaxy (closest galaxy) = ", Andromeda_T)