import requests
import hashlib

class UCM:
    
    def __init__(self, url, port, username, password) -> None:
        self.Ucmurl = url
        self.Ucmport = port
        self.Ucmusername = username
        self.Ucmpassword = password
        self.cookie = ''


    def getChallenge(self):
        x = requests.get(self.Ucmurl + ":" + self.Ucmport + "/api?action=challenge&user=" + self.Ucmusername + "&version=1.0", verify=False)
        jsonResponse = x.json()
        challenge = jsonResponse['response']['challenge']
        print(challenge)
        response = self.ucmLogin(challenge)
        respCookie = response.json()
        self.cookie = respCookie['response']['cookie']
        return self.cookie

    def ucmLogin(self, challenge):
        tokenString = challenge + self.Ucmpassword
        token = hashlib.md5(tokenString.encode())
        x = requests.get(self.Ucmurl + ":" + self.Ucmport + "/api?action=login&token=" + str(token.hexdigest()) + "&url=" + self.Ucmurl + ":" + self.Ucmport + "&user=" + self.Ucmusername, verify=False)
        return x


    def getSystemStatus(self):
        x = requests.get(self.Ucmurl + ":" + self.Ucmport + "/api?action=getSystemStatus&cookie=" + self.cookie, verify=False)
        jsonResponse = x.json()
        return(jsonResponse)
    
    def getSystemGeneralStatus(self):
        x = requests.get(self.Ucmurl + ":" + self.Ucmport + "/api?action=getSystemGeneralStatus&cookie=" + self.cookie, verify=False)
        jsonResponse = x.json()
        return(jsonResponse)
    
    def listAccounts(self):
        x = requests.get(self.Ucmurl + ":" + self.Ucmport + "/api?action=listAccount&cookie=" + self.cookie, verify=False)
        jsonResponse = x.json()
        return(jsonResponse)


    def getSipAccount(self, ext_number):
        x = requests.get(self.Ucmurl + ":" + self.Ucmport + "/api?action=getSipAccount&cookie=" + self.cookie + "&extension=" + ext_number, verify=False)
        jsonResponse = x.json()
        return(jsonResponse)
    
    def updateSipAccount(self, ext_number, user_pass):
        x = requests.get(self.Ucmurl + ":" + self.Ucmport + "/api?action=updateSipAccount&cookie=" + self.cookie + "&extension=" + ext_number + "&password=" + user_pass, verify=False)
        jsonResponse = x.json()
        return(jsonResponse)
    
    def listVoIPTrunk(self):
        x = requests.get(self.Ucmurl + ":" + self.Ucmport + "/api?action=listVoIPTrunk&cookie=" + self.cookie, verify=False)
        jsonResponse = x.json()
        return(jsonResponse)
    
    def getSIPTrunk(self, trunk):
        x = requests.get(self.Ucmurl + ":" + self.Ucmport + "/api?action=getSIPTrunk&cookie=" + self.cookie + "&trunk=" + trunk, verify=False)
        jsonResponse = x.json()
        return(jsonResponse)
    
    def updateSIPTrunk(self, trunk):
        x = requests.get(self.Ucmurl + ":" + self.Ucmport + "/api?action=updateSIPTrunk&cookie=" + self.cookie + "&trunk=" + trunk, verify=False)
        jsonResponse = x.json()
        return(jsonResponse)
    
    def deleteSIPTrunk(self, trunk):
        x = requests.get(self.Ucmurl + ":" + self.Ucmport + "/api?action=deleteSIPTrunk&cookie=" + self.cookie + "&trunk=" + trunk, verify=False)
        jsonResponse = x.json()
        return(jsonResponse)
    
    def listAnalogTrunk(self):
        x = requests.get(self.Ucmurl + ":" + self.Ucmport + "/api?action=listAnalogTrunk&cookie=" + self.cookie, verify=False)
        jsonResponse = x.json()
        return(jsonResponse)
    
    def addAnalogTrunk(self, trunkName, channels, trunkGroup):
        x = requests.get(self.Ucmurl + ":" + self.Ucmport + "/api?action=addAnalogTrunk&cookie=" + self.cookie + "&trunk_name=" + trunkName + "&chans=" + channels + "&trunkgroup=" + trunkGroup, verify=False)
        jsonResponse = x.json()
        return(jsonResponse)
    
    def getAnalogTrunk(self, trunkNum):
        x = requests.get(self.Ucmurl + ":" + self.Ucmport + "/api?action=getAnalogTrunk&cookie=" + self.cookie + "&analogtrunk=" + trunkNum, verify=False)
        jsonResponse = x.json()
        return(jsonResponse)
    
    def updateAnalogTrunk(self, trunkIndex):
        x = requests.get(self.Ucmurl + ":" + self.Ucmport + "/api?action=updateAnalogTrunk&cookie=" + self.cookie + "&trunk_index=" + trunkIndex, verify=False)
        jsonResponse = x.json()
        return(jsonResponse)
    
    def deleteAnalogTrunk(self, trunkNum):
        x = requests.get(self.Ucmurl + ":" + self.Ucmport + "/api?action=deleteAnalogTrunk&cookie=" + self.cookie + "&analogtrunk=" + trunkNum, verify=False)
        jsonResponse = x.json()
        return(jsonResponse)
    
    def addSLATrunk(self, trunkName):
        x = requests.get(self.Ucmurl + ":" + self.Ucmport + "/api?action=addSLATrunk&cookie=" + self.cookie + "&trunk_name=" + trunkName, verify=False)
        jsonResponse = x.json()
        return(jsonResponse)


    #       Apply Changes
    def ApplyChanges(self):
        x = requests.get(self.Ucmurl + ":" + self.Ucmport + "/api?action=applyChanges&cookie=" + self.cookie, verify=False)
        jsonResponse = x.json()
        return(jsonResponse)