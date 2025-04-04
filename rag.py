from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import LlamaCpp

# 1️⃣ Carrega o PDF
loader = PyPDFLoader("/Users/marcelodearaujo/Desktop/IntuitiveCare/anexos_ans/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf")
documents = loader.load()

# 2️⃣ Gera embeddings e armazena no FAISS
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.from_documents(documents, embeddings)

# 3️⃣ Usa um modelo LLM que roda localmente
llm = LlamaCpp(
    model_path = '/Users/marcelodearaujo/Desktop/IntuitiveCare/llama-2-7b-chat.Q4_K_M.gguf',
    n_ctx=4096,
    n_gpu_layers=16 
) 

# 4️⃣ Cria a cadeia de busca + geração (RAG)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm, 
    retriever=db.as_retriever(),
    return_source_documents=True
)

# 5️⃣ Faz uma pergunta
resposta = qa_chain.invoke("O que é ANGIOTOMOGRAFIA?")
print(resposta)
