import os
from dotenv import load_dotenv
import json
from urllib.request import Request
from types import SimpleNamespace


load_dotenv()
api_key = os.environ.get("PRACTICE_API_KEY")
if not api_key:
    print("Set PRACTICE_API_KEY first")
else:
    print("Practice key loaded")

body = {
    "model": "practice-model",
    "max_tokens": 100,
    "messages": [{
        "role": "user",
        "content": "Explain Python lists"
    }]
}

print(body["messages"][0]["content"])

request_text = json.dumps(body)
print(request_text)
print(type(request_text))

parsed_body = json.loads(request_text)
print(type(parsed_body))
print(parsed_body["messages"][0]["content"])

request = Request(
    url="https://example.com/practice",
    data=request_text.encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST",
)

print(request.get_method())
print(request.full_url)
print(request.data.decode("utf-8"))

response_text = '''{
  "content": [{"type": "text", "text": "A Python list stores an ordered collection of items."}],
  "usage": {"input_tokens": 12, "output_tokens": 11}
}'''

result = json.loads(response_text)
print(result["content"][0]["text"])

sdk_response = SimpleNamespace(
    content=[
        SimpleNamespace(type="text", text=result["content"][0]["text"])
    ]
)

print(sdk_response.content[0].text)