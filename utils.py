import json

from question import Question


def load_questions(filename):
    """
    вопросы считываются и раскладываются в экземпляры класса Question.
    Все экземпляры складываются в список questions
    :param filename:
    :return: список вопросов
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = []
    for item in data:
        text = item['q']
        difficulty = int(item['d'])
        right_answer = item['a']
        question = Question(text, difficulty, right_answer)
        questions.append(question)

    return questions

def build_statistics(questions):
    """
    Подсчет статистики
    :param questions:
    :return: кол-во правильных ответов и баллы
    """
    count = 0
    score = 0

    for question in questions:
        if question.is_correct():
            score = score + question.score
            count = count +1

    return f'Вот и всё! \n'\
            f'Отвечено {count} вопроса из 5\n' \
            f' Набрано баллов: {score}'
