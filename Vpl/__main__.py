from vpl import vpl
import sys

def main():
    while True:
        vpl()
        opt = str(input("Deseja realizar outra operação(s/n)? "))
        if opt.lower() == "n":
            break

if __name__ == "__main__":
    main()
    sys.exit(0)
    
