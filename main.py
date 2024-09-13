from pathlib import Path
from helper.agent import Agent
from helper.document_storage import DocumentStorage




if __name__ == '__main__':
    doc_storage = DocumentStorage()
    output_dir = 'data'
    doc_storage.execute(list(Path(output_dir).glob("**/*")))
    doc_store = doc_storage.get_document_store()

    agent = Agent(doc_store=doc_store)
    print(f"Answer: \n{agent.execute('What is the topic this paper highlights?')}")
