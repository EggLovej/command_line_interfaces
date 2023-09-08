import argparse
import psutil

def create_parser():
    parser = argparse.ArgumentParser(
        prog = 'cpu_tracker',
        description = 'A program to track CPU usage',
        epilog = 'Enjoy the program! :)',
    )
    parser.add_argument('-i', '--interval', metavar='interval', default=10,
        help = 'As cpu usage is calculated over an interval, it is recommended to provide a time interval in seconds. Default is 10 seconds.'
    )
    return parser

def print_cpu_usage(interval):
    print(f'Average CPU usage over the last {interval} seconds: {get_cpu_usage(interval)}%')

def get_cpu_usage(interval):
    return psutil.cpu_percent(interval=interval)
    

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    print_cpu_usage(int(args.interval))