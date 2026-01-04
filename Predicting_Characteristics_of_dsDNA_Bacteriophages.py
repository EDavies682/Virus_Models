# Jover et al. (2014)

import math

print("This code is designed to predict the characteristics of nonlipid_containing dsDNA bacteriophages")

# constants

c = 2.0 # +- 0.2

# the fraction of volume within a capsid taken up by the phage genome
fill = 0.51 # +- 0.04

# capsid thickness (nm)
h = 2.5

# volume of a base pair (nm3)
v_bp = 1.07

# volume of a single capsid protein (nm)
v_pr = 47

def known_values():
    global n_bp, r, v_ic, r_c, n_pr, v_c, v_pr, virus_name
    
    virus_name = input("Enter the name of the virus (or press enter for unknown): ")
    i_n_bp = input("Enter the number of base pairs (or press enter for unknown): ")
    i_r = input("Enter the internal radius (nm) (or press enter for unknown): ")
    i_r_c = input("Enter the external radius (nm) (or press enter for unknown): ")
    i_v_ic = input("Enter the volume inside the capsid (or press enter for unknown): ")
    i_n_pr = input("Enter the number of proteins (or press enter for unknown): ")
    i_v_c = input("Enter the volume of the capsid (or press enter for unknown): ")
    i_v_pr = input("Enter the average volume of capsid proteins (or press enter for unknown): ")

    # Convert to floats
    n_bp = float(i_n_bp) if i_n_bp != "" else ""
    r = float(i_r) if i_r != "" else ""
    r_c = float(i_r_c) if i_r_c != "" else ""
    v_ic = float(i_v_ic) if i_v_ic != "" else ""
    n_pr = float(i_n_pr) if i_n_pr != "" else ""
    v_c = float(i_v_c) if i_v_c != "" else ""
    if i_v_pr != "":
        v_pr = float(i_v_pr)

def find_n_np():
    global n_bp, r, v_ic, r_c, n_pr, v_c
    if n_bp != "":
        n_bp = n_bp
    elif r != "":
        n_bp = c * r**3
    elif v_ic != "":
        n_bp = fill * (v_ic / v_bp)
    elif r_c != "" :
        n_bp = ((4 * math.pi) / (3 * v_bp)) * (r_c - h)**3

        
def find_r():
    global n_bp, r, v_ic, r_c, n_pr, v_c
    if r != "":
        r = r
    elif r_c != "":
        r = r_c - h
    elif n_bp != "":
            r = math.cbrt(n_bp / c)

        
def find_r_c():
    global n_bp, r, v_ic, r_c, n_pr, v_c
    if r_c != "":
        r_c = r_c
    elif r != "":
        r_c = r + h
    elif n_bp != "":
            r = math.sqrt(n_bp / c)
    elif n_pr != "":
        r_c = v_pr * n_pr
    
def find_v_ic():
    global n_bp, r, v_ic, r_c, n_pr, v_c
    if v_ic != "":
        v_ic = v_ic
    elif n_bp != "":
        v_ic = (n_bp / fill) * v_bp

def find_n_pr():
    global n_bp, r, v_ic, r_c, n_pr, v_c
    if n_pr != "":
        n_pr = n_pr
    elif r_c != "":
        n_pr = ((4 * math.pi) / (3 * v_pr)) * (3 * r_c**2 * h - 3 * h**2 * r_c + h**3)
    elif v_c != "":
        n_pr = v_c / v_pr
        
def find_v_c():
    global n_bp, r, v_ic, r_c, n_pr, v_c
    if v_c != "":
        v_c = v_c
    elif n_pr != "":
        v_c = n_pr * v_pr
    elif r_c != "":
        v_c = ((4 * math.pi) / (3 * v_pr) * (3 * r_c**2 * h - 3 * h**2 * r_c + h**3)) * v_pr


 
known_values()
if n_bp == "" and r == "" and r_c == "" and v_ic == "" and n_pr == "":
    print("Please input at least one value")
    known_values()
else:
    n = 0
    while n_bp == "" or r == "" or r_c == "" or v_ic == "" or n_pr == "" and n < 20:
        n += 1
        find_n_np()
        find_r()
        find_r_c()
        find_v_ic()
        find_n_pr()
        find_v_c()
        
print(n)
if virus_name == "":
    print("Unknown Virus")
else:
    print(virus_name)

if n_bp == "":
    print("Not enough data to predict the number of base pairs")
else:
    print(f"Number of base pairs: {n_bp:.2f}")

if r == "":
    print("Not enough data to predict the internal radius")
else:
    print(f"Internal radius: {r:.2f} nm")

if r_c == "":
    print("Not enough data to predict the external radius")
else:
    print(f"External radius: {r_c:.2f} nm")

if v_ic == "":
    print("Not enough data to predict the volume inside the capsid")
else:
    print(f"Volume inside the capsid: {v_ic:.2f}nm3")

if n_pr == "":
    print("Not enough data to predict the number of proteins making up the capsid")
else:
    print(f"Number of proteins making up the capsid: {n_pr:.2f}")

if v_c == "":
    print("Not enough data to predict the volume of the capsid")
else:
    print(f"Volume of the capsid: {v_c:.2f} nm3")

 
    

        













    
