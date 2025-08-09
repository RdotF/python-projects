import pandas as pd

def analyze_logs(log_file_path):
    #Read the log file
    table = pd.read_csv(log_file_path)

    #Filter for suspicious patterns
    #Many failed attempts indicate brute force, scraping

    failed_attempts = table[table['action'] == 'Deny'] # returns only table[True] (where True is action == Deny)
                                                #capitalization is important

    sus_ip = failed_attempts['internal_ip'].value_counts() # returns Series, where index - IPs, values - quantity of times the IPs are in the table
    #'internal_ip' - the name might be different, look into your csv file

    print('Suspicious IP addresses:')
    print(sus_ip[sus_ip > 1]) # more than 1

if __name__ == '__main__':
    log_file = input('Enter the path to the log:') #firewall_logs_2022.csv
    analyze_logs(log_file)




# EXAMPLE OF THE RETURN
"""
Suspicious IP addresses:
internal_ip
172.28.57.56       2
192.168.138.19     2
192.168.247.52     2
192.168.233.15     2
192.168.12.55      2
192.168.94.207     2
192.168.149.169    2
192.168.186.158    2
192.168.155.238    2
192.168.138.104    2
192.168.12.153     2
192.168.104.75     2
192.168.105.51     2
192.168.134.245    2
192.168.195.161    2 
Name: count, dtype: int64
"""