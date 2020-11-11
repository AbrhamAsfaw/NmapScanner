import os
import subprocess # module to execute nmap commands          # ABRHAM ASFAW   ATE_5110_09


def mainMenu():
    print("."*80)
    print("\t\t\t       NMAP SCANNER")
    print("."*80)
    print()
    print("\t\t\t1---> Port Discovery")
    print("\t\t\t2---> Port In Range Discovery")
    print("\t\t\t3---> Host Discovery")
    print("\t\t\t4---> Os Discovery")
    print("\t\t\t5---> Clear Terminal")
    print("\t\t\t6---> Quit Scanner")

    print()
    choice = int(input("Choose Scan Option : "))
    if choice == 1:
        Port_Discovery()
        mainMenu()
    elif choice ==2:
        Port_DiscoveryInRange()
        mainMenu()
    elif choice == 3:
        Host_Discovery()
        mainMenu()
    elif choice == 4:
        Os_Discovery()
        mainMenu()
    elif choice == 5:
        clear()
        mainMenu()
    elif choice == 6:
        clear()
        quit_Scanner()
    else:
        print("Invalid Choice :( ")
        mainMenu()

# port Discovery
def Port_Discovery():
    port = input("[*]Please Enter Host Address To Scan : ")
    print("."*80)
    subprocess.check_call(['nmap','-n','-v','-Pn','-sV','-oN','Port_Discovery.txt', port])
    print("."*80)

# port Discovery In Range
def Port_DiscoveryInRange():
    port_range = input("[*]Please Enter Host Address To Scan : ")
    print("."*80)
    subprocess.check_call(['nmap','-p','1-100','-oN','Port_DiscoveryInRange.txt', port_range])
    print("."*80)

# Host Discovery
def Host_Discovery():
    host = input("[*]Please Enter Host Address To Scan : ")
    print("."*80)
    subprocess.check_call(['nmap','-n','-v','Pn','-sn','-sL','-PE','-PP','-oN','Host_Discovery.txt', host])
    print("."*80)

# OS Discovery
def Os_Discovery():
    os = input("[*]Please Enter Host Address To Scan : ")
    print("."*80)
    subprocess.check_call(['nmap','-n','-F','-A','-Pn','-sS','-O','-oN','Os_Discovery.txt', os])
    print("."*80)

#clear Terminal
def clear():
    os.system('cls||clear')

#Quit Scanner
def quit_Scanner():
    quit()


if __name__ == "__main__":
    mainMenu()