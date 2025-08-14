# Various Python Scripts for Automation
____
# 1. Networking | Vulnerabilities </br>
## Port Scanner </br>
Script automates the task of finding open ports</br>
</br>
The programm takes __two__ parameters: </br>
> url </br>
> number of ports (100 means 0-100) </br>
<!-- -->
</br>
Returns the list of open ports </br>
Integrated progressbar for terminal </br>

## SQL-injection-tester </br>
Has a pre-determined list of payloads </br>
</br>
__DOES NOT inject url__ </br>
Injections are targeted at __forms__ (POST requests) </br>
</br>
The programm takes __one__ parameter: 
>url

## Web-Scrapper
Script finds all nested links. Provided url acts as a root <br/>
</br>
Scrapes all the links on the page and then filters them </br>
The programm writes found links in file **nestedLinks.txt**  </br>
</br>
It takes __one__ parameter: </br>
> url
<!-- -->
Returns filtered nested links in the console 
# 2. Automation
## Log-analysis
Reads provided csv file with logs</br>
</br>
Filters on the columns of the table and then analyses filtered data on the condition</br>
Here, script looks for suspicious IP-addresses from the firewall log</br>
</br>
The programm takes __one__ parameter:</br>
> path to the log
<!-- -->
Returns the list of the suspicious IP-addresses
## Password-manager
The script uses symmetric cryptography to store passwords in json format</br>
</br>
The programm has four commands: show services, get password, save password, delete service.</br>
</br>
Secret key must be created before hashing </br>
```python create-secret-key.py```
<!-- -->
Then the programm can be run and new services created. Pairs of service-password are stored in passwords.json</br>
WIth secret key the programm restores password from hashed string </br>
