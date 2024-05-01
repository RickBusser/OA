"""Module providing an elevator simulator script."""
import argparse
import sys



TRAVEL_TIME = 10
# Change this to non_zero for time spent at each floor
STOP_TIME = 0

def elevator_sim(start_floor:int, floors:list[int], floor_str:str):
    """ Provide code that simulates an elevator. You are free to use any language.
        Upload the completed project to GitHub for discussion during interview.
        Document all assumptions and any features that weren’t implemented.
        The result should be an executable, or script, that can be run with the following inputs and
            generate the following outputs.
            Inputs: [list of floors to visit] (e.g. elevator start=12 floor=2,9,1,32)
            Outputs: [total travel time, floors visited in order] (e.g. 560 12,2,9,1,32)
            Program Constants: Single floor travel time: 10
    """

    current_floor = start_floor
    total_time = 0
    total_floors_str = f'{start_floor},' + floor_str
    for new_floor in floors:
        # use abs() here in case we're going down instead of up
        # assuming that opening and closing the doors takes 0 time.
        this_time = abs(current_floor - new_floor) * TRAVEL_TIME
        total_time += this_time + STOP_TIME
        current_floor = new_floor

    print(f'Travel Time {total_time} Floors Visited {total_floors_str}')

def main():
    """
        main function for elevator script.
        responsible for parsing arguments and calling elevator function
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', help="Starting floor for elevator", type=int, required=True)
    parser.add_argument("--floor", help="CSV list of floors to visit", type=str, required=True)
    args = parser.parse_args()
    # Convert the csv list of floors to an array of integers
    # Adding exception handler here in case list of floors isn't all ints
    try:
        floors = [int(s.strip()) for s in args.floor.split(",")]
        #equivalent to the following lines
        #    floors = []
        #    for s in args.floor.split(","):
        #        floors.append(int(s.strip()))
    except ValueError as msg:
        print(msg)
        sys.exit(-1)
    elevator_sim(args.start, floors, args.floor)

if __name__ == '__main__':
    main()
