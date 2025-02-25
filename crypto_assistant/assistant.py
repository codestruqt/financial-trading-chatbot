import openai
from retrieval import retrieve_context

def generate_crypto_summary(query):
    context = retrieve_context(query)
    prompt = f"Using the following context:\n{context}\n\nPlease provide a brief summary for the crypto project: {query}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a knowledgeable crypto market research assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.5
    )
    summary = response.choices[0].message.content.strip()
    return summary
