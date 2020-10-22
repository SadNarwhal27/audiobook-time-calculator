"""
Audiobook Time Calculator
Travis Schall
"""


def time_input():
    """
    Takes in number of hours and minutes left in the book along with narration speed
    """
    norm_hours = int(input('Hours: '))
    norm_minutes = int(input('Minutes: '))
    speed = float(input('Narration Speed: '))
    calculate_time(norm_hours, norm_minutes, speed)


def calculate_time(norm_hours, norm_minutes, speed):
    """
    Calculates the new amount of time left using normal time variables and narration speed
    :param norm_hours: amount of hours left in the book
    :param norm_minutes: amount of minutes left in the book
    :param speed: narration speed rate
    """
    norm_time = norm_minutes + (norm_hours * 60)
    new_time = norm_time / speed

    new_minutes = int(new_time % 60)

    # Keeps the new hours to 0 if there is less than 1 hour left in the book
    new_hours = 0
    if new_time / 60 > 1:
        new_hours = int(new_time / 60)

    print('\nOriginal Time: {}:{}\nNew Time: {}:{}'.format(norm_hours, norm_minutes, new_hours, new_minutes))


def main():
    """
    Main function of the program
    """
    time_input()


if __name__ == '__main__':
    main()
