import os
import time
from redis import Redis
from rq import Queue, Worker

redis = Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)
queue = Queue("summaries", connection=redis)

def anonymize(text: str) -> str:
    # Placeholder anonymization
    return text.replace("Name", "[REDACTED]")

def call_llm(text: str) -> str:
    # Simulate call to LLM like OpenAI
    return f"Summary: {text[:50]}..."

def process_job(job):
    payload = job.args[0]
    anon = anonymize(payload["text"])
    summary = call_llm(anon)
    return {"summary": summary}

if __name__ == "__main__":
    worker = Worker([queue])
    worker.work()
