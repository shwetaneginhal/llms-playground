# LLM projects with RAG, Vector Search and Agents

My version of building LLM projects using **RAG (Retrieval-Augmented Generation)**, **Vector Search**, **Agents** and other AI Engineering stuffs. 

This repo contains projects from the [DataTalksClub LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp).

---

## Key Modifications

Instead of using the OpenAI API as directed in the Zoomcamp, in this space I have used LLMs hosted by GitHub and Microsoft Azure. 

GitHub provides access to top-tier models including:

* `Llama-3.3-70B-Instruct`
* `GPT-4o` / `GPT-4o-mini`
* `Mistral-Large`
* `DeepSeek-R1`

---

## Sections:

* **RAG:** RAG pipeline for an FAQ dataset. Used two types of searches: minsearch (similar to Elasticsearch) and SQLite search. The former one has to be loaded for every restart and is in-memory. The later one is loaded once (eg. faq.db) and this separates ingestion from querying. 

### Setting up the GitHub Token for LLM Access

Follow these steps to securely configure your environment and access the GitHub-hosted models:

1. **Generate a Token:** Get a classic PAT (Personal Access Token) from your GitHub account developer settings.
2. **Secure the Token:** Save it in a `.env` file or another secure location on your local machine. 
   > **Note:** Never hard-code your GitHub token directly into Python scripts or commit it to version control.
3. **Get it running:** Simply run the following command in your terminal before executing the project scripts:

```bash
export GITHUB_LLM_TOKEN="your_token_here"