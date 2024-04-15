import requests
import json


url_type = str(input("url_type:"))
 
value1 = str(input("value1:"))
value2 = str(input("value2:"))
value3 = str(input("value3:"))


# Gönderilecek JSON verisi
data = {
    "{name}": f"{value1}",
    "{score}": f"{value2}",
    "{player_id}": f"{value3}",
}

# Hedef URL
url = f"http://127.0.0.1/api/{url_type}"

# JSON verisini POST isteği olarak gönderme
response = requests.post(url, json=data)

# Sunucudan gelen yanıtı kontrol etme
if response.status_code == 200:
    print("İstek başarılı oldu!")
    print("Sunucu yanıtı:", response.json())
else:
    print("İstek başarısız oldu! Hata kodu:", response.status_code)