import random

def create_files():
      for index in range(14):
            file_no = index + 1
            question_file = f"question_set_{file_no}"
            answer_file = f"answer_set_{file_no}"
            with open(question_file, 'w') as wf:
                  print("Question file generated", question_file)
            with open(answer_file, 'w') as wf:
                  print("Answer file generated", answer_file)
            gen_question(question_file, answer_file)

def gen_question(question_file, answer_file):
      zones = {
            "Mechi": "Illam",
            "Koshi": "Biratnagar",
            "Sagarmatha": "Rajbiraj",
            "Janakpur": "Jaleswor",
            "Bagmati": "Kathmandu",
            "Narayani": "Birgunj",
            "Gandaki": "Pokhara",
            "Dhaulagiri": "Baglung",
            "Lumbini": "Butwal",
            "Rapti": "Tulsipur",
            "Bheri": "Birendranagar",
            "Karnali": "Jumla",
            "Seti": "Dhangadi",
            "Mahakali": "Mahendranagar",
        }

      zones_list = list(zones.keys())
      random.shuffle(zones_list)

      for index, zone in enumerate(zones_list):
            question_no = index + 1
            question = f"\n\n{question_no}. What is headquarter of {zone}?"
            hqs = list(zones.values())
            random.shuffle(hqs)
            answer = zones[zone]
            options = random.sample(hqs, 3)
            options.append(answer)
            option_string = ''
            for index, hq in enumerate(options):
                  option_no = 'ABCD'[index]
                  option_string += f"\n{option_no}. {hq}"
            full_question = question + option_string
            with open(question_file, 'a') as af:
                  af.write(full_question)

            answer_key = f"\n{question_no}. {answer}"
            with open(answer_file, 'a') as af:
                  af.write(answer_key)

if __name__ == '__main__':
      create_files()
