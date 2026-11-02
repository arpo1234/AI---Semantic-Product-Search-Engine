import pandas as pd
import chromadb
from chromadb.utils import embedding_functions
import os

print("Master DATASET Loading...")

if not os.path.exists("dazzle_master_dataset.csv"):
    print("❌ 'dazzle_master_dataset.csv' not finding in folder..Please put it into folder ")
    exit()

df = pd.read_csv("dazzle_master_dataset.csv")


df['Product Name'] = df['Product Name'].fillna('').astype(str)
df['Product Description'] = df['Product Description'].fillna('').astype(str)
df['Current Price'] = df['Current Price'].fillna('N/A').astype(str)
df['Original Price'] = df['Original Price'].fillna('N/A').astype(str)
df['Thumbnail URL'] = df['Thumbnail URL'].fillna('').astype(str)

print("  Chroma DB And SBERT Embedding Function Setup Running..")


chroma_client = chromadb.PersistentClient(path="dazzle_vector_db")


sbert_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# making table or collection in databse  
collection = chroma_client.get_or_create_collection(
    name="dazzle_products", 
    embedding_function=sbert_fn
)

print(" after processing 301 data pushing it in chromadb")

# create list for inser data in chromaDB
documents = []
metadatas = []
ids = []       

for idx, row in df.iterrows():
    
    combined_text = f"Product: {row['Product Name']}. Description: {row['Product Description']}"
    documents.append(combined_text)
    
    
    metadatas.append({
        "product_name": row['Product Name'],
        "current_price": row['Current Price'],
        "original_price": row['Original Price'],
        "thumbnail_url": row['Thumbnail URL']
    })
    
    
    ids.append(f"prod_{idx}")


collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)

print(f"\n Successful! Totall {collection.count()} vector and metadata saved 'dazzle_vector_db' saved in folder")