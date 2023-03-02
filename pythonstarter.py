import openai

openai.api_key = "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"
i=1
model_engine = "text-davinci-003"
prompt = "what question do you wish people would ask you?"

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

while i < 10:
    response = completion.choices[0].text
    print("response:" + response)
    prompt = "What time is it?"
    print("prompt:" + prompt)
    i=i+1



