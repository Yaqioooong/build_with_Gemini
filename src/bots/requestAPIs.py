import json
import requests
import os
# 请求Gemini
def requestGemini():
    proxies = {
        'http': 'http://127.0.0.1:6969',
        'https': 'https://127.0.0.1:6969',
    }
    headers = {
        'Content-Type': 'application/json',
    }
    params = {
        # 此处填写GEMINI API KEY
        'key': os.environ['KEY_GEMINI']
    }
    json_data = {
        'contents': [
            {
                'parts': [
                    {
                        'text': '随机生成一个中文词汇和英文单词，并分别对其进行解释。',
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
    jsonStr = response.text
    jsonData = json.loads(jsonStr)
    res = jsonData['candidates'][0]['content']['parts'][0]['text']
    return res