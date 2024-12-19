# 🤖 Biometric Privacy ChatBot
**_a RAG chatbot that provides policy recommendations for lawmakers in the biometric data and AI privacy spaces_**

Melody Choi, Natalia Eichmann 

Developed for SPI 352, taught by Prof. Peter Henderson and Christian Chung

Fall 2024, Princeton University

## 👩‍💻	Overview

Our model is a RAG chatbot that takes in a user query as input and offers a response informed by a database collected from a wide range of US and EU legislations, court cases, and policy-related scholarly articles. The chatbot is built in Python, using LangChain for developing LLM pipelines, OpenAI's GPT-4o, OpenAI's text-embedding-3-small, and Choma vector database.

On startup, the chatbot will load the vector database (persisted on disk) and ask for the user to enter a query.
![img1](https://github.com/user-attachments/assets/77fc4fa9-4efc-46d0-a050-97674b95e695)

When a query is input, the chatbot will retrieve context, augment the user's original query, and feed the combined prompt into GPT-4o through LangChain, outputting a response.
![img2](https://github.com/user-attachments/assets/6163817c-1554-4e9f-9985-17ad99bdf38f)

----

### Documents used as context:
- Fiero, Anne Wright, and Elena Beier. "New Global Developments in Data Protection and Privacy Regulations: Comparative Analysis of European Union, United States, and Russian Legislation." Stanford Journal of International Law 58 (2022): 151–192.
- Hilsman, Sophia. "Toward a Biometric Privacy Act to Protect Individual Rights: What the United States Can Learn from the European Union and China," Cardozo International & Comparative Law Review 7, no. 3 (Summer 2024): 993-1034 
- Jung, Youna, and Ethan D. Virgil. "Analysis of Legislative Framework Governing Biometric Data." Procedia Computer Science 241 (2024): 48–55. https://doi.org/10.1016/j.procs.2024.08.009.
- Hu, Margaret. "Biometrics and an AI Bill of Rights," Duquesne Law Review 60, no. 2 (Summer 2022): 283-301
- Harper, Hannah. "Your Body, Your Data, but Not Your Right of Action: Seeking Balance in Federal Biometric Privacy Legislation," National Security Law Journal 8, no. 1 (Summer 2021): 86-122
- EU AI Act
- GDPR
- Illinois BIPA
- Texas CUBI
- Nevada SB370
- Washington Biometric Identifiers Legislation
- BCLPEmerging Biometric Laws and Pending Legislation Tracker
- SIA's Guide to US Biometric Privacy Laws




## 💡	Installation (IN PROGRESS)

To install, run the following commands:
  ```
  $ git clone https://github.com/melodygchoi/spi352
  $ cd spi352
  $ pip install -r requirements.txt
  ```
