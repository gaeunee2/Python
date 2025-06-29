from notebook import Note
from notebook import NoteBook

menu = int(input('메뉴 입력(0이면 종료): '))
wise_saying_notebook = NoteBook("명언 노트")

while menu != 0:
    if menu == 1:
        print('<모든 노트 내용 출력>')
        for page_number, note in wise_saying_notebook.notes.items():
            print(f'{page_number}페이지 내용: {note.contents}')
    elif menu == 2:
        print('<노트 내용 출력>')
        num = int(input('노트 번호 입력: '))
        if num in wise_saying_notebook.notes:
            content = wise_saying_notebook.notes[num].contents
            print(content)
        else:
            print('해당 페이지에 노트가 없습니다.')
    elif menu == 3:
        print('<새로운 노트 추가>')
        num = int(input('노트 번호 입력: '))
        sentence = input('노트 내용 입력: ')
        note = Note(sentence)
        wise_saying_notebook.add_note(num, note)
    elif menu == 4:
        print('<노트 삭제>')
        num = int(input('노트 번호 입력: '))
        wise_saying_notebook.remove_note(num)
    elif menu == 6:
        print('<모든 페이지 수 출력>')
        print(wise_saying_notebook.get_number_of_all_pages())
    elif menu == 7:
        print('<총 글자 수 출력>')
        print(wise_saying_notebook.get_number_of_all_characters())
    elif menu == 8:
        print(wise_saying_notebook.title)
    else:
        print('잘못된 메뉴 입력')

    menu = int(input('메뉴 입력(0이면 종료): '))