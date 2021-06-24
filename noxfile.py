
locations = "insult_ai", "tests", "noxfile.py", "docs/conf.py"

@nox.session(python=["3.9"])
def docs(session: Session) -> None:
    """Build the documentation."""
    session.install("sphinx", "sphinx_autodoc_typehints")
    session.run("sphinx-build", "docs", "docs/_build")

@nox.session(python="3.9")
def docs(session: Session) -> None:
    """Build the documentation."""
    session.run("poetry", "install", "--no-dev", external=True)
    session.install( "sphinx", "sphinx-autodoc-typehints",'sphinx-click')
    session.run("sphinx-build", "docs", "docs/_build")
