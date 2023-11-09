import os
import pandas as pd
from openai import OpenAI
from openai.types.chat import ChatCompletionMessage


dataset_path = 'data/car_details_v4.csv'

conversation = [
    {
        'role': 'system',
        'content': 'You are assistant that helps to chose the car. Database of available cars gonna be passed in next messages'
    }
]


def load_data() -> None:
    data = pd.read_csv(dataset_path)
    conversation.append({'role': 'system', 'content': " ".join([f"Row {i}: {', '.join(f'{col}: {val}' for col, val in row.items())}" for i, row in data.iterrows()])})


def generate_answer() -> ChatCompletionMessage:
    client = OpenAI(api_key="GigaSecretInformation;-)")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    return completion.choices[0].message


def communication() -> None:
    load_data()
    print('Press "Q" to finish conversation')
    question = ''

    while question != 'q':
        question = input()
        conversation.append({'role': 'assistant', 'content': question})
        conversation.append({'role': 'assistant', 'content': generate_answer().content})
        os.system('cls')
        print_conversation()


def print_conversation() -> None:
    for ele in conversation:
        if ele['role'] == 'system':
            continue
        print(f'{"[Chat]" if ele["role"] == "assistant" else "[Chatter]"} {ele["content"]}')


if __name__ == '__main__':
    communication()
