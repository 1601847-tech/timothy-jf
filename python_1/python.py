# Function Purpose: Checks if a score is passing or failing.
def check_score(test_score):
    # Decision Making: check if score is 70 or higher
    if test_score >= 70:
        return "Pass"
    else:
        return "Fail"

# 1. Collection (List): A sequence of data
score_list = [85, 92, 76, 65, 58, 90, 73, 88, 45, 100]

# 2. Variable 1 (Integer): Counts the total number of items checked
total_checked = 0

# 3. Variable 2 (Boolean): Tracks if the overall class is doing well
class_is_doing_good = True

print("Checking scores:")

# Looping Structure: Repeatedly checks each score in the list
for single_score in score_list:
    
    # Custom Function Call: Uses the elements from the list
    result = check_score(single_score)
    
    # Simple Print: Using basic commas
    print("Score:", single_score, "Result:", result)
    
    total_checked = total_checked + 1
    
    # Decision Making: checks if anyone failed
    if result == "Fail":
        class_is_doing_good = False

print("Total scores checked:", total_checked)
print("Is class doing good?", class_is_doing_good)
