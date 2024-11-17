import string


vowels = frozenset('aeiouy')


def calc_lines_stat(lines):
    vowels_count = 0
    consonant_count = 0
    words_stat = {}
    for line in lines:
        for word in line.split():
            word = word.strip(string.punctuation).lower()
            for c in word:
                if c in vowels:
                    vowels_count += 1
                else:
                    consonant_count += 1
            if word not in words_stat:
                words_stat[word] = 0
            words_stat[word] += 1

    return dict(sorted(words_stat.items(), key=lambda x: x[1], reverse=True)), vowels_count, consonant_count


def read_file_lines():
    with open("../data/first_task.txt", encoding="utf-8") as file:
        return file.readlines()


def write_words_stat(words_stat):
    with open("first_task_result.txt", "w", encoding="utf-8") as file:
        top_word = ""
        top_count = -1
        for word, count in words_stat.items():
            file.write(f"{word}:{count}\n")
            if count > top_count:
                top_word = word
                top_count = count

        file.write("-----------\n")
        file.write(f"{top_word}:{top_count}")


def write_vowels_stat(vowels_count, consonant_count):
    vowels_proportion = round(vowels_count / (vowels_count + consonant_count), 3)
    with open("first_task_result_2.txt", "w", encoding="utf-8") as file:
        file.write(f"{vowels_count}\n")
        file.write(f"{vowels_proportion}")


lines = read_file_lines()
words_stat, vowels_count, consonant_count = calc_lines_stat(lines)
write_words_stat(words_stat)
write_vowels_stat(vowels_count, consonant_count)
