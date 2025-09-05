# Minimal sanity check so you know Python is running.
print("Hello, LangGraph learner!")

# Optional: verify packages import without actually calling APIs.
try:
    import langgraph, langchain, openai  # type: ignore
    print("Imports OK.")
except Exception as e:
    print("Import problem:", e)
