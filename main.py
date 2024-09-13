import sys
from pathlib import Path
from helper.agent import Agent
from helper.document_storage import DocumentStorage


if __name__ == "__main__":
    cli_mode = False

    if len(sys.argv) >= 3 and sys.argv[1] == "--question":
        question = sys.argv[2]
        print(f"User: {question}")
    else:
        print("Entering CLI mode, use [:q] to exit.")
        question = input("User: ")
        cli_mode = True

    doc_storage = DocumentStorage()
    output_dir = "data"
    doc_storage.execute(list(Path(output_dir).glob("**/*")))
    doc_store = doc_storage.get_document_store()

    agent = Agent(doc_store=doc_store)
    while True:
        print(f"ChatBot: \n{agent.execute(question)}")
        if cli_mode:
            question = input("User: ")
            if question == ":q":
                print("ChatBot: Thank you & Have a nice day!")
                break

        else:
            break
