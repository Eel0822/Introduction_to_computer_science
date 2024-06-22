#統計116 H24126094 李繕安
g=9.8
H_1st_ball=float(input("Input the height of the 1st ball: "))
mass1=float(input("Input the mass of the 1st ball: "))
mass2=float(input("Input the mass of the 2nd ball: "))
E1=mass1*g*H_1st_ball
V1_after_slide=(2*E1/mass1)**(1/2)
V2_after_collision=(mass1*((V1_after_slide)**2)/mass2)**(1/2)
print("The velocityb of the 1st ball after slide: ", V1_after_slide ,"m/s")
print("The velocityb of the 2nd ball after collision:", V2_after_collision ,"m/s")