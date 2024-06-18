
# ICT 09 – Programming 1

# FINAL PROJECT

# 3. Typing master:
# - This should show the user some text, and then challenge them to type it — while timing
# them and scoring them on for accuracy 

import time

def typing_master():
    text_to_type = "The quick brown fox jumps over the lazy dog."
    print("Type the following text as fast as you can:")
    print(text_to_type)

    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()

    time_taken = end_time - start_time
    accuracy = sum(1 for a, b in zip(text_to_type, user_input) if a == b) / len(text_to_type) * 100

    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_master()
