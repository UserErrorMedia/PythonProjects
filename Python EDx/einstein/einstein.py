# Testing E=mc2
speed_of_light = 300000000
c = speed_of_light

def energy(m):
    E = m * c ** 2
    return E

# Define main function
def main():
# Prompt user for "m" in kilograms
    m = int(input("What is the mass in kilograms? "))
# Calculate the energy equivalent
    E = energy(m)
    print(f"{E:,}")

if __name__ == "__main__":
    main()