def main():
    try:
        # open'students.txt' in read mode
        with open('students.txt', 'r') as file:
            total_score = 0  # Keeps track of the total score of all students
            count = 0        # Counts how many students there are
            top_scorer = ''  # Stores the name of the top-scoring student
            top_score = -1   # Stores the highest score found so far

            # Go through each line in the file
            for line in file:
                name, score_str = line.strip().split(',')  # Split the line into name and score
                score = int(score_str)  # Convert the score from string to integer
                total_score += score    # Add the score to the total
                count += 1              # Increase the student count

                # Check if this student has the highest score so far
                if score > top_score:
                    top_score = score      # Update the top score
                    top_scorer = name      # Update the name of the top scorer

            # After going through the file, check if there were any students
            if count == 0:
                print("No student data found.")
            else:
                average = total_score / count  # Calculate the average score
                print(f"Average Score: {average:.1f}")  # Print average score (1 decimal place)
                print(f"Top Scorer: {top_scorer} with a score of {top_score}")  # Print top scorer info

    except FileNotFoundError:
        # If the file does not exist, show an error message
        print("Error: students.txt file not found.")
    except Exception as e:
        # Catch and show any other unexpected errors
        print(f"An error occurred: {e}")

# This makes sure the main() function only runs when this file is executed directly
if __name__ == "__main__":
    main()
