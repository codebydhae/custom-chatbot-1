#match best response to inputs given to chatbot
import json
from cdifflib import CSequenceMatcher

#load kb to program
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
        print(data)
    return data
#Test load function
#load_knowledge_base('knowledge_base.json')

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | Nooone:
    #n= 1st best response | cutoff= 60% accuracy
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["questions"] == question:
            return q["answer"]

def chat_bot():
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    while  True:
        user_input: str = input('You:  ')

        if user_input.lower() == 'quit':
            break

        #search json for best match
        best_match: str | None = find_best_match(user_input, [q["questions"] for  q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print('Bot: I don\'t know what to say. Can you teach me?')
            new_answer: str = input('Type the answer or "skip" to skip:   ')

            if new_answer.lower() == 'skip':
                knowledge_base["questions"].append({"question":  user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json',  knowledge_base)
                print('Bot: Thank you. Now I know!')

if __name__ == '__main__':
    chat_bot()