#function to analyze the cat shetlter log file
def analyze_cat_shelter_log(filename):
    try:
        with open(filename, 'r') as file:   #open the specified log file for reading 
            our_cat_entries, intruder_doused_count, total_time_correct_cat = 0, 0, 0
            min_duration, max_duration = float('inf'), 0 # initialize variables to keep track of cat entries and statistics

            for line in file:
                #check for the end of the log file
                if line.strip() == 'END':
                    break
                #splits the line into parts (cat type, entry type , exit time)
                parts = line.strip().split(',')
                cat_type, entry_time, exit_time = parts

                entry_time = int(entry_time)
                exit_time = int(exit_time)
                duration = exit_time - entry_time

                if cat_type == 'OURS':   #update statistics based on cat type
                    our_cat_entries += 1
                    total_time_correct_cat += duration
                    min_duration = min(min_duration, duration)
                    max_duration = max(max_duration, duration)
                elif cat_type == 'THEIRS':
                    intruder_doused_count += 1
            #calculate average duration of our cat visits
            avg_duration = total_time_correct_cat / our_cat_entries if our_cat_entries else 0

            #display the analysis results
            print("Log File Analysis")
            print("==================")
            print(f"Cat Visits: {our_cat_entries}")
            print(f"Other Cats: {intruder_doused_count}")
            print()
            print(f"Total Time in House: {total_time_correct_cat // 60} Hours, {total_time_correct_cat % 60} Minutes")
            print()
            print(f"Average Visit Length: {avg_duration:.0f} Minutes")
            print(f"Longest Visit: {max_duration} Minutes")
            print(f"Shortest Visit: {min_duration} Minutes")

    except FileNotFoundError as e:   
        print(f"Error: File '{filename}' not found.")
    except Exception as e:     
        print(f"Error: {e}")


def main():    
    while True:    
         day = input("Enter which Log File do you want to Analyse (day 1, day 2, or day 3):\nday ")
         #determine the log file based on user input
         if day == '1':
             choice = 'shelter_2023-08-25.log'
             break
         elif day == '2':
             choice = 'shelter_2023-08-26.log'
             break
         elif day == '3':
             choice = 'shelter_2023-08-27.log'
             break
         else:
             #handle incorrect user input
             print('Wrong Entry! Please Try Again.')
             continue
         
    analyze_cat_shelter_log(choice)
         
main()
