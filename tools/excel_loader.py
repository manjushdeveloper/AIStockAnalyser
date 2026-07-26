import pandas as pd
from langchain_core.documents import Document


class ExcelLoader:

    def __init__(self, excel_path):
        self.excel_path = excel_path

    def load_rules(self):
        """
        Reads the Excel file and converts each row
        into a LangChain Document.
        """

        df = pd.read_excel(self.excel_path)

        documents = []

        for index, row in df.iterrows():

            content = "\n".join(
                [f"{column}: {row[column]}" for column in df.columns]
            )

            document = Document(
                page_content=content,
                metadata={
                    "row_number": index + 1
                }
            )

            documents.append(document)

        return documents


if __name__ == "__main__":

    loader = ExcelLoader("Data/strategy.xlsx")

    docs = loader.load_rules()

    print(f"Total Rules : {len(docs)}\n")

    for doc in docs:
        print(doc.page_content)
        print("-" * 50)