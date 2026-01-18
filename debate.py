import subprocess
import sys

def run_mistral(system_prompt, user_prompt):
    full_prompt = f"""
SYSTEM:
{system_prompt}

USER:
{user_prompt}
"""

    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=full_prompt,
        text=True,
        capture_output=True   # <-- THIS WAS MISSING
    )

    return result.stdout


def main():
    print("=== AI Debate Machine ===\n")

    topic = input("Enter debate topic: ").strip()

    ai1_name = input("Enter AI 1 name: ").strip()
    ai1_personality = input(f"Define {ai1_name}'s personality/philosophy: ").strip()

    ai2_name = input("Enter AI 2 name: ").strip()
    ai2_personality = input(f"Define {ai2_name}'s personality/philosophy: ").strip()

    ai1_system = f"""
You are {ai1_name}.
Personality / Philosophy:
{ai1_personality}

You argue FOR the motion.
Be confident, structured, and persuasive.
"""

    ai2_system = f"""
You are {ai2_name}.
Personality / Philosophy:
{ai2_personality}

You argue AGAINST the motion.
Be critical, logical, and challenging.
"""

    print("\n--- ROUND 1: Opening Statements ---\n")

    ai1_response = run_mistral(
        ai1_system,
        f"Debate topic: {topic}\nPresent your opening argument FOR the motion."
    )
    print(f"\n{ai1_name}:\n{ai1_response}")

    ai2_response = run_mistral(
        ai2_system,
        f"Debate topic: {topic}\nPresent your opening argument AGAINST the motion."
    )
    print(f"\n{ai2_name}:\n{ai2_response}")

    round_num = 2

    try:
        while True:
            print(f"\n--- ROUND {round_num}: Rebuttals ---\n")

            ai1_response = run_mistral(
                ai1_system,
                f"""
Debate topic: {topic}

Opponent's last argument:
{ai2_response}

Respond with a rebuttal. Challenge weaknesses and defend your position.
"""
            )
            print(f"\n{ai1_name}:\n{ai1_response}")

            ai2_response = run_mistral(
                ai2_system,
                f"""
Debate topic: {topic}

Opponent's last argument:
{ai1_response}

Respond with a rebuttal. Object strongly based on your philosophy.
"""
            )
            print(f"\n{ai2_name}:\n{ai2_response}")

            round_num += 1

    except KeyboardInterrupt:
        print("\n\nDebate stopped by user.")
        sys.exit(0)


if __name__ == "__main__":
    main()

