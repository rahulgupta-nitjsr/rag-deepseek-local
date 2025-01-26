import faiss
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = faiss.IndexFlatL2(384)
        self.texts = []

    def add_text(self, text):
        embedding = self.model.encode([text])[0]
        self.index.add(embedding.reshape(1, -1))
        self.texts.append(text)

    def search(self, query, k=5):
        query_vector = self.model.encode([query])[0]
        distances, indices = self.index.search(query_vector.reshape(1, -1), k)
        return [self.texts[i] for i in indices[0]]
