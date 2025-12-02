#Data


print(" choose a formula")
print("a = kinetic energy (KE = 0.5*M*V^20)")
print("b = force ( F = m*a)")
print("c = ohm's law (v = I*R)")
print("d = speed (S = D/t)")
print("e = potential energy (PE = m*g*h)")


choice = input("Enter a, b, c, d, or e")

if choice == "a":
    m = float(input("Mass m: "))
    v = float(input("Velocity v :" ))
    KE = 0.5*m*v**2
    print("Kinetic Energy =" , KE)

elif choice == "b":
    m = float(input("Mass m : "))
    a = float(input("Acceleration a : "))
    f = m*a
    print(" force =", f)

elif choice == "c":
    v = float(input("Voltage v : "))
    i = float(input(" Current I : "))
    r = float(input("Resistance R  : "))
    v = i*r
    print(" ohm's law =", v)

elif choice == "d":
    s = float(input("speed s : "))
    d = float(input(" distance d : "))
    t = float(input("time t  : "))
    s = d/t
    print(" speed =", s)

elif choice == "e":
    m = float(input("Mass m : "))
    h = float(input(" height h: "))
    g = 9.81
    PE = m*g*h
    print(" potential Energy =", PE)

else:
     print("choice not found, pick again")

















