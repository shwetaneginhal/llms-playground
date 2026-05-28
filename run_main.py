
import os
from ingest import load_faq_data, build_index
from rag_helper import RAGBase
import openai



documents = load_faq_data()
index = build_index(documents)

github_token = os.environ.get("GITHUB_LLM_TOKEN")

client = openai.OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=github_token
)

assistant = RAGBase(index = index, llm_client = client, course = 'llm-zoomcamp')

#answer = assistant.rag('I just discovered the course. Can I join now?')
#print(answer)

answer1 = assistant.rag('Can I still join the course after it started?')
print(answer1)

