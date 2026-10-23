# Lesson 04: APIs & Keys

Date: 2026-10-23

## What I practised

I used a fake key and local simulated responses. I prepared an HTTP request but did not send it. I did not use a real provider SDK or make a paid API call.

My practice code is in [apis_setup.py](apis_setup.py).

## How an API call works

An API gives programs a defined way to communicate with a service.

| Part | Purpose |
|------|---------|
| Endpoint | The URL receiving the request |
| API key | A credential that authorizes access to the service |
| Headers | Information about the request, such as authentication and body format |
| Request body | The task and settings sent to the service |
| Response body | The result returned by the service |

Changing the question changes the request body. It does not require changing the API key.

## Loading a key

An environment variable is a named value available to a process. For practice:

```bash
export PRACTICE_API_KEY="practice-only-123"
```

Python can read it with `os.environ`. Direct access raises `KeyError` when the variable is missing:

```python
api_key = os.environ["PRACTICE_API_KEY"]
```

Using `.get()` returns `None` when the variable is missing, allowing my code to handle it:

```python
api_key = os.environ.get("PRACTICE_API_KEY")
if not api_key:
    print("Set PRACTICE_API_KEY first")
else:
    print("Practice key loaded")
```

This checks whether the value is nonempty. It does not verify that a provider accepts the key.

## Using a .env file

A `.env` file can hold local settings, including credentials. Python does not load it automatically.

```bash
uv pip install python-dotenv
```

```python
from dotenv import load_dotenv

load_dotenv()
```

`load_dotenv()` loads values into the Python process's environment. My code then reads them with `os.environ.get()`.

Add `.env` to `.gitignore` to help prevent accidental commits. I checked the ignore rule with:

```bash
git check-ignore .env
```

The output was `.env`. Ignore rules do not remove a file that Git already tracks. Keep real credentials out of source code and notes.

## Dictionaries, JSON, and bytes

| Expression | Result |
|------------|--------|
| `json.dumps(body)` | Converts a Python dictionary into JSON text (`str`) |
| `json.loads(response_text)` | Parses JSON text into Python values; a JSON object becomes a `dict` |
| `request_text.encode("utf-8")` | Converts text into bytes |
| `request.data.decode("utf-8")` | Converts stored request bytes back into text |

I accessed the instruction in my request dictionary with:

```python
body["messages"][0]["content"]
```

Read this as: get the messages list, select its first item, then get its content.

## Preparing an HTTP request

```python
request = Request(
    url="https://example.com/practice",
    data=request_text.encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST",
)
```

Creating a `Request` only prepares it. Sending it requires another operation, such as `urlopen(request)`. The example URL and practice model are placeholders.

`Content-Type: application/json` describes the body format. It does not authenticate the request. In the lesson's Anthropic example, the API key is carried in the `x-api-key` header. Authentication headers depend on the provider.

## Reading responses and understanding SDKs

After parsing my simulated JSON response, I extracted the answer with:

```python
result["content"][0]["text"]
```

An SDK is a provider's programming library. It can handle JSON conversion, HTTP requests, and response objects. The exact interface depends on the SDK.

I used `SimpleNamespace` to simulate an object response:

```python
sdk_response.content[0].text
```

Dictionary keys use brackets, such as `["content"]`. Object attributes use dots, such as `.content`. Both examples use `[0]` to select the first list item. `SimpleNamespace` itself does not call an API.

## Common errors

| Error | Meaning | Response |
|-------|---------|----------|
| `KeyError` when reading an environment variable | The variable is missing | Set it or handle the missing value with `.get()` |
| HTTP 401 | Authentication failed | Check the credential and required authentication header |
| HTTP 429 | Commonly indicates a rate limit | Wait before retrying; follow the provider's retry guidance |

Changing the prompt does not fix invalid credentials. Retrying immediately in a tight loop can keep exceeding a rate limit.

## Package installation correction

I tried `python -m uv install -r requirements.txt` and got `No module named uv`. I learned to use the available `uv` command directly:

```bash
uv pip install -r requirements.txt
```

The `os`, `json`, `urllib.request`, and `types` modules come with Python. `python-dotenv` is an additional package.

## Quiz and reflection

- First attempt: **2/3**. I confused `Content-Type` with the authentication header.
- Retake: **3/3**. I correctly recalled local key storage, Anthropic's `x-api-key` header, and waiting after HTTP 429.
- Object attribute access was initially confusing. Reading `.content[0].text` one step at a time helped.
- Real HTTP calls and a real provider SDK remain future practice; this lesson used local simulation.

Next lesson: **Jupyter Notebooks**.
