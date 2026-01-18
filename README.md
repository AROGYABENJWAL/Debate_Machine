Debate Machine

Debate Machine is a small Python project that simulates a debate between two AI personas.
Each AI has its own name and philosophy, and they argue on a topic over multiple rounds, responding to and challenging each other’s points.

This project is meant to be simple, understandable, and easy to extend later with real AI models.

What this project does

Lets you create two AI debaters

Each AI has:

A name

A personality / philosophy

Takes a debate topic from the user

Runs:

Round 1 → Opening statements

Next rounds → Rebuttals (each AI responds to the other)

Runs completely in the terminal

Right now, the logic is rule-based.
The structure is designed so real AI models (like Ollama + Mistral) can be plugged in later.

Folder structure
Debate_Machine/
│
├── debate.py
├── README.md
└── .gitignore

Requirements

Python 3.8 or higher

No external libraries needed for the current version

Check Python:

python3 --version

How to run

Clone the repository:

git clone https://github.com/AROGYABENJWAL/Debate_Machine.git
cd Debate_Machine


Run the script:

python3 debate.py

How the debate works

When you run the script, you’ll be asked for:

Name of AI 1

Philosophy / personality of AI 1

Name of AI 2

Philosophy / personality of AI 2

Debate topic

Number of rounds

Debate flow

Round 1: Both AIs give their initial arguments

Round 2 and onwards:
Each AI responds to the other’s previous argument and tries to counter it using its own philosophy

Example
AI 1 Name: LogicAI
AI 1 Philosophy: Calm, logical, evidence-based

AI 2 Name: PassionAI
AI 2 Philosophy: Emotional, persuasive, value-driven

Topic: Should AI be regulated?

Why I made this

This project started as an experiment to understand:

Multi-agent interactions

Debate and rebuttal logic

How personality affects arguments

It’s also meant to be a base for a future AI-powered debate system.

Possible future improvements

Connect real AI models (Ollama / Mistral)

Save debate transcripts to a file

Add a judge or scoring system

Web interface

Voice output

Contributing

Feel free to fork the repo, experiment, and open a pull request if you add something interesting.

License

MIT License
