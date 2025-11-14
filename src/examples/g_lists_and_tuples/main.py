#main program
from lists import generate_lottery_numbers, display_lottery_numbers, generate_quick_pick_numbers, display_quick_pick_numbers, check_quick_pick_list_for_winner, \
    count_of_numbers_matched, handle_numbers_matched

def main():
    lottery_list = generate_lottery_numbers(7)
    display_lottery_numbers(lottery_list)    
    pick_list = generate_quick_pick_numbers(5, 7)
    display_quick_pick_numbers(pick_list)

    if(check_quick_pick_list_for_winner(pick_list, lottery_list)):
        print('Winning numbers!')
    else:
        print('No winner')

    for row_list in pick_list:
        count = count_of_numbers_matched(row_list, lottery_list)
        handle_numbers_matched(count)

if __name__ == "__main__":
    main()