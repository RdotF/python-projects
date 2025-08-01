import socket, time


def progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=40, fill='█', printEnd='\r'):

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)

    if iteration == total:
        print()
def scan_ports(target, n):
    open_ports = []
    for port in range(1, n):

        #Creating socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Specifying INTERNET communication TCP type

        #Progress bar
        #Works in terminals. Carriage return isn't shown in consoles
        progress_bar(port, n-1)
        time.sleep(0.1)

        sock.settimeout(1) # 1 sec to set the connection
        result = sock.connect_ex((target, port)) # set the connection without Exception in case of error
        if result == 0: # if 0 - connection established
            open_ports.append(port)
        sock.close() # free the resources
    return open_ports

def check_ip(target):
    try:
        socket.inet_aton(target)
        return True
    except OSError:
        try:
            socket.gethostbyname(target)
            return True
        except socket.gaierror:
            return False

if __name__ == "__main__":
    target = input("Enter the target IP address: ")
    if not check_ip(target):
        print('INVALID INPUT. Example of valid input: 192.168.0.3 / google.com')
        exit(1)

    n = int(input("Enter the number of ports to be scanned (e.g. 100): "))
    print("Scanning ports...")
    print(f'\nOpen ports for {target} are: {scan_ports(target, n)}')

