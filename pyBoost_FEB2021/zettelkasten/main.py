all_notes = []


def crate_note(title, body, tags):
    note = {"title": title, "body": body, "tags": tags}
    return note


def find_note(tag):
    result = [note for note in all_notes if tag in note["tags"]]
    return result


while True:
    title = input("введите назщвание заметки либо 0 чтобь перейти к поиску:")
    if title == "0":
        break
    body = input("body :")
    tags = []
    while True:
        tag = input("введите тег, либо 0 чтобы остановить:")
        if tag == "0":
            break

        tags.append(tag)

    all_notes.append(crate_note(title, body, tags))

tag = input("введите тег: ")
search = find_note(tag)
print(search)
