from UCM import UCM
import json

from bs4 import BeautifulSoup as bs
import requests

url = "{UCM url}"
port = "str({UCM port})"
Username = "APIUsername"
Password = "APIPassword"

extensionNumber = "1000"
extensionSIPPass = "<>9dhj7H7d8"

ucm1 = UCM(url, port, Username, Password)

#       Get challenge and Login
x = ucm1.getChallenge()
print(x)
#       List all Accounts
listAct = ucm1.listAccounts()
print(json.dumps(listAct, indent=2))
#       List single SIP account
listSipExt = ucm1.getSipAccount(extensionNumber)
print(json.dumps(listSipExt, indent=2))
#       Update SIP account
updtAct = ucm1.updateSipAccount(extensionNumber, extensionSIPPass)
print(json.dumps(updtAct, indent=2))

#       Apply changes
applychng = ucm1.ApplyChanges()
print(json.dumps(applychng, indent=2))
