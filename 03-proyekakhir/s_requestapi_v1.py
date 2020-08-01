import requests

def get_respon1(): 
    response = requests.get("http://10.33.109.242:5000/connections")
    return response.json()
def get_respon1_delete():
    response = requests.get("http://10.33.109.242:5000/connections/delete")
    return response.json()

def get_respon2():
    response = requests.get("http://10.33.109.242:5000/logins")
    return response.json()
def get_respon2_delete():
    response = requests.get("http://10.33.109.242:5000/logins/delete")
    return response.json()

def get_respon3():
    response = requests.get("http://10.33.109.242:5000/dcerpcrequests")
    return response.json()
    
def get_respon3_delete():
    response = requests.get("http://10.33.109.242:5000/dcerpcrequests/delete")
    return response.json()

def get_respon4():
    response = requests.get("http://10.33.109.242:5000/dcerpcbinds")
    return response.json()
def get_respon4_delete():
    response = requests.get("http://10.33.109.242:5000/dcerpcbinds/delete")
    return response.json()

def get_respon5():
    response = requests.get("http://10.33.109.242:5000/offers")
    return response.json()
def get_respon5_delete():
    response = requests.get("http://10.33.109.242:5000/offers/delete")
    return response.json()

def get_respon6():
    response = requests.get("http://10.33.109.242:5000/downloads")
    return response.json()
def get_respon6_delete():
    response = requests.get("http://10.33.109.242:5000/downloads/delete")
    return response.json()

def get_respon7():
    response = requests.get("http://10.33.109.242:5000/mssql_commands")
    return response.json()
def get_respon7_delete():
    response = requests.get("http://10.33.109.242:5000/mssql_commands/delete")
    return response.json()

def get_respon8():
    response = requests.get("http://10.33.109.242:5000/mssql_fingerprints")
    return response.json()
def get_respon8_delete():
    response = requests.get("http://10.33.109.242:5000/mssql_fingerprints/delete")
    return response.json()

def get_respon9():
    response = requests.get("http://10.33.109.242:5000/mysql_commands")
    return response.json()
def get_respon9_delete():
    response = requests.get("http://10.33.109.242:5000/mysql_commands/delete")
    return response.json()

def get_respon10():
    response = requests.get("http://10.33.109.242:5000/mysql_command_args")
    return response.json()
def get_respon10_delete():
    response = requests.get("http://10.33.109.242:5000/mysql_command_args/delete")
    return response.json()

def get_respon11():
    response = requests.get("http://10.33.109.242:5000/mysql_command_ops")
    return response.json()
def get_respon11_delete():
    response = requests.get("http://10.33.109.242:5000/mysql_command_ops/delete")
    return response.json()





  


