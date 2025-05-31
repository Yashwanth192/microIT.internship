#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox

class Question:
    def __init__(self, prompt, choices, answer):
        self.prompt = prompt
        self.choices = choices  # List like ['Earth', 'Mars', ...]
        self.answer = answer    # Correct choice letter (e.g., 'B')

class QuizGameGUI:
    def __init__(self, root, questions_by_category):
        self.root = root
        self.root.title("Quiz Game")
        self.questions_by_category = questions_by_category
        self.score = 0
        self.current_question_index = 0
        self.selected_category = None
        self.questions = []
        self.user_answers = []

        self.create_category_selection()

    def create_category_selection(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()

        label = tk.Label(self.root, text="Select a category", font=("Arial", 18))
        label.pack(pady=20)

        for cat in self.questions_by_category:
            btn = tk.Button(self.root, text=cat, font=("Arial", 14),
                            command=lambda c=cat: self.start_quiz(c))
            btn.pack(pady=5)

    def start_quiz(self, category):
        self.selected_category = category
        self.questions = self.questions_by_category[category]
        self.score = 0
        self.current_question_index = 0
        self.user_answers = []
        self.show_question()

    def show_question(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()

        if self.current_question_index >= len(self.questions):
            self.show_results()
            return

        q = self.questions[self.current_question_index]

        prompt_label = tk.Label(self.root, text=q.prompt, font=("Arial", 16), wraplength=500)
        prompt_label.pack(pady=20)

        self.selected_answer = tk.StringVar(value="")

        for idx, choice in enumerate(q.choices):
            # choices are like 'A) Earth', so just show full text
            rb = tk.Radiobutton(self.root, text=choice, variable=self.selected_answer, value=choice[0],
                                font=("Arial", 14))
            rb.pack(anchor='w', padx=40)

        btn_submit = tk.Button(self.root, text="Submit Answer", font=("Arial", 14),
                               command=self.submit_answer)
        btn_submit.pack(pady=20)

        # Show progress
        progress = tk.Label(self.root, text=f"Question {self.current_question_index + 1} of {len(self.questions)}",
                            font=("Arial", 12))
        progress.pack()

    def submit_answer(self):
        answer = self.selected_answer.get()
        if not answer:
            messagebox.showwarning("No answer", "Please select an answer before submitting.")
            return

        q = self.questions[self.current_question_index]
        self.user_answers.append(answer)
        if answer == q.answer:
            self.score += 1
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            correct_text = next(c for c in q.choices if c.startswith(q.answer))
            messagebox.showinfo("Wrong!", f"Wrong! Correct answer is: {correct_text}")

        self.current_question_index += 1
        self.show_question()

    def show_results(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()

        result_label = tk.Label(self.root, text=f"Quiz Finished!\nYour score: {self.score} / {len(self.questions)}",
                                font=("Arial", 18))
        result_label.pack(pady=20)

        review_btn = tk.Button(self.root, text="Review Answers", font=("Arial", 14),
                               command=self.review_answers)
        review_btn.pack(pady=10)

        restart_btn = tk.Button(self.root, text="Restart", font=("Arial", 14),
                                command=self.create_category_selection)
        restart_btn.pack(pady=10)

        quit_btn = tk.Button(self.root, text="Quit", font=("Arial", 14),
                             command=self.root.quit)
        quit_btn.pack(pady=10)

    def review_answers(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()

        label = tk.Label(self.root, text="Review Answers", font=("Arial", 18))
        label.pack(pady=20)

        canvas = tk.Canvas(self.root)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for i, q in enumerate(self.questions):
            ua = self.user_answers[i]
            correct = q.answer
            is_correct = ua == correct
            fg_color = "green" if is_correct else "red"

            q_label = tk.Label(scrollable_frame, text=f"Q{i+1}: {q.prompt}", font=("Arial", 14), wraplength=500)
            q_label.pack(anchor='w', pady=5)

            ua_text = next((c for c in q.choices if c.startswith(ua)), "No answer")
            correct_text = next(c for c in q.choices if c.startswith(correct))

            answer_label = tk.Label(scrollable_frame, text=f"Your answer: {ua_text} - {'Correct' if is_correct else 'Wrong'}",
                                    fg=fg_color, font=("Arial", 12))
            answer_label.pack(anchor='w', padx=20)

            if not is_correct:
                correct_label = tk.Label(scrollable_frame, text=f"Correct answer: {correct_text}",
                                         fg="green", font=("Arial", 12, "italic"))
                correct_label.pack(anchor='w', padx=20)

            sep = tk.Label(scrollable_frame, text="-" * 70)
            sep.pack()

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        back_btn = tk.Button(self.root, text="Back to Results", font=("Arial", 14),
                             command=self.show_results)
        back_btn.pack(pady=10)

# Example questions same as before
questions_by_category = {
    "Science": [
        Question(
            "What planet is known as the Red Planet?",
            ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
            "B"
        ),
        Question(
            "What gas do plants absorb from the atmosphere?",
            ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"],
            "C"
        ),
    ],
    "History": [
        Question(
            "Who was the first president of the United States?",
            ["A) Abraham Lincoln", "B) George Washington", "C) Thomas Jefferson", "D) John Adams"],
            "B"
        ),
        Question(
            "In which year did World War II end?",
            ["A) 1945", "B) 1939", "C) 1918", "D) 1963"],
            "A"
        ),
    ]
}

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x500")
    app = QuizGameGUI(root, questions_by_category)
    root.mainloop()


# In[ ]:




