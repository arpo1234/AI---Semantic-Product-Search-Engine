from django.shortcuts import render
import chromadb
from chromadb.utils import embedding_functions


chroma_client = chromadb.PersistentClient(path="dazzle_vector_db")

sbert_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

collection = chroma_client.get_collection(name="dazzle_products", embedding_function=sbert_fn)

def search_products(request):
    query = request.GET.get('q', '') 
    results = []

    if query:
      
        raw_results = collection.query(
            query_texts=[query],
            n_results=4
        )
        
        if raw_results and raw_results['metadatas'][0]:
            for i in range(len(raw_results['metadatas'][0])):
                meta = raw_results['metadatas'][0][i]
                results.append({
                    'name': meta.get('product_name'),
                    'current_price': meta.get('current_price'),
                    'original_price': meta.get('original_price'),
                    'thumbnail_url': meta.get('thumbnail_url'),
                    'score': round((1 - raw_results['distances'][0][i]) * 100, 2) 
                })


    return render(request, 'core/index.html', {'results': results, 'query': query})
