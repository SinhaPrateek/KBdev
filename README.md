# KBdev

### NLP, Named Entity Recognition, tf-idf, XML parsing, Python Libraries: Spacy, Networkx
Developed a Knowledge Graph out of data from ACL Anthology, a database of research papers on NLP
1. I parsed the paper XMLs to extract relevant information such as paper title, author, abstract, citations.
2. From abstracts, extracted noun chunks and used tf-idf technique to shortlist relevant keyword/topics from those noun chunks.
3. Developed Knowledge Graph, a Graph DB, containing nodes for each paper title, author, abstract and topic
Using this KG, we can find (A) the most researched topic and sought out author in a subject, (B) progression of topics.
Also, we can predict missing edges in the KG, which means predicting which topics will be researched more in the future and who would be the likely authors. Authors can be recommended other authors who are likely to collaborate even if working on different topics.
New clusters of topics can be discovered which are likely to lead to new knowledge generation in future.
