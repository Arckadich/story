def number_of_line(*files):
    all_text = {}
    for file in files:
        with open(file, 'rt', encoding='utf-8') as f:
            y = f.readlines()
            all_text[file] = y
    all_text1 = {k: all_text[k] for k in sorted(all_text, key=all_text.get, reverse=True)}
    for key, value in all_text1.items():
        with open('all.txt', 'a', encoding='utf-8') as f:
            r = len(value)
            f.writelines(f'\n{key}')
            f.writelines(f'\n{r}\n')
            # f.writelines(value)
number_of_line('1.txt', '2.txt', '3.txt')