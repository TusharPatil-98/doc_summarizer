[![ML Application test with Github Actions](https://github.com/TusharPatil-98/doc_summarizer/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/TusharPatil-98/doc_summarizer/actions/workflows/pythonapp.yml)
# Document Summarizer with Haystack

The **Document Summarizer** is a Python-based tool that allows you to generate concise summaries from longer texts or documents. Whether you're dealing with research papers, articles, or even lengthy emails, this tool can help you extract the essential information efficiently.

## Features

- **Text Summarization**: Given a document, the summarizer extracts key sentences or phrases to create a shorter summary using Haystack.
- **Interactive Mode**: Run the summarizer in interactive mode, where you can input questions or prompts to generate relevant summaries.
- **Easy Setup**: Just follow the steps below to get started!

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/TusharPatil-98/doc_summarizer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd doc_summarizer
   ```

3. Install the required Python packages and run project:

   ```bash
   make all
   ```

## Usage

1. Place your documents (in pdf, markdown or plain text format) inside the `data` folder.

2. Run the summarizer using the following commands:

   - To summarize a specific document:

     ```bash
     python main.py --question "What is the main idea of this article?"
     ```

   - To run in interactive mode (where you input questions):

     ```bash
     python main.py
     ```

3. The summarizer will process the document and provide a concise summary based on your input.

## Example

Suppose you have an article titled `my_article.txt` in the `data` folder. You can summarize it by running:

```bash
python main.py --question "What are the key findings in this article?"
```

## Contributing

Contributions are welcome! If you'd like to enhance the summarizer or fix any issues, feel free to submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README further, add badges, and provide more detailed instructions as needed. Happy summarizing! 🚀 If you have any questions or need further assistance, don't hesitate to ask! 😊

And hey, speaking of summarization, do you have any favorite books or articles that you'd recommend for someone interested in generative AI? 📚✨
