from abc import ABC, abstractmethod


# Interface Produto: Documento
class Document(ABC):
    @abstractmethod
    def create(self, content: str):
        pass


# Produtos Concretos
class PDFDocument(Document):
    def create(self, content: str):
        print(f"Documento PDF criado com o conteúdo:\n{content}")


class WordDocument(Document):
    def create(self, content: str):
        print(f"Documento Word criado com o conteúdo:\n{content}")


class TXTDocument(Document):
    def create(self, content: str):
        print(f"Documento TXT criado com o conteúdo:\n{content}")


# Fábrica Base (Creator)
class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        pass

    def generate_document(self, content: str):
        document = self.create_document()
        document.create(content)


# Fábricas Concretas
class PDFDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return PDFDocument()


class WordDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return WordDocument()


class TXTDocumentFactory(DocumentFactory):
    def create_document(self) -> Document:
        return TXTDocument()


# Testando o Gerenciador de Documentos
if __name__ == "__main__":
    # Conteúdo do documento
    content = "Este é um exemplo de conteúdo do documento."

    # Criando fábricas de documentos
    pdf_factory = PDFDocumentFactory()
    word_factory = WordDocumentFactory()
    txt_factory = TXTDocumentFactory()

    # Gerando documentos
    pdf_factory.generate_document(content)
    word_factory.generate_document(content)
    txt_factory.generate_document(content)
