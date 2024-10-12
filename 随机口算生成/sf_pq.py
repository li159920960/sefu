import operator
import random
import re


# 生成随机的口算题目
def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*', '/'])
    if operator == '/':
        num1 = num2 if num1 < num2 else num1  # 确保除数不为0
    question = f"{num1} {operator} {num2} =?"
    return question


# 判断答案是否正确
def check_answer(question, answer):
    match = re.search(r'([\d\s+*\-/]+)=?',question)
    if match:
        expr = match.group(1).strip()
        try:
            if operator == '/':
                # 如果是除法，确保结果为整数
                a, b = map(int, expr.split())
                expected_answer = a // b
            else:
                expected_answer = eval(expr)

            return answer == expected_answer
        except:
            return False
    return False


# 玩家玩起小猿口算
def play_arithmetic(question_count):
    print("欢迎来到小猿口算游戏！")
    print("系统将随机生成口算题目，请输入答案。\n")
    correct_count = 0
    for _ in range(question_count):
        question = generate_question()
        print(question)
        answer = input("答案是：")
        if not answer.isdigit():
            print("请输入一个整数答案。")
            continue
        correct = check_answer(question, int(answer))
        if correct:
            print("正确！")
        else:
            parts = question.split(' =?')
            expr = parts[0]
            try:
                expected_answer = eval(expr)
            except:
                # 如果eval失败，尝试手动处理除法情况
                if '/' in expr:
                    a, b = map(int, expr.split())
                    expected_answer = a // b
                else:
                    expected_answer = None
            if expected_answer is not None:
                print(f"错误！正确答案是：{expected_answer}")
            else:
                print("无法确定正确答案。")
    accuracy = correct_count / question_count * 100
    print(f"你一共回答了{question_count}道题，正确{correct_count}道题，正确率为{accuracy:.2f}%")


# 程序入口
num_questions = int(input("请输入你要回答的题目数量："))
play_arithmetic(num_questions)
