from tools.excel_loader import ExcelLoader
from tools.vector_store import StrategyVectorStore


loader = ExcelLoader("data/strategy.xlsx")

documents = loader.load_rules()

print(f"\nLoaded Documents : {len(documents)}")

store = StrategyVectorStore()

store.create_vector_store(documents)

store.save_vector_store()

print("\nSearching...\n")

results = store.similarity_search(
    "Find financially healthy companies",
    k=3
)

for i, doc in enumerate(results):

    print("=" * 60)

    print(f"Result {i+1}")

    print(doc.page_content)

    print(doc.metadata)