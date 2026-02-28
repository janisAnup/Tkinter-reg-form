Tkinter Registration Form

🎯 A simple and stylish registration form built using Python's Tkinter library.

🛠️ Features:
- User-friendly GUI
- Entry fields for registration details
- Styled using a separate `designs.py` file for cleaner code
- Modular structure

📂 Files:
- `main.py` — main application logic
- `designs.py` — holds all the styling for the form
- `README.md` — you're reading it 😉

👩‍💻 Created by Janis Anup  
🧑‍💼 Internship Task 1 @ Next24Tech



Assginment-1
 Student REST API
 Repo is available in the https://github.com/christopher-pb location
 1.Clone the code and push it to the master/main branch
 2.Raise a pull request and merge the code to main/master 
 3. Should be able to build the code and should be shown in the action tab in github as successful
 
 Assginment-2
 Employee REST API
 Repo is available in the https://github.com/christopher-pb location and go through the README.md file
 1.Clone the code and do the same for employee with json itself and not database
	Employees
		EmployeeID 
		FirstName
		LastName
		Gender
		DateOfBirth
	Department Table

	Departments
		DepartmentID 
		DepartmentName
		Location
	Salaries
		SalaryID 
		EmployeeID 	
		BasicSalary
		Bonus
		Allowances
 2.Raise a pull request and merge the code to main/master 
 3. Should be able to build the code and should be shown in the action tab in github as successful
 4.Download the code and run the application 
 5.Use the postman to check the rest call





 UNIT 1 — ALL QUESTIONS WITH ANSWERS
2-MARK QUESTIONS (80 words)
Q1. What is NLP?
Answer: Natural Language Processing (NLP) is a field of computer science, artificial intelligence, and linguistics concerned with interactions between computers and human languages. It involves a computer extracting meaningful information from natural language input and producing natural language output. NLP is the technology used by machines to understand, analyse, manipulate, and interpret human languages. It helps developers organize knowledge for performing tasks such as translation, automatic summarization, Named Entity Recognition, speech recognition, relationship extraction, and topic segmentation.

Q2. What are the two components of NLP?
Answer: The two components are: (1) Natural Language Understanding (NLU) — helps machines understand and analyse human language by extracting metadata from content such as concepts, entities, keywords, emotion, relations, and semantic roles. It maps given input into useful representations and analyses different aspects of language. (2) Natural Language Generation (NLG) — acts as a translator converting computerized data into natural language representation. It involves Text Planning (what to say), Sentence Planning (how to say it), and Text Realization (producing actual text).

Q3. What was the Georgetown-IBM experiment?
Answer: The Georgetown-IBM experiment was conducted in 1954 and was one of the earliest demonstrations of machine translation. It involved automatic translation of 60 Russian sentences into English using a simple system with only 6 grammar rules and 250 vocabulary words. Scientists believed full machine translation would be achieved within 3-5 years, but this proved overly optimistic. It was a landmark event in the history of NLP that sparked significant interest and funding in machine translation research during the 1950s.

Q4. What is the Turing Test?
Answer: The Turing Test was proposed by Alan Turing in 1950 in his paper "Computing Machinery and Intelligence." It tests whether a machine can exhibit intelligent behaviour indistinguishable from a human. A human judge conducts text-based conversations with both a machine and a human without knowing which is which. If the judge cannot reliably distinguish the machine from the human, the machine passes the test. It remains a foundational concept in artificial intelligence and NLP for measuring machine intelligence.

Q5. What was SHRDLU?
Answer: SHRDLU was a program written by Terry Winograd in 1968-70 that helped users communicate with a computer and move objects in a virtual world. It could handle instructions such as "pick up the green ball" and answer questions like "What is inside the black box." The main importance of SHRDLU was that it showed that syntax, semantics, and reasoning about the world could be combined to produce a system that understands natural language. However, it only worked within its limited blocks world.

Q6. What was the LUNAR system?
Answer: LUNAR was the classic example of a Natural Language database interface system that used Augmented Transition Networks (ATNs) and Woods' Procedural Semantics. It was designed to answer questions about lunar rock samples collected during Apollo missions. LUNAR was capable of translating elaborate natural language expressions into database queries and could handle 78% of requests without errors. It demonstrated that computers could understand complex English questions and automatically convert them into structured queries for information retrieval.

Q7. What is Case Grammar?
Answer: Case Grammar was developed by linguist Charles J. Fillmore in 1968. It uses languages such as English to express the relationship between nouns and verbs by using prepositions. In Case Grammar, case roles are defined to link certain kinds of verbs and objects. For example, in "Neha broke the mirror with the hammer": Neha is identified as the agent (who performed the action), mirror as the theme (what was affected), and hammer as the instrument (the tool used to perform the action).

Q8. What is an Augmented Transition Network (ATN)?
Answer: An Augmented Transition Network (ATN) is a finite state machine that is capable of recognizing regular languages. It was a key development during the 1960-1980 period of NLP. ATNs extend basic Finite State Automata by adding memory and register capabilities, allowing the machine to store and recall information while processing input. This enabled parsing of more complex sentence structures than simple FSAs could handle. ATNs were used in systems like LUNAR for parsing natural language queries into database operations.

Q9. What is Chomsky's Generative Grammar?
Answer: In 1957, Noam Chomsky introduced the idea of Generative Grammar in his book "Syntactic Structures." He claimed that language is generative in nature — a finite set of rules can generate an infinite number of valid sentences. Generative Grammar provides rule-based descriptions of syntactic structures. For example, the rule S → NP VP states a sentence consists of a noun phrase followed by a verb phrase. This framework became foundational for computational linguistics, NLP, and the development of grammar-based language models.

Q10. List four advantages of NLP.
Answer: (1) NLP helps users ask questions about any subject and get a direct response within seconds. (2) NLP offers exact answers to the question — it does not offer unnecessary and unwanted information. (3) NLP helps computers communicate with humans in their languages, making technology accessible. (4) Most companies use NLP to improve the efficiency of documentation processes, accuracy of documentation, and identify the information from large databases. Additionally, NLP is very time efficient in processing large volumes of text data.

Q11. List the disadvantages of NLP.
Answer: (1) NLP may not show context — it struggles to understand implied meaning, sarcasm, and cultural nuances. (2) NLP is unpredictable — it may produce incorrect or inconsistent outputs for similar inputs. (3) NLP may require more keystrokes compared to simple keyword-based search approaches. (4) NLP is unable to adapt to the new domain, and it has a limited function — it is built for a single and specific task only, requiring significant retraining or redesign for different applications and domains.

Q12. What is Language Modeling?
Answer: Language modeling (LM) is the use of various statistical and probabilistic techniques to determine the probability of a given sequence of words occurring in a sentence. Language models analyze bodies of text data to provide a basis for their word predictions. LM is used in artificial intelligence, NLP, natural language understanding and generation systems, particularly those performing text generation, machine translation, and question answering. For example, given "I want to", a language model assigns probabilities to next words like "eat" or "go."

Q13. What is an N-gram language model?
Answer: An N-gram model creates a probability distribution for a sequence of N words. The N defines the size of the gram or sequence of words being assigned a probability. This allows the model to predict the next word in a sentence. For example, if N=5, a gram might look like "can you please call me." The model calculates P(next word | previous N-1 words) using counts from training data. N-gram models are simple but effective for autocomplete, spell correction, and speech recognition tasks.

Q14. What is a Unigram model?
Answer: A Unigram is the simplest type of language model where N=1. It doesn't look at any conditioning context in its calculations. It evaluates each word or term independently. The probability of a sentence is the product of individual word probabilities: P("the cat sat") = P("the") × P("cat") × P("sat"). Since unigrams ignore word order, "the cat sat" and "sat cat the" have identical probabilities. Despite this limitation, unigrams serve as useful baselines and are used in basic information retrieval tasks.

Q15. What is a Bidirectional language model?
Answer: Unlike N-gram models which analyze text in one direction (backward — considering only previous words), bidirectional models analyze text in both directions — backward and forward simultaneously. This means they consider both preceding and following words to make predictions. For example, in "The ___ sat on the mat," a bidirectional model uses "The" (before) AND "sat on the mat" (after) to predict the missing word. BERT (Bidirectional Encoder Representations from Transformers), introduced by Google in 2018, is the most well-known bidirectional language model.

Q16. What are Neural Language Models?
Answer: Neural language models use deep learning techniques to overcome the limitations of N-gram models. These models use neural networks such as Recurrent Neural Networks (RNNs) and Transformers to capture complex patterns and dependencies in text. Unlike N-grams which have fixed and limited context windows, neural models can learn long-range relationships between words across entire sentences or documents. Examples include GPT models (using Transformer architecture for text generation) and BERT (bidirectional understanding), achieving near-human performance in language tasks.

Q17. Name four uses of Language Modeling.
Answer: (1) Speech recognition — machines process speech audio; voice assistants like Siri and Alexa use speech recognition powered by language models. (2) Text generation — uses prediction to generate coherent and contextually relevant text for creative writing and summarization. (3) Chatbots — engage in humanlike conversations and generate accurate responses for customer support and information retrieval. (4) Machine translation — translation of one language to another by programs like Google Translate and Microsoft Translator, which rely on language models for fluent output.

Q18. What is a Regular Expression?
Answer: A Regular Expression (RegEx) is a sequence of characters mainly used to find or replace patterns embedded in text. It is a set of characters or pattern used to find substrings in a given string. A regular expression is a language for specifying text search strings that helps match or extract strings using specialized syntax. The Regular Expression language was formalized by American mathematician Stephen Cole Kleene. In NLP, regex is used for data cleaning, named entity recognition (extracting emails, phone numbers), and text normalization.

Q19. How do Regular Expressions work? Explain with the student name example.
Answer: Consider students: Sunil, Shyam, Ankit, Surjeet, Sumit, Subhi, Surbhi, Siddharth, Sujan. The pattern requires first two letters as S and u, followed by exactly three positions taken by any letter. Checking: Sunil (S-u-n-i-l ✅), Shyam (second letter 'h' not 'u' ❌), Ankit (starts with 'A' ❌), Surjeet (too many letters after Su ❌), Sumit (S-u-m-i-t ✅), Subhi (S-u-b-h-i ✅), Surbhi (too long ❌), Siddharth (Si not Su ❌), Sujan (S-u-j-a-n ✅). Extracted: Sunil, Sumit, Subhi, Sujan.

Q20. State the mathematical properties of Regular Expressions.
Answer: (1) ε is a Regular Expression indicating the language has an empty string. (2) φ is a Regular Expression denoting an empty language. (3) If X and Y are Regular Expressions, then X.Y (concatenation of XY), X+Y (union of X and Y), and X*, Y* (Kleene Closure of X and Y) are also regular expressions. (4) If a string is derived from the above rules, then that would also be a regular expression. These mathematical properties form the algebraic foundation for all pattern matching operations.

Q21. Name three NLP uses of Regular Expressions.
Answer: (1) Data Cleaning and Pre-processing — regex removes unwanted characters such as special characters, punctuation, and numbers that can interfere with NLP algorithms and models. (2) Named Entity Recognition (NER) — regex extracts named entities such as names, locations, organizations, email IDs, and phone numbers from large unstructured text content. (3) Text Normalization — regex transforms text data into standard format, such as converting all text to lowercase or removing stop words, making NLP tasks more accurate and effective.

Q22. Define Finite State Automaton formally.
Answer: The term automata derives from Greek "αὐτόματα" meaning "self-acting." An automaton is an abstract self-propelled computing device following a predetermined sequence of operations automatically. An automaton with finite states is called Finite Automaton (FA) or Finite State Automata (FSA). Mathematically represented as 5-tuple (Q, Σ, δ, q₀, F): Q is a finite set of states, Σ is the alphabet, δ is the transition function, q₀ is the initial state from where input is processed (q₀ ∈ Q), F is the set of final states (F ⊆ Q).

Q23. What is Morphological Analysis?
Answer: Morphological analysis is a field of linguistics that studies the structure of words. It identifies how a word is produced through the use of morphemes. A morpheme is the basic unit of the English language — the smallest element of a word that has grammatical function and meaning. Morphology studies how words are built from smaller meaning-bearing units. Two broad classes of morphemes exist: stems (the main morpheme supplying the core meaning) and affixes (adding additional meaning of various kinds including prefixes, suffixes, infixes, and circumfixes).

Q24. What are the types of affixes? Give examples.
Answer: Affixes are bound morphemes adding additional meaning to stems. Four types: (1) Suffix — added after root: eat→eats, walk→walked. (2) Prefix — added before root: un→un-buckle, re→re-write. (3) Circumfix — added around root on both sides: German "sagen" (to say) → "ge-sag-t" (said), with ge- before and -t after. (4) Infix — inserted inside root: Tagalog "hingi" (borrow) → "humingi" (the agent of an action), with -um- inserted within the word.

Q25. What is a Lexicon in NLP?
Answer: A lexicon is the vocabulary — the body of words used in a particular language or subject. In morphological analysis, the lexicon transducer maps between the lexical level (with its stems and morphological features) and an intermediate level that represents a simple concatenation of morphemes. Then a host of transducers, each representing a single spelling rule constraint, all run in parallel to map between this intermediate level and the surface level (actual written form). The lexicon serves as the dictionary validating root words during morphological processing.

Q26. What is Tokenization?
Answer: Tokenization, in the realm of Natural Language Processing and machine learning, refers to the process of converting a sequence of text into smaller parts known as tokens. These tokens can be as small as characters or as long as words. For example, "Chatbots are helpful" → word tokens: ["Chatbots", "are", "helpful"], or character tokens: ["C","h","a","t","b","o","t","s"," ","a","r","e"," ","h","e","l","p","f","u","l"]. It is the fundamental first step in almost every NLP pipeline.

Q27. What are the types of Tokenization?
Answer: (1) Word tokenization — breaks text into individual words; most common for English with clear word boundaries. (2) Character tokenization — segments text into individual characters; beneficial for languages lacking clear word boundaries or tasks requiring granular analysis like spelling correction. (3) Subword tokenization — strikes a balance between word and character tokenization, breaking text into units larger than a character but smaller than a word. For example, "Chatbots" → ["Chat", "bots"]. Useful for out-of-vocabulary words in NLP tasks.

Q28. Name three use cases of Tokenization.
Answer: (1) Search engines — when you type a query into Google, it employs tokenization to dissect your input, helping the engine sift through billions of documents to present the most relevant results. (2) Machine translation — tools like Google Translate utilize tokenization to segment sentences in the source language; tokenized segments are translated and reconstructed in the target language retaining original context. (3) Speech recognition — voice assistants like Siri or Alexa convert spoken words to text, then tokenize to process requests.

Q29. What is Spell Checking in NLP?
Answer: Spell checking is the process of identifying words in texts that have spelling errors or are misspelled. Text data from social media or extracted from images using Optical Character Recognition (OCR) usually contains typos, misspellings, spurious symbols, or errors that impact machine learning models. For example, if "John" is present both correctly and as "J0hn" (zero replacing 'o'), a model treats them as two separated words causing unexpected prediction outcomes. Spell checking detects and corrects such errors to improve data quality.

Q30. Define Minimum Edit Distance.
Answer: The Minimum Edit Distance between two strings str1 and str2 is defined as the minimum number of insert/delete/substitute operations required to transform str1 into str2. For example, str1="ab", str2="abc" — inserting character 'c' on str1 transforms it into str2, so edit distance is 1. Edit distance can also be calculated as operations to transform str2 into str1 — deleting 'c' from "abc" gives "ab" with same distance of 1. The word "giraffe" differs from "graffe" by only one letter, making it the closest match.

Q31. Give an example of Minimum Edit Distance.
Answer: For str1="INTENTION" and str2="EXECUTION", the minimum edit distance is 5. All operations are performed on str1. The algorithm uses a dynamic programming matrix of size (10×10). Each cell is computed as the minimum of: cell above + 1 (deletion), cell to the left + 1 (insertion), and diagonal cell + substitution cost (0 if characters match, 2 if different). The bottom-right cell of the completed matrix gives the final answer. Applications include spell correction where candidates are ranked by their edit distance from the misspelled word.

Q32. What is an Exponential Language Model?
Answer: An Exponential Language Model is based on the principle of entropy, which is defined as a state of disorder, randomness, or uncertainty. The model states that the probability distribution with the most entropy is the best choice. This means the model avoids making unjustified assumptions about the data — it selects the most uniform distribution that still satisfies known constraints from training data. Exponential models are also called Maximum Entropy models and are used in NLP tasks like part-of-speech tagging and text classification.

Q33. What are Parts-of-Speech tagging and Parsing as language model uses?
Answer: Parts-of-Speech tagging involves the markup and categorization of words by certain grammatical characteristics (noun, verb, adjective, etc.). It was first used in the study of the Brown Corpus — a body of random English prose designed to be studied by computers. This corpus trained several important language models, including one used by Google to improve search quality. Parsing involves analysis of any string of data or sentence that conforms to formal grammar and syntax rules, depicting each word's relationship to others. Spell-checking applications use parsing.

5-MARK QUESTIONS (150 words)
Q1. Explain the origin and history of NLP from 1940s to the present.
Answer:

1940-1960 (Machine Translation era): NLP started in the 1940s. In 1948, the first recognizable NLP application was introduced at Birkbeck College, London. In the 1950s, there was a conflicting view between linguistics and computer science. Chomsky developed his first book "Syntactic Structures" and claimed language is generative in nature. In 1957, he introduced Generative Grammar — rule-based descriptions of syntactic structures.

1960-1980 (AI era): Key developments included Augmented Transition Networks (ATNs) — finite state machines capable of recognizing regular languages. Charles Fillmore developed Case Grammar (1968) to express noun-verb relationships using case roles like agent, theme, and instrument. Key systems: SHRDLU (1968-70) demonstrated natural language understanding in a virtual blocks world, handling instructions and questions by combining syntax, semantics, and reasoning. LUNAR provided natural language database querying using ATNs and Procedural Semantics, handling 78% of requests without errors.

Modern Era: Modern NLP consists of speech recognition, machine translation, and machine text reading. Combined, these allow AI to gain knowledge of the world, powering applications like Amazon Alexa where users can ask questions and receive spoken answers.

Q2. Explain NLU and NLG as components of NLP in detail.
Answer:

Natural Language Understanding (NLU) helps the machine understand and analyse human language by extracting metadata from content such as concepts, entities, keywords, emotion, relations, and semantic roles. NLU is mainly used in business applications to understand the customer's problem in both spoken and written language. It involves two key tasks: (1) mapping given input into useful representations that computers can process, and (2) analyzing different aspects of the language including grammar, meaning, and context. For example, when a customer writes "My order is late and I'm angry," NLU extracts entity (order), emotion (anger), and intent (complaint).

Natural Language Generation (NLG) acts as a translator that converts computerized data into natural language representation. It involves three stages: (1) Text Planning — determining what content to communicate by selecting relevant information; (2) Sentence Planning — deciding sentence structure, choosing appropriate words and syntax; (3) Text Realization — producing the final grammatically correct and fluent text output. For example, given structured data about weather (temperature=35°C, humidity=80%), NLG generates: "Expect a hot and humid day."

Together NLU (input) and NLG (output) form the complete NLP cycle enabling full human-computer communication.

Q3. Explain the advantages and disadvantages of NLP.
Answer:

Advantages: (1) NLP helps users ask questions about any subject and get a direct response within seconds, enabling rapid access to information from vast data sources. (2) NLP offers exact answers to the question — it does not offer unnecessary and unwanted information, improving search precision. (3) NLP helps computers communicate with humans in their languages, making technology accessible to non-technical users globally. (4) It is very time efficient — processing thousands of documents in minutes rather than hours of manual reading. (5) Most companies use NLP to improve the efficiency of documentation processes, accuracy of documentation, and identify important information from large databases, automating formerly manual workflows.

Disadvantages: (1) NLP may not show context — it struggles with implied meaning, sarcasm, cultural references, and situational nuances in language. (2) NLP is unpredictable — similar inputs may produce inconsistent or incorrect outputs. (3) NLP may require more keystrokes than simple keyword-based search methods. (4) NLP is unable to adapt to the new domain, and it has a limited function — it is built for a single and specific task only. Switching to a new domain requires significant retraining or complete redesign of the system.

Q4. Explain the different types of Language Models with examples and uses.
Answer:

N-gram Model: Creates probability distributions for sequences of N words, predicting the next word based on previous N-1 words. Example: N=5 gram "can you please call me." Simple and effective for autocomplete.

Unigram Model: Simplest type (N=1) — evaluates each word independently without considering context. P("cat sat") = P("cat") × P("sat"). Ignores word order entirely.

Bidirectional Model: Analyzes text in both directions — backward and forward — unlike N-grams which only look backward. Captures context from both sides of each word. BERT is the leading example.

Exponential Model: Based on the principle of entropy (state of disorder, randomness, uncertainty). Selects the probability distribution with the most entropy as the best choice, avoiding unjustified assumptions.

Neural Language Models: Use deep learning — RNNs and Transformers — to capture complex patterns and long-range dependencies in text, overcoming N-gram limitations.

Key Uses: (1) Speech recognition (Siri, Alexa). (2) Text generation for creative writing and summarization. (3) Chatbots for customer support. (4) Machine translation (Google Translate, Microsoft Translator). (5) Parts-of-speech tagging — categorizing words grammatically, famously used in the Brown Corpus study and by Google for search improvement. (6) Parsing — analyzing sentence structure, used in spell-checking applications.

Q5. What are Regular Expressions? Explain properties, working, and NLP applications.
Answer:

Definition: Regular Expressions (RegEx) are sequences of characters used to find or replace patterns in text. A regex is a language for specifying text search strings, formalized by mathematician Stephen Cole Kleene. It helps match or extract strings using specialized syntax — for example, extracting all email IDs or phone numbers from large unstructured text.

Mathematical Properties: (1) ε is a RegEx indicating empty string. (2) φ is a RegEx denoting empty language. (3) If X and Y are RegEx, then X.Y (concatenation), X+Y (union), and X*, Y* (Kleene Closure) are also regular expressions. (4) Any string derived from these rules is also a regular expression.

Working Example: Students: Sunil, Shyam, Ankit, Surjeet, Sumit, Subhi, Surbhi, Siddharth, Sujan. Pattern: names with first two letters S and u, followed by exactly 3 characters. Checking each name against the pattern: Sunil ✅, Shyam ❌ (not Su), Ankit ❌, Surjeet ❌ (too long), Sumit ✅, Subhi ✅, Surbhi ❌ (too long), Siddharth ❌, Sujan ✅. Extracted: Sunil, Sumit, Subhi, Sujan.

NLP Applications: (1) Data cleaning — removing special characters and punctuation. (2) Named Entity Recognition — extracting names, locations, organizations. (3) Text normalization — converting text to standard format.

Q6. Explain Finite State Automata — definition, formal representation, and components.
Answer:

The term "automata" derives from the Greek word "αὐτόματα" meaning "self-acting" and is the plural of automaton — an abstract self-propelled computing device that follows a predetermined sequence of operations automatically. An automaton having a finite number of states is called a Finite Automaton (FA) or Finite State Automata (FSA).

Formal Representation — 5-tuple (Q, Σ, δ, q₀, F):

Q is a finite set of states — the different positions the machine can be in, represented as circles in diagrams. Σ is a finite set of symbols called the alphabet of the automaton — the valid input characters the machine can read. δ is the transition function — defines how the machine moves from one state to another when reading an input symbol, represented as arrows between states. q₀ is the initial state from where any input is processed (q₀ ∈ Q) — the starting point of computation. F is a set of final state/states of Q (F ⊆ Q) — if the machine ends in one of these states after reading all input, the string is accepted.

Example: FSA accepting "cat": Q={q₀,q₁,q₂,q₃}, Σ={a-z}, δ(q₀,'c')=q₁, δ(q₁,'a')=q₂, δ(q₂,'t')=q₃, initial state=q₀, F={q₃}. Input "cat" traces q₀→q₁→q₂→q₃ (accepted). Input "car" reaches q₂ with 'r' where no transition exists (rejected).

Q7. Explain English Morphology — morphemes, stems, affixes with all four types.
Answer:

Morphological analysis studies the structure of words, identifying how words are produced through morphemes — the basic unit of language and the smallest element with grammatical function and meaning. Morphology studies how words are built from smaller meaning-bearing units.

Two Broad Classes: (1) Stems — the "main" morpheme of the word, supplying the main meaning (cat, run, happy). (2) Affixes — add "additional" meaning of various kinds and are further divided into four types.

Suffix (added after root) — most common in English: eat→eats (third person), walk→walked (past tense), happi→happiness (adjective to noun).

Prefix (added before root): un-buckle (reversal of action), re-write (repetition), dis-agree (opposition).

Circumfix (added around root — both sides simultaneously): German "sagen" (to say) → "ge-sag-t" (said). The prefix "ge-" and suffix "-t" are added together, neither alone carries the past tense meaning.

Infix (inserted inside root word): In Philippine language Tagalog, "hingi" (borrow) → "humingi" (the agent of an action). The morpheme "-um-" is inserted within the root.

NLP Importance: Morphological analysis enables search systems to match word variants, reduces vocabulary for ML models, and helps machine translation correctly handle tense and grammatical relationships.

Q8. Explain the Lexicon and Transducer system for morphological analysis.
Answer:

A lexicon is the vocabulary — the body of words used in a particular language or subject. In NLP morphological analysis, it stores all valid root words with their grammatical categories.

The lexicon transducer maps between the lexical level (with its stems and morphological features, e.g., "fox +Noun +Plural") and an intermediate level that represents a simple concatenation of morphemes (e.g., "fox+s"). Then a host of transducers, each representing a single spelling rule constraint, all run in parallel so as to map between this intermediate level and the surface level (the actual written form, e.g., "foxes").

Three-Level Process:

Lexical level: fox +Noun +Plural (dictionary representation)
Intermediate level: fox + s (morphemes concatenated)
Surface level: foxes (actual spelling after rules applied)
Spelling Rule Examples: (1) Nouns ending in x, s, sh, ch take "-es" instead of "-s": fox→foxes, bus→buses. (2) Nouns ending in consonant+y change y to ies: baby→babies. (3) Regular nouns just add "-s": cat→cats.

Analysis direction: surface "foxes" → spelling rules identify "es" after "x" = plural → lexicon confirms "fox" is a valid noun → output: "fox +Noun +Plural." Generation direction: "fox +Noun +Plural" → lexicon validates → spelling rule applies "-es" → output: "foxes."

Q9. Explain Tokenization — definition, types, and use cases in detail.
Answer:

Definition: Tokenization, in the realm of NLP and machine learning, refers to the process of converting a sequence of text into smaller parts known as tokens. These tokens can be as small as characters or as long as words. Example: "Chatbots are helpful" → ["Chatbots", "are", "helpful"] (word tokens) or ["C","h","a","t","b","o","t","s"," ","a","r","e"," ","h","e","l","p","f","u","l"] (character tokens).

Types: (1) Word tokenization — breaks text into individual words. Most common approach, particularly effective for languages with clear word boundaries like English. (2) Character tokenization — segments text into individual characters. Beneficial for languages lacking clear word boundaries or for tasks requiring granular analysis such as spelling correction. (3) Subword tokenization — strikes a balance between word and character tokenization, breaking text into units larger than a single character but smaller than a full word. For example, "Chatbots" → ["Chat", "bots"]. Especially useful for handling out-of-vocabulary words in NLP tasks.

Use Cases: (1) Search engines — Google employs tokenization to dissect user queries, helping sift through billions of documents for relevant results. (2) Machine translation — Google Translate tokenizes sentences in the source language, translates segments, and reconstructs them in the target language retaining context. (3) Speech recognition — Siri and Alexa convert spoken words to text, then tokenize to process and act upon user requests.

Q10. Explain the process of detecting and correcting spelling errors in NLP.
Answer:

Importance: Spell checking identifies misspelled words in texts. Data from social media or extracted using OCR usually contains typos, misspellings, spurious symbols, or errors that impact machine learning models. For example, if "John" appears both correctly and as "J0hn" (zero replacing 'o'), a model treats them as two separated words, causing unexpected outcomes in predictions.

Detection: Non-word errors (e.g., "graffe") are detected by dictionary lookup — the word doesn't exist. Real-word errors (e.g., "there" vs "their") require context analysis since both are valid words.

Correction using Noisy Channel Model: The system assumes the user intended a correct word w, but noise corrupted it into misspelling x. The formula w* = argmax P(x|w) × P(w) combines: the error model P(x|w) measuring how likely this specific typo is, and the language model P(w) measuring how common the correct word is.

Example: User typed "graffe." Candidates: "giraffe" (differs by one letter — edit distance 1), "grail" (distance 4), "graf" (distance 2). The word "giraffe" is intuitively more similar than "grail" or "graf" because it has the smallest edit distance. The Noisy Channel Model confirms: P("graffe"|"giraffe") × P("giraffe") yields the highest score, selecting "giraffe" as the correction.

Q11. Explain Minimum Edit Distance — definition, operations, algorithm, and example.
Answer:

Definition: Minimum Edit Distance between two strings str1 and str2 is the minimum number of insert/delete/substitute operations required to transform str1 into str2. For str1="ab", str2="abc", inserting 'c' gives distance 1. Equivalently, deleting 'c' from str2 also gives distance 1.

Three Operations: (1) Insertion — adding a character: "ab"→"abc." (2) Deletion — removing a character: "abc"→"ab." (3) Substitution — replacing one character: "cat"→"car."

Algorithm (Dynamic Programming): Build an (m+1)×(n+1) matrix for strings of length m and n. Initialize first row as 0,1,2,...,n (cost of insertions from empty string) and first column as 0,1,2,...,m (cost of deletions). For each cell[i][j]: if characters match, diagonal cost=0; otherwise substitution cost applies. Cell[i][j] = minimum of: cell[i-1][j]+1 (deletion), cell[i][j-1]+1 (insertion), cell[i-1][j-1]+cost (substitution or match). Bottom-right cell gives the answer.

Example: For str1="INTENTION" and str2="EXECUTION", building the 10×10 matrix and filling each cell, the minimum edit distance is 5 (with substitution cost=2). This means 5 single-character operations transform "INTENTION" into "EXECUTION."

Applications: Spell correction (ranking candidates by distance — "giraffe" with distance 1 from "graffe" beats "grail" with distance 4), DNA sequence alignment in bioinformatics, plagiarism detection, and machine translation evaluation using Word Error Rate.

Q12. Explain Grammar-Based and Statistical Language Models in detail.
Answer:

Grammar-Based Language Models define language using formal grammar rules written by human linguists. Rules describe how sentences are structured: S → NP VP (sentence = noun phrase + verb phrase), NP → Det N (noun phrase = determiner + noun). Given rules with terminals like Det→"the"|"a", N→"cat"|"fish", V→"ate", the model generates valid sentences like "the cat ate the fish" and rejects invalid orders like "cat the ate fish the." Each rule carries a probability, and a sentence's probability is the product of all applied rule probabilities. Advantages: linguistically motivated and captures grammar structure. Disadvantages: requires expert linguists, cannot cover all variations, rigid with informal language.

Statistical Language Models learn word patterns from large text corpora using probabilistic techniques. The N-gram model predicts the next word using previous N-1 words via the Markov assumption. Bigram calculation: P("cat"|"the") = Count("the cat") / Count("the"). If "the cat" appears 200 times and "the" appears 1000 times in training data, P("cat"|"the") = 0.2. The chain rule computes sentence probability: P(w₁w₂...wₙ) = P(w₁) × P(w₂|w₁) × P(w₃|w₂) × ... Advantages: automatic learning from data, handles real-world language, scalable. Disadvantages: zero-probability for unseen sequences, limited context.

Key Difference: Grammar-based models are human-designed (top-down rules), while statistical models are machine-learned (bottom-up from data).

Q13. Explain SHRDLU and LUNAR systems and their significance in NLP history.
Answer:

SHRDLU was a program written by Terry Winograd in 1968-70 at MIT. It enabled users to communicate with a computer and move objects in a virtual "blocks world" — a simplified environment containing colored blocks on a table. SHRDLU could handle instructions such as "pick up the green ball" and answer questions like "What is inside the black box." The main importance of SHRDLU was that it demonstrated that syntax (grammar), semantics (meaning), and reasoning about the world could be combined to produce a system that understands natural language. However, its limitation was that it only worked within its tiny virtual blocks world and could not understand language about the real world.

LUNAR was the classic example of a Natural Language database interface system. It used Augmented Transition Networks (ATNs) and Woods' Procedural Semantics to process queries about lunar rock samples from Apollo missions. LUNAR was capable of translating elaborate natural language expressions into database queries. Users could ask complex questions in plain English, and the system would automatically convert them into structured database operations. It achieved 78% accuracy — handling 78% of requests without errors.

Significance: Both systems were built during the 1960-1980 AI era of NLP. SHRDLU proved that combining multiple linguistic levels enables language understanding, while LUNAR demonstrated practical natural language interfaces for databases. Together, they showed NLP's potential but also revealed that scaling beyond limited domains remained a major challenge, motivating the shift to statistical approaches in the 1990s.*__
