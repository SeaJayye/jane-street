"""
example facts:
    m = 3.28 ft
    ft = 12 in
    hr = 60 min
    min = 60 sec
example queries:
    2 m = ? in      --> answer = 78.72
    13 in = ? m     --> answer = 0.330 (roughly)
    13 in = ? hr    --> "not convertible!"
"""

def convert_m_or_ft(m=-1, ft=-1):
    try:
        m = float(m)
        ft = float(ft)
    except:
        return "not convertible!"
    if m == -1:
        return str(ft * 0.3048) + " m."
    elif ft == -1:
        return str(m * 3.28084) + " ft."
    
if __name__ == "__main__":
    userin = input("""
    What type of unit do you want to convert?
          1. meters to feet
          2. feet to meters
    """)
    if userin == "1":
        usernum = input("How many meters do you want to convert?\n")
        print(convert_m_or_ft(m=usernum))
    elif userin == "2":
        usernum = input("How many feet do you want to convert?\n")
        print(convert_m_or_ft(ft=usernum))
    else:
        print("Invalid selection!")