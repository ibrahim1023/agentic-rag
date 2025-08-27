import sys
from dotenv import load_dotenv

load_dotenv()


def main():
    from agent.agent import run_agent

    print("=" * 60)
    print("🤖 AI Coding Agent")
    print("=" * 60)

    if len(sys.argv) > 1:
        goal = " ".join(sys.argv[1:]).strip()
    else:
        goal = input("Enter your coding goal: ").strip()

    if not goal:
        print("No goal provided. Exiting.")
        return

    run_agent(goal)


if __name__ == "__main__":
    main()