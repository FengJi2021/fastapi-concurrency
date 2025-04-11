# Load Test to verify the impact of sleep function in FastAPI

## How to run

1. Clone the repository

2. Setup the environment

```bash
# install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# create virtual environment
uv venv
uv install

```

3. Run the FastAPI app

```bash
uv run uvicorn src.main:app

# in a separate terminal run load test

uv run locust -f test/locustfile.py
```

4. Open the Locust web interface and run the test