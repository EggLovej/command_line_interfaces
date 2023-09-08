#! /usr/bin/env python3.11

import argparse
from bisect import bisect
from plyer import notification
from time import sleep
from tqdm import tqdm

def make_parser():
    parser = argparse.ArgumentParser(
        prog = 'timer',
        description = ' A timer based on the pomodoro principal',
        epilog = 'Enjoy the program! :)',
    )

    parser.add_argument('-t', '--time', metavar='time', default=25,
        help = 'Sets the time for the work cycle',)

    parser.add_argument('-sb', '--short_break', metavar='short break', default=5,
        help = 'Sets the short break time',)

    parser.add_argument('-lb','--long_break', metavar='long break', default=30,
        help = 'Sets the long break time',)

    parser.add_argument('-c', '--cycles', metavar='cycles', default=4,
        help = 'Sets the amount of work cycles',)
    
    return parser

def send_notification(title, description, duration):
    notification.notify(
        title = title,
        message = description,
        app_icon = "pomodoro.ico",
        timeout = duration,
    )

def start_pomodoro(work_time, short_break, long_break, cycles):
    for cycle in range(1, cycles+1):
        print(f'Starting work cycle {cycle} of {cycles}')
        send_notification("Pomodoro Timer", f'Starting work cycle {cycle} of {cycles}', 5)
        countdown2(work_time, "Work cycle")

        if(cycle % 4 == 0):
            print(f'Time for a {long_break} minute break!')
            send_notification("Pomodoro Timer", f'Work cycle {cycle} of {cycles} completed! Time for a long break!', 5)
            countdown2(long_break, "Long break")

        else:
            print(f'Time for a {short_break} minute break!')
            send_notification("Pomodoro Timer", f'Work cycle {cycle} of {cycles} completed! Time for a short break!', 5)
            countdown2(short_break, "Short break")
    
def countdown2(minutes, desc):
    for i in tqdm(range(minutes * 60, 0, -1), desc=desc, ncols=100, colour='green', bar_format='{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]'):
        sleep(1)


def countdown(minutes):
    for i in range(minutes * 60, 0, -1):
        mins, secs = divmod(i, 60)
        time_str = f"{mins:02d}:{secs:02d}"
        print(time_str, end="\r")
        sleep(1)
    print("00:00", end="\r")


def create_timer(args):
    time = int(args.time)
    short_break = int(args.short_break)
    long_break = int(args.long_break)
    cycles = int(args.cycles)
    print('\n============== Creating timer ==============')
    print(f'Length of interval: {time} minutes')
    print(f'Length of short break: {short_break} minutes')
    print(f'Length of long break: {long_break} minutes')
    print(f'Amount of cycles: {cycles}')
    print(f'=========== Total amount of time ===========')
    total = 0
    for i in range(1, cycles + 1):
        total += time
        if(i % 4 == 0):
            total += long_break
        else:
            total += short_break
    print(f'{humanize_time(total * 60)}')


def humanize_time(seconds):
    time_cuts = [60, 60*60, 24*60*60]
    time_chunks = [('second', 1), ('minute', 60), ('hour', 60*60), ('day', 24*60*60)]

    unit, divisor = time_chunks[bisect(time_cuts, seconds)]
    num_units = seconds // divisor
    plural = 's' if num_units > 1 else ''
    return f'{num_units} {unit}{plural}'

if __name__ == '__main__':
    parser = make_parser()
    args = parser.parse_args()
    create_timer(args)
    start_pomodoro(int(args.time), int(args.short_break), int(args.long_break), int(args.cycles))
