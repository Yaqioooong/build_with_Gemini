import requests
import json


def requestGemini():
    proxies = {
        'http': 'http://127.0.0.1:6969',
        'https': 'http://127.0.0.1:6969',
    }
    headers = {
        'Content-Type': 'application/json',
    }
    params = {
        'key': 'YOUR_GEMINI_API_KEY!',
    }
    json_data = {
        'contents': [
            {
                'parts': [
                    {
                        'text': 'generate a random word in Chinese ans English respectively',
                    },
                ],
            },
        ],
    }
    response = requests.post(
        'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent',
        params=params,
        headers=headers,
        json=json_data,
        proxies=proxies
    )
    return response


requestGemini()

if __name__ == '__main__':
    response = requestGemini()
    response.encoding="utf-8"
    jsonStr = response.text
    print(jsonStr)
    jsonData = json.loads(jsonStr)
    res = jsonData['candidates'][0]['content']['parts'][0]['text']
    print(res)

