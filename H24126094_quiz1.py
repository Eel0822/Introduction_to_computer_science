Richter=float(input("Please input a Richter scale value: "))
#輸入地震規模
print("Richter scale value: ", Richter)
#印出地震規模
energy=round(10**(1.5*Richter+4.8),5)
#計算能量並四捨五入到小數點後五位
print("Equivalence in Joules: ", energy)
#印出能量
TNT=round(energy/(4.184*(10**9)),5)
#計算能量相當於幾個炸彈並四捨五入到小數點後五位
print("Equivalence in ton of TNT: ", TNT)
#印出能量相當於幾個炸彈
lunch=round(energy/2930200,5)
#計算能量相當於幾頓營養午餐並四捨五入到小數點後五位
print("Equivalence in the number of nutritious lunches: ",lunch)
#印出能量相當於幾頓營養午餐