#LAB10 노트북 만들기

class Note(object):
    def __init__(self, contents):
        self.contents = contents

    def write_content(self, contents):
        self.contents = contents
        
    def remove_all(self):
        self.contents = ""

class NoteBook(object):
    def __init__(self, title):
        self.title = title
        self.notes = {}

    def add_note(self, page_number, note):
        if page_number in self.notes:
            print('해당 페이지에는 이미 노트가 존재합니다.')
        elif page_number > 300:
            print('더 이상 노트를 추가하지 못합니다.')
        else:
            self.notes[page_number] = note

    def remove_note(self, page_number):
        if page_number in self.notes:
            del self.notes[page_number]
        else:
            print('해당 페이지에 노트가 존재하지 않습니다.')

    def get_number_of_all_pages(self):
        return len(self.notes)

    def get_number_of_all_characters(self):
        total = sum(len(note.contents) for note in self.notes.values())
        return total