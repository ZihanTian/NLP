import metapy
with open('recipes/tutorial.toml', 'w') as f:
    f.write('type = "line-corpus"\n')
    f.write('store-full-text = true\n')
config = """prefix = "." # tells MeTA where to search for datasets

dataset = "recipes" # a subfolder under the prefix directory
corpus = "tutorial.toml" # a configuration file for the corpus specifying its format & additional args

index = "recipes-idx" # subfolder of the current working directory to place index files

query-judgements = "recipes/recipes-qrels.txt" # file containing the relevance judgments for this dataset

stop-words = "stopwords.txt"

[[analyzers]]
method = "ngram-word"
ngram = 1
filter = "default-unigram-chain"
"""
with open('recipes-config.toml', 'w') as f:
    f.write(config)
inv_idx = metapy.index.make_inverted_index('recipes-config.toml') 
ranker = metapy.index.OkapiBM25(k1 = 1.2, b = 0.5, k3 = 500)
num_results = 10
retrieval_results = []
results = []
with open('recipes/queries.txt') as query_file:
    for query_num, line in enumerate(query_file):
        small = []
        query = metapy.index.Document()
        query.content(line.strip())
        results = ranker.score(inv_idx, query, num_results)  
        res_list = [(query_num + 1, x[0]) for x in results]
        retrieval_results += res_list
        
        
        print("Query: ", query.content())
        print("Retrieved Results")
        for num, (d_id, _) in enumerate(results):
          small.append(d_id)
          content = inv_idx.metadata(d_id).get('content')
          print(str(num + 1), d_id, content)
        print(small)