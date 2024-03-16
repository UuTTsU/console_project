import sys
import utils
from DiaryBook import DiaryBook
from Account import Account


class Menu:
    def __init__(self, name):
        print(name)
        self.filepath = "./data/"+name+'.json/'
        self.diarybook = DiaryBook()
        self.choices = {
            '1': self.show_all_diaries,
            '2': self.add_diary,
            '3': self.search_diaries,
            '4': self.populate_database,
            # '5': self.sort diary,
            '6': self.quit
        }


    def show_all_diaries(self):
        if len(self.diarybook.diaries) == 0:
            print('there are no diaries in the database')
        else:
            for diary in self.diarybook.diaries:
                print(f'{diary.id} - {diary.memo}')


    def add_diary(self):
        memo = input('enter a memo: ')
        tags = input('enter a tag: ')
        self.diarybook.new_diary(memo, tags)
        print('your note has been aded succesfully!!!')

    def search_diaries(self):
        keyword = input('enter a kewyword: ')
        filtered_diaries = self.diarybook.search_diary(keyword)
        if len(filtered_diaries) == 0:
            print('we could not find any diary matching the key words')
        else:
            for diary in filtered_diaries:
                print(f'{diary.id} - {diary.memo}')


    def populate_database(self):
        diaries = utils.read_from_json_into_app('data.json')
        for diary in diaries:
            self.diarybook.diaries.append(diary)

    def sort_diary(self):
        pass

    def quit(self):
        print('thanks for using our diarybook!...')
        sys.exit(0)

    def display_menu(self):
        print("""
            Diarybook Menu:
            
            1. show diaries
            2. add diary
            3. filter using keyword
            4. populate database
            5. quit program
            
            
        """)

    def run(self):

        while True:
            self.display_menu()
            choice = input('enter an option: ')
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(choice + "is not a valid choice")


if __name__ == "__main__":
    user = Account()
    Menu(user.give_user()).run()


