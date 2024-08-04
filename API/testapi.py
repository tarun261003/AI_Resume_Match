from config import OPEN_API_KEY
from openai import OpenAI

def get_result(prompt):
    completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  temperature=0.7,
  n=1,
  messages=[
    {"role": "system", "content": "You are helping me in AI Resume Match maker Project"},
    {"role": "user", "content": prompt}
  ]
  
)
    # print("Rate limit:", completion.headers.get("x-ratelimit-limit"))
    # print("Remaining requests:", completion.headers.get("x-ratelimit-remaining"))
    # print("Reset time:", completion.headers.get("x-ratelimit-reset"))

    return completion.choices[0].message.content

if __name__=="__main__":
    client = OpenAI(api_key=OPEN_API_KEY)
    print(get_result('Hello Gpt'))
    # for i in client.models.list():
        # print(i.id)