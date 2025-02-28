import requests

url = "https://vllm-hf-2.canadaeast.inference.ml.azure.com/"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer xxxxxxxxxxxx"
}
data = {
    "model": "Noumaan/phi3-mini-128k-instruct-4bit-quantized",
    "prompt": "San Francisco is a",
    "max_tokens": 200,
    "temperature": 0.7
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
