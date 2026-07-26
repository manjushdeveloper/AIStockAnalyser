import os

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings



class StrategyVectorStore:
    """
    Handles creation, saving, loading and retrieval
    of the FAISS Vector Database.
    """

    def __init__(
        self,
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    ):

        self.embedding_model = HuggingFaceEmbeddings(
            model_name=model_name
        )

        self.vector_db = None

    ##################################################
    # Create Vector Store
    ##################################################

    def create_vector_store(self, documents):

        """
        documents : List[Document]

        Creates FAISS vector database from
        LangChain Documents.
        """

        self.vector_db = FAISS.from_documents(
            documents,
            self.embedding_model
        )

        return self.vector_db

    ##################################################
    # Save Vector Store
    ##################################################

    def save_vector_store(
        self,
        folder_path="vector_store"
    ):

        if self.vector_db is None:
            raise Exception(
                "Vector Store has not been created."
            )

        os.makedirs(folder_path, exist_ok=True)

        self.vector_db.save_local(folder_path)

        print(f"\nVector Store saved to : {folder_path}")

    ##################################################
    # Load Vector Store
    ##################################################

    def load_vector_store(
        self,
        folder_path="vector_store"
    ):

        self.vector_db = FAISS.load_local(
            folder_path,
            self.embedding_model,
            allow_dangerous_deserialization=True
        )

        print("\nVector Store Loaded Successfully")

        return self.vector_db

    ##################################################
    # Search
    ##################################################

    def similarity_search(
        self,
        query,
        k=5
    ):

        if self.vector_db is None:
            raise Exception(
                "Load/Create Vector Store first."
            )

        return self.vector_db.similarity_search(
            query=query,
            k=k
        )

    ##################################################
    # Retriever
    ##################################################

    def get_retriever(
        self,
        k=5
    ):

        if self.vector_db is None:
            raise Exception(
                "Load/Create Vector Store first."
            )

        return self.vector_db.as_retriever(
            search_kwargs={
                "k": k
            }
        )