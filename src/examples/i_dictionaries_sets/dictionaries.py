#Create dictionaries
survey_questions = \
{
    '2.1': 'The texts, assigned readings, and other course resources help me learn the course material.',
    '2.2': 'Clear instructions are provided',
    '2.3': 'Tests, papers, assignments, and or other activities include clear instructions.',
    '2.4': 'Uses instructional technology',
    '2.5': 'Tests, papers, assignments, or other activities'
}

survey_question_options = \
{
    1: 'Never',
    2: 'Sometimes',
    3: 'More',
    4: 'More more',
    5: 'Always',
    6: 'Always Always'
}

survey_responses_list = [] # [1, '2.1', 3] responses for all the students in the course
#survey_response_results_total = {'2.1': 0, '2.2': 0, '2.3': 0, '2.4': 0, '2.5': 0}
#survey_response_results = {} # {'2.1': 4, '2.2': 3, '2.3':5, '2.4':2, '2.5': 3}

def test_config():
    return True

def create_dictionary():
    phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}
    print(phonebook)

def loop_dictionary_w_for():
    phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}

    for key in phonebook:
        print(key, phonebook[key])

def loop_dictionary_w_for_items():
    phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}

    for key, value in phonebook.items():
        print(key, value)

def loop_dictionary_w_values():
    phonebook = {'555-1111':'Chris', '555-2222':'Katie', '555-3333':'Joanne'}

    for value in phonebook.values():
        print(value)

def display_menu():
    print('1-Enter Survey Responses')
    print('2-Get Survey Results')
    print('3-Exit')

def run_menu():
    option = 0

    while option != 3:
        display_menu();
        option = int(input("Enter option: "))
        handle_menu_option(option)

def handle_menu_option(option):

    if(option == 1):
        display_survey_questions()
    elif(option == 2):
        survey_response_result = tabulate_survey_response_results(survey_responses_list)

        average = get_course_average(survey_response_result)

        print('Course average: ', average)

        rating = get_faculty_rating(average)

        print('Rating: ', rating)

    elif(option == 3):
        print('Exiting...')
    else:
        print('Invalid option')


def display_survey_questions():
    survey_id = 1

    for question_id, question_text in survey_questions.items():
        print(question_id, question_text)

        for option, value in survey_question_options.items():
            print(option, value)

        capture_survey_question_response(survey_id, question_id)

        survey_id += 1

def capture_survey_question_response(survey_id, question_id):
    response = int(input("Enter response: "))
    survey_responses_list.append([survey_id, question_id, response]) # [[1, 2.1, 2], [1, 2.2, 5]]
    print(survey_responses_list)

def tabulate_survey_response_results(survey_responses_list):
    cnt = 0
    survey_response_results_total = {'2.1': 0, '2.2': 0, '2.3': 0, '2.4': 0, '2.5': 0}
    survey_response_results = {} # {'2.1': 4, '2.2': 3, '2.3':5, '2.4':2, '2.5': 3}
                                

    for response in survey_responses_list: #[1, '2.1', 4]
        survey_response_results_total[response[1]] += response[2]
        if '2.5' == response[1]:
            cnt += 1

    for question_id, total in survey_response_results_total.items():
        survey_response_results[question_id] = total / cnt
        print(survey_response_results)

    return survey_response_results

def get_course_average(survey_response_result):

    total_average = 0
    total = 0

    for key in survey_response_result:
        total += survey_response_result[key]

    total_average = total / len(survey_response_result)

    return total_average

def get_faculty_rating(ratio):
    
    if(ratio <= 6 and ratio >= 5.5):
        return 'Excellent'
    elif(ratio >= 5 and ratio < 5.5):
        return 'Very Good'
    elif(ratio >= 4) and ratio < 5:
        return 'Good'
    elif(ratio >= 3 and ratio < 4):
        return 'Needs Improvement'
    elif(ratio <= 3) and ratio >= 0:
        return 'Unacceptable'
    else:
        return "Invalid Value"

