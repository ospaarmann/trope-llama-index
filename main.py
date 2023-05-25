# Import necessary packages
import os
import pickle

from llama_index import (
    GPTVectorStoreIndex,
    ResponseSynthesizer,
)
from llama_index.retrievers import VectorIndexRetriever
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.indices.postprocessor import SimilarityPostprocessor
from llama_index import download_loader
from pathlib import Path

os.environ['OPENAI_API_KEY'] = 'YOUR_OPENAI_API_KEY'

PDFReader = download_loader("PDFReader")

loader = PDFReader()

# load pdf and index them 
documents = loader.load_data(file=Path('./article.pdf'))

# build index
index = GPTVectorStoreIndex.from_documents(documents)

# configure retriever
retriever = VectorIndexRetriever(
    index=index, 
    similarity_top_k=2,
)

# configure response synthesizer
response_synthesizer = ResponseSynthesizer.from_args(
    node_postprocessors=[
        SimilarityPostprocessor(similarity_cutoff=0.7)
    ]
)

# assemble query engine
query_engine = RetrieverQueryEngine(
    retriever=retriever,
    response_synthesizer=response_synthesizer,
)

# Querying the index
while True:
    prompt = input("Type prompt...")
    response = query_engine.query(prompt)
    print(response)
