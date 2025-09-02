---
Priority level:
  - A 🥰
---
### **GraphRAG / Architecture & Modeling**

1. **What schema patterns work best for high-performance RAG on top of a live graph?**
    - Should I favor certain relationship structures or avoid certain node types?
2. **How should I model evolving trust, influence, and social context over time?**
    - Is versioning or temporal layering on relationships common/best?
3. **Are there best practices around dynamically generated subgraphs per query for context injection into LLMs?**
4. **What’s the right balance between explicit schema and emergent patterns (e.g., user behavior generating edge types)?**
5. **How would you handle influence/conflict estimation at scale if trust is asymmetric and contextual?**

---

### **LLM Integration / Retrieval**

1. **When injecting graph context into a LLM, what chunking strategies (nodes/edges/paths) have worked best?**
2. **What’s the current state-of-the-art for embedding structured graph data alongside text for RAG?**
3. **How do you avoid hallucination or overfitting when RAG is augmented from social/introduction graphs?**

---

### **Performance & Scaling**

1. **What indexing, caching, or embedding strategies have worked well for subsecond RAG over large graphs?**
2. **Are there hybrid graph-neural approaches you’d recommend for relevance/influence scoring at inference-time (vs precomputed)?**

---

### **Team + Tools**

1. **If you were me, would you build on top of open-source like GraphStorm or Neptune ML—or go leaner with custom infra?**
2. **What would you absolutely avoid if rebuilding Amazon’s internal knowledge or influence graph from scratch today?**