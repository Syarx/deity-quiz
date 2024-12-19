import itertools
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import defaultdict

# Import data from separate files
from data.constants import NUM_QUESTIONS, NUM_ANSWERS, DOMAINS
from data.gods import (
    gods_by_domains,
    gods_by_title,
    gods_by_race,
    gods_by_class,
    gods_by_alignment,
)
from data.questions import questions, answers
from data.points import custom_points
from data.answers import answer_domains

# Initialize points for domains
domain_points = {domain: 0 for domain in DOMAINS}


class QuizApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quiz Application")
        self.root.geometry("1600x960")

        self.extra_answers = []
        self.row = 2
        self.col = 0
        self.current_question = 1
        self.first_choice = None
        self.second_choice = None

        # Main question window
        self.question_frame = tk.Frame(self.root, width=1500, height=900)
        self.question_frame.grid(row=0, column=0, padx=40, pady=10, sticky="nsew")

        self.question_title = tk.Label(
            self.question_frame,
            text=f"Question {self.current_question}",
            font=("Arial", 24),
            anchor="center",
        )
        self.question_title.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")
        self.question_label = tk.Label(
            self.question_frame,
            text=questions[self.current_question - 1],
            font=("Arial", 20),
            wraplength=1450,
            anchor="w",
            justify="left",
        )
        self.question_label.grid(row=1, column=0, columnspan=2, pady=10, sticky="w")

        self.answer_buttons = []
        for key, value in answers.items():
            if key[0] == self.current_question:
                button = tk.Button(
                    self.question_frame,
                    text=value,
                    font=("Arial", 14),
                    width=65,
                    height=4,
                    wraplength=650,
                    anchor="center",
                    bg="SystemButtonFace",
                    command=lambda i=key[1]: self.select_answer(i),
                )
                button.grid(row=self.row, column=self.col, padx=5, pady=5, sticky="w")
                self.row += 1
                if self.row == 6:
                    self.row = 2
                    self.col = 1
                self.answer_buttons.append(button)

        self.next_button = tk.Button(
            self.question_frame,
            text="Next",
            bg="light gray",
            width=20,
            height=2,
            state=tk.DISABLED,
            command=self.next_question,
        )
        self.next_button.grid(row=7, column=0, columnspan=2, pady=(15, 10))

        self.root.mainloop()

    def select_answer(self, answer_index):
        if self.first_choice is None:
            self.first_choice = answer_index
            self.answer_buttons[answer_index - 1].configure(bg="green")
            self.next_button.configure(state=tk.NORMAL, bg="yellow")
        elif self.first_choice == answer_index:
            if self.second_choice is not None:
                self.first_choice = self.second_choice
                self.second_choice = None
                self.answer_buttons[answer_index - 1].configure(bg="SystemButtonFace")
            else:
                self.first_choice = None
                self.answer_buttons[answer_index - 1].configure(bg="SystemButtonFace")
                self.next_button.configure(state=tk.DISABLED, bg="SystemButtonFace")
        elif self.second_choice == answer_index:
            self.second_choice = None
            self.answer_buttons[answer_index - 1].configure(bg="SystemButtonFace")
        elif self.first_choice is not None and self.second_choice is None:
            self.second_choice = answer_index
            self.answer_buttons[answer_index - 1].configure(bg="green")
        elif self.first_choice != answer_index and self.second_choice != answer_index:
            print("Error")

    def calculate_points(self, first_choice, second_choice):
        first_points = custom_points.get((self.current_question, first_choice), 6) * 2
        if second_choice is not None:
            second_points = custom_points.get((self.current_question, second_choice), 6)

        if self.current_question < 37:
            # Distribute points to multiple domains for the first choice
            first_domains = answer_domains[(self.current_question, first_choice)]
            for domain in first_domains:
                domain_points[domain] += first_points

            # Distribute points to multiple domains for the second choice
            if second_choice is not None:
                second_domains = answer_domains[(self.current_question, second_choice)]
                for domain in second_domains:
                    domain_points[domain] += second_points

        else:
            if self.current_question > 36:
                temp = answers[(self.current_question, first_choice)]
            self.extra_answers.append({temp: int(first_points / 2)})
        # self.update_graph()

    def update_graph(self):
        self.ax.clear()
        self.ax.bar(domain_points.keys(), domain_points.values(), color="skyblue")
        self.ax.set_xticklabels(domain_points.keys(), rotation=90)
        self.ax.set_title("Domain Points")
        self.figure.tight_layout()
        self.bar_chart.draw()

    def next_question(self):
        self.calculate_points(self.first_choice, self.second_choice)
        if self.current_question == NUM_QUESTIONS:
            self.show_final_results()
            return

        self.current_question += 1
        self.first_choice = None
        self.second_choice = None
        self.question_title.configure(text=f"Question {self.current_question}")
        self.question_label.configure(text=questions[self.current_question - 1])
        self.next_button.configure(state=tk.DISABLED, bg="SystemButtonFace")

        if self.current_question == 38:
            for i in range(3):
                button = tk.Button(
                    self.question_frame,
                    text="",
                    font=("Arial", 14),
                    width=65,
                    height=4,
                    wraplength=650,
                    anchor="center",
                    bg="SystemButtonFace",
                    command=lambda i=i: self.select_answer(8 + i),
                )
                if i == 0:
                    self.row = 6
                    self.col = 0
                button.grid(row=self.row, column=self.col, padx=5, pady=5, sticky="w")
                self.row += 1
                if self.row == 7:
                    self.row = 5
                    self.col = 1
                self.answer_buttons.append(button)
        if self.current_question == 39:
            self.answer_buttons[9].destroy()
            self.answer_buttons.pop()

        for i, button in enumerate(self.answer_buttons):
            button.configure(
                text=answers[self.current_question, i + 1],
                bg="SystemButtonFace",
            )

    def get_god_title(self, god_name):
        return gods_by_title.get(god_name, "God not found")

    def show_frame_2(self, sorted_gods):
        self.question_frame.destroy()

        first_three = list(itertools.islice(sorted_gods.items(), 3))

        self.question_frame = tk.Frame(self.root, width=1500, height=250)
        self.question_frame.pack(side=tk.TOP, padx=5, pady=10)

        for i, (god, value) in enumerate(first_three):
            if (
                i == 0
                and first_three[0][1] == first_three[1][1]
                and first_three[0][1] == first_three[2][1]
            ):
                self.question_title = tk.Label(
                    self.question_frame,
                    text=f"Your preferred Gods are {first_three[0][0]}, {first_three[1][0]} and {first_three[2][0]}. They are {self.get_god_title(first_three[0][0]), {self.get_god_title(first_three[1][0])} and {self.get_god_title(first_three[2][0])}}",
                    font=("Arial", 24),
                    wraplength=1000,
                    anchor="w",
                    justify="left",
                )
                self.question_title.pack(pady=20)
            if (
                i == 0
                and first_three[0][1] == first_three[1][1]
                and first_three[0][1] != first_three[2][1]
            ):
                self.question_title = tk.Label(
                    self.question_frame,
                    text=f"Your preferred Gods are {first_three[0][0]} and {first_three[1][0]}. They are {self.get_god_title(first_three[0][0]), {self.get_god_title(first_three[1][0])} and {self.get_god_title(first_three[2][0])}}",
                    font=("Arial", 24),
                    wraplength=1400,
                    anchor="w",
                    justify="left",
                )
                self.question_title.pack(pady=20)
            if i == 0 and first_three[0][1] != first_three[1][1]:
                self.question_title = tk.Label(
                    self.question_frame,
                    text=f"Your preferred God is {self.get_god_title(first_three[0][0])}, {first_three[0][0]},",
                    font=("Arial", 24),
                    wraplength=1400,
                    anchor="w",
                    justify="left",
                )
                self.question_title.pack(pady=(20, 0))
            if i == 1 and first_three[0][1] != first_three[1][1]:
                self.question_title = tk.Label(
                    self.question_frame,
                    text=f"other good choices for you are {self.get_god_title(first_three[1][0])}, {first_three[1][0]} and {self.get_god_title(first_three[2][0])}, {first_three[2][0]}",
                    font=("Arial", 22),
                    wraplength=1400,
                    anchor="w",
                    justify="left",
                )
                self.question_title.pack(pady=(5, 20))

        # Domain points graph window
        self.graph_frame = tk.Frame(self.root, width=1500, height=700)
        self.graph_frame.pack(side=tk.BOTTOM, padx=5, pady=5)

        self.figure, self.ax = plt.subplots(figsize=(12, 6))
        self.bar_chart = FigureCanvasTkAgg(self.figure, self.graph_frame)
        self.bar_chart.get_tk_widget().pack()
        self.update_graph()

    def show_final_results(self):
        god_points = {}
        domain_dict = {}
        grouped_value = defaultdict(list)

        for key, value in domain_points.items():
            grouped_value[value].append(key)

        sorted_grouped_dict = dict(
            sorted(grouped_value.items(), key=lambda item: item[0], reverse=True)
        )
        # messagebox.showinfo("Final Results", f"Top Domain(s):\\n{result_text}")
        largest_seven = list(sorted_grouped_dict.items())[:7]

        updated_values = [12, 10, 8, 6, 4, 2, 1]

        for i in range(len(largest_seven)):
            value, keys = largest_seven[i]
            largest_seven[i] = updated_values[i], keys

        for points, domains in largest_seven:
            for domain in domains:
                domain_dict[domain] = points

        for god, domains in gods_by_domains.items():
            total_points = 0
            for domain in domains:
                if domain in domain_dict:
                    total_points += domain_dict[domain]
            god_points[god] = total_points

        sorted_god_points = dict(
            sorted(god_points.items(), key=lambda item: item[1], reverse=True)
        )

        for i, entry in enumerate(self.extra_answers):
            for god, points in entry.items():
                if i == 0:
                    for god_name, races in gods_by_race.items():
                        if god in races:
                            sorted_god_points[god_name] += points
                elif i == 1:
                    for god_name, classes in gods_by_class.items():
                        if god in classes:
                            sorted_god_points[god_name] += points
                elif i == 2:
                    for god_name, alignment in gods_by_alignment.items():
                        if god == alignment:
                            sorted_god_points[god_name] += points

        sorted_god_points = dict(
            sorted(sorted_god_points.items(), key=lambda item: item[1], reverse=True)
        )

        self.show_frame_2(
            sorted_god_points,
        )

        # self.root.destroy()


if __name__ == "__main__":
    QuizApp()
