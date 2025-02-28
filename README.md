# Flashy Language Learning App
Flashy is a simple yet effective flashcard-based language learning application. It is designed to help users learn new words between two languages (e.g., French and English). The program tracks learning progress by recording which words have been learnt and provides a mechanism to continue learning the remaining words.
## Features:
1. **Language Learning Through Flashcards**:
    - Displays flashcards with a word in one language on the front and its translation on the back.
    - Supports any two languages (default: French → English).

2. **Progress Tracking**:
    - The app maintains a list of remaining words to learn and automatically saves progress to a file (`Left_for_learning.csv`).

3. **Customizable Word List**:
    - Users can replace or modify the CSV file with their own set of words and languages.

4. **Scoring**:
    - Displays the number of words successfully learnt over the total.

## How to Use:
1. **Adding Your Word List**:
    - Locate the `data/french_words.csv` file in the `data/` directory.
    - Replace or edit this file with your own CSV file. Ensure the file includes two columns with the headers `French` and `English` (or any other two languages you are learning). Example:
``` 
     French,English
     Bonjour,Hello
     Merci,Thank you
```
- If you're resuming learning, the app will automatically load `Left_for_learning.csv` (if it exists). You can delete this file to restart learning from the main CSV.

1. **Running the App**:
    - Launch the program, and flashcards will automatically appear.
    - The front side of the card will show a word in one language (e.g., French).
    - After 3 seconds, the card will flip to reveal the translation in the second language (e.g., English).

2. **Using the Buttons**:
    - **Correct Button (✔️)**: Click this button when you've successfully learnt a word. It will remove the word from the learning list and update your progress.
    - **Wrong Button (❌)**: Click this button to skip a word and move to the next card.

3. **Progress and Saving Data**:
    - As you learn words, they are removed from the learning list, and the app updates `Left_for_learning.csv` with the remaining words.
    - Ensure the program has file-writing permissions to update the progress.

## How It Works:
1. **Reading Word Data**:
    - The app first tries to load `Left_for_learning.csv` (list of unlearnt words).
    - If the file does not exist, it loads the `french_words.csv` file as the starting point.

2. **Displaying Cards**:
    - Each flashcard randomly displays a word from the list in one language.
    - After 3 seconds, the card flips to reveal the translation.

3. **Tracking Progress**:
    - When the learner marks a word as "learnt" by clicking the correct button, the word is removed from the learning list.
    - The rest of the word list is saved as `Left_for_learning.csv` for future sessions.

4. **Customizability**:
    - By updating the `french_words.csv` file, the app's content can be tailored to any pair of languages or topics (e.g., technical terms, travel vocabulary, etc.).

## Folder Structure:
- **`data/french_words.csv` **: Contains the initial word list for learning.
- **`data/Left_for_learning.csv` **: Automatically generated file that includes the words not yet learnt.
- **`images`**: Contains images for the card backgrounds (front and back) and buttons (correct/wrong).

## Requirements:
- Python 3.10 or above
- Required Python libraries:
    - `pandas`
    - `tkinter`

- Images:
    - Ensure the `images/` folder contains `card_front.png`, `card_back.png`, `wrong.png`, and `right.png` for the program UI to function correctly.

Install dependencies using `pip` (if not already installed):
``` bash
pip install pandas
```
## Example Workflow:
1. Start with a CSV file (`french_words.csv`) containing your desired vocabulary list.
2. Launch the program.
3. Use the `✔️` button when you have learnt a word or the `❌` button to skip a word.
4. Exit the program when done. Your progress will be saved to `Left_for_learning.csv`.
5. Restart the program anytime to pick up where you left off.

Enjoy learning new languages with Flashy!
