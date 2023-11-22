import sys
from input_manager import get_input
from solutions import solution_for_day

def main():
    day = int(sys.argv[1]) 
    part = int(sys.argv[2])
    test = '--test' in sys.argv

    input_data = get_input(day,test=test)
    solution = solution_for_day(day, input_data,part)

    print(f"Solution for Day {day}, Part {part}{' (Test)' if test else ''}: {solution}")

if __name__ == '__main__':
    main()
