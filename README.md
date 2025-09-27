# Moroccan Constitution Chatbot (RAG)

A **Retrieval-Augmented Generation (RAG) chatbot** that allows you to ask questions about the **Moroccan Constitution of 2011** directly from the terminal.  
The chatbot uses **LangChain**, **OpenAI**, and **FAISS** for efficient document retrieval.

---

## 🔹 Features

- Automatically loads the PDF of the Moroccan Constitution
- Splits the text into chunks for better retrieval
- Contextual search using FAISS and OpenAI embeddings
- Maintains conversation history
- Simple terminal-based interface

---

## 🔹 Prerequisites

- Python 3.10+  
- OpenAI API key (stored in a `.env` file)  
- Chrome and ChromeDriver installed (if using Selenium for future extensions)  

---

## 🔹 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/moroccan-constitution-chatbot.git
cd moroccan-constitution-chatbot
```

2. **Install the dependencies:**
```bash
pip install -r requirements.txt
```

3. **Create a `.env` file at the root with your OpenAI key:**
```ini
OPENAI_API_KEY=sk-xxxxxx
```

4. **Place the PDF in the documents/ folder:**
```
documents/constitution_marocaine_2011-ar.pdf
```

---

## 🔹 Usage

1. **Run the chatbot from the terminal:**
```bash
python intro.py
```

2. **Type your questions in the terminal**
3. **To exit, type `exit`, `quit`, or `q`**

### Example Conversation:
```
You: What are the fundamental rights guaranteed by the Constitution?
Bot: The Moroccan Constitution guarantees ...

You: And what does it say about freedom of expression?
Bot: Freedom of expression is protected ...
```

---

## 🔹 Project Structure

```
moroccan-constitution-chatbot/
├── documents/
│   └── constitution_marocaine_2011-ar.pdf
├── intro.py
├── requirements.txt
└── README.md
```

---

## 🔹 Technologies Used

- **LangChain**: conversational chain management
- **OpenAI**: embeddings and text generation
- **FAISS**: vector search engine
- **PyPDF**: PDF reading
- **python-dotenv**: environment variable management

---

## 🔹 License

This project is licensed under the MIT License.
