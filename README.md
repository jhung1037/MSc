# Theatrical Script Generator

## Description
This script generator is designed to create more human-like conversations. It is powered by GPT-4 and integrated with the LangChain framework. The example materials are excerpts from the first scene of *Summer and Smoke* by Tennessee Williams. When run, it recreates a new story between the two main characters.

## Inception
Although LLMs are nearly flawless at question-answering tasks nowadays, they still struggle to generate a theatrical-approved script or a lifelike conversation. Therefore, this experiment is conducted to explore the possibility of simulating cognitive processes by employing acting techniques with LLMs. Hoping that one day this realisation will go beyond merely humanising conversations or enhancing script generators; it will extend to perfecting human mind simulation.

## Installation
```
pip install openai 
pip install langchain 
pip install chromadb
```
**Optional:**
```
pip install tiktoken
```

## To Run the Code
1.  Ensure you input your OpenAI API key into `API_Key.py`.
2.  Execute `Main.py`.
3.  A `Script.txt` file will be generated. The length of the script can be customised in `Main.py`.

## Individual Code file Description
1.  `Main.py` brings together the code, orchestrating character interactions and recording lines into a script.
2.  `Chatbot.py` houses the core structure of the created chatbots, with GPT-4 and LangChain operating within.
3.  `Prompts.py` serves as the primary template for human-like thinking process prompting.
4.  The `Settings` folder contains necessary data for character initialisation.
5.  `TokenCounter.py` optimises GPT-4 usage. It was originally designed to manage the number of tokens passed to GPT-4 without compromising the generated content.

## Example Outcome
```
John: Playing by the fountain again?
Alma: Just pondering eternity.
John: Eternity with angels?
Alma: Sometimes, even angels need company.
John: Ever need company from mere mortals?
Alma: Mortals have their own charm.
John: Ever seen a mortal's guardian angel?
Alma: They're closer than you think.
John: Is that so?
Alma: Sometimes, the smallest gestures show them.
John: You ever find handkerchiefs falling from the sky?
Alma: Perhaps it's heaven's way of looking out.
John: Or maybe it's someone much closer?
Alma: Maybe it is.
John: I remember making wishes here.
```
