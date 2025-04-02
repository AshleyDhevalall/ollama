import ollama

# Replace with the desired model and prompt
response = ollama.chat(
    model="llama3:latest",  # Or any model supported by Ollama
    messages=[
        {"role": "user", "content": "Explain Newton's second law of motion"}
    ]
)

print(response["message"]["content"])