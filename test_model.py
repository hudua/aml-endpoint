import requests
import json

url = "https://maplehack2.canadacentral.inference.ml.azure.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 5IFsKwOwX6FjOpkQgg0Wol3AfRmR6MI24w5U4E445Mu9IZvVA6aQJQQJ99BBAAAAAAAAAAAAINFRAZMLNXQP"
}
data = {
    "model": "microsoft/Phi-3-mini-4k-instruct",
    "messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
