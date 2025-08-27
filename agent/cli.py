import typer
from rich import print


app = typer.Typer(help="AI Coding Agent CLI")


@app.command()
def start(goal: str = typer.Option(..., prompt=True, help="What should the agent build?")):
    """Start the AI coding agent with a goal description."""
    print("[bold green]Starting AI Coding Agent[/bold green]")
    from .agent import run_agent  # Lazy import to avoid model init on --help
    run_agent(goal)


if __name__ == "__main__":
    app()

