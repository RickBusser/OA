# Elevator simulator script.
import argparse

#•    Provide code that simulates an elevator. You are free to use any language.
#•    Upload the completed project to GitHub for discussion during interview.
#•    Document all assumptions and any features that weren’t implemented.
#•    The result should be an executable, or script, that can be run with the following inputs and generate the following outputs.
#                   Inputs: [list of floors to visit] (e.g. elevator start=12 floor=2,9,1,32)
#                   Outputs: [total travel time, floors visited in order] (e.g. 560 12,2,9,1,32)
#                   Program Constants: Single floor travel time: 10

travel_time = 10
# Change this to non_zero for time spent at each floor
stop_time = 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', help="Starting floor for elevator", type=int, required=True)
    parser.add_argument("--floor", help="CSV list of floors to visit", type=str, required=True)
    args = parser.parse_args()
    # Convert the csv list of floors to an array of integers
    # Adding exception handler here in case list of floors isn't all ints
    try:
        floors = []
        for s in args.floor.split(","):
            floors.append(int(s.strip()))
    except ValueError as msg:
        print(msg)
        exit(-1)

    current_floor = args.start
    total_time = 0
    total_floors_str = f'{args.start},' + args.floor
    for new_floor in floors:
        # use abs() here in case we're going down instead of up
        # assuming that opening and closing the doors takes 0 time.
        this_time = abs(current_floor - new_floor) * travel_time
        total_time += this_time + stop_time
        current_floor = new_floor

    print(f'Travel Time {total_time} Floors Visited {total_floors_str}')
