def text_test(some_text):
    return (some_text == some_text[::-1])


text = input('Test your text ')
print(text_test(text))
