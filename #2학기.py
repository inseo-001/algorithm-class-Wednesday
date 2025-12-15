#20221379 이인서.

class Node:  # 연결 리스트의 노드로, 노드의 data 필드는 도서(Book) 객체를 저장하는 역할
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next
    def append(self, new):  # 현재 노드 다음에 new 노드를 삽입
        if new is not None:
            new.link = self.link
            self.link = new
    def popNext(self):  # 현재 노드의 다음 노드를 삭제한 후 반환
        deleted_node = self.link
        if deleted_node is not None: 
            self.link = deleted_node.link
        return deleted_node
class LinkedList:  # 단순 연결 리스트 클래스
    def __init__(self):
        self.head = None  # 1번째 인덱스를 머리로 잡고 None값으로 초기화
    def isEmpty(self):
        return self.head is None #head 가 none이면 비어있는 리스트
    def append(self, book):
        new_node = Node(book)
        if self.head is None:
            self.head = new_node
            return
        hd = self.head
        while hd.link:  #리스트의 끝까지 순회하는 코드
            hd = hd.link
        hd.append(new_node)

    def delete_by_pos(self, pos):
        if pos is None or pos < 0 or self.head is None: #값이 0보다 작거나 없으면 false 반환합니다
            return False
        # 0번째 노드 삭제
        if pos == 0:
            deleted = self.head
            self.head = self.head.link
            return True
        
        prev = self.head
        idx = 0

        while prev and idx < pos -1:
            prev = prev.link
            idx += 1
        if prev is None or prev.link is None:
            return False
        
        return prev.popNext() is not None
        
    def find_by_num(self, num):   #index의 약자 ind로 변수를 정했습니다 (책 찾는 함수)
        ind = self.head        #처음부터 순차적으로 탐색 시작
        while ind:        #ind를 도는동안 
            if ind.data.booknum == num: #ind.num 이 찾는 num이면 반환 
                return ind.data
            ind = ind.link #못찾으면 다음 노드로 진행
        # print(f"찾는 도서는 없습니다") 밑의 함수에서 선언했습니다.
        return None # 없으면 없다고 반환
    

    def find_pos_by_num(self, num): # 책의 위치를 찾는 함수    
        ind = self.head
        pos = 0
        while ind:
            if ind.data.booknum == num:
                return pos
            ind = ind.link
            pos += 1
        # print(f"찾는 도서는 없습니다") #위랑 똑같음
        return None 
    
    def find_by_booknum(self, booknum): # 중복된 번호를 찾는 함수입니다. 밑에 중복오류때 쓸 함수
        ind = self.head
        while ind:
            if ind.data.booknum == booknum:
                return ind.data
            ind = ind.link
        return None
    
class Book:
    def __init__(self, booknum, booktitle, writer, bornyears):
        self.booknum = booknum
        self.booktitle = booktitle
        self.writer = writer
        self.bornyears = bornyears

    def printerbook(self):
        print(f"책 번호: {self.booknum}, 제목: {self.booktitle}, 저자: {self.writer}, 출판 연도: {self.bornyears}")

class BookManagement:
    def __init__(self):
        self.books = LinkedList() 

    def add_book(self, booknum, booktitle, writer, bornyears):
        if self.books.find_by_booknum(booknum) is not None:
            print("오류: 이미 존재하는 책 번호입니다.")
            return
        new_book = Book(booknum, booktitle, writer, bornyears)
        
        self.books.append(new_book)    # 새로운 책을 리스트에 삽입

    def remove_book(self, booknum):
        pos = self.books.find_pos_by_num(booknum)
        if pos is None:
            print("번호를 다시 입력해주세요. (오류)")
            return False
        self.books.delete_by_pos(pos)
    
    def search_book(self, num):
        book = self.books.find_by_num(num)
        if book:
            book.printerbook()
        else:
            print("찾으시는 도서가 없습니다")
            return None
    
    def display_books(self):
        
        if self.books.isEmpty():  # 항상 if 문이 먼저 while 문이 먼저 나오면 불필요한 순회가 일어남
            print(f"현재 등록된 도서가 없습니다.")
            return
        ind = self.books.head
        while ind:
            ind.data.printerbook()
            ind = ind.link
        
        
    
    def run(self):
        while 1:
            print(f"=== 도서 관리 프로그램 ===")
            print(f"1. 도서 추가")
            print(f"2. 도서 삭제 (책 번호로 삭제)") #문제에 제목으로 삭제지만 번호를 기준으로 라고 되어있어서 그냥 번호로 하겠습니다.
            print(f"3. 도서 조회 (책 번호로 조회)")
            print(f"4. 전체 도서 목록 출력")
            print(f"5. 종료")
            choice = input("메뉴를 선택하세요: ").strip()
        

            if choice == "1":
                booknum = input("책 번호를 입력하세요: ")
                booktitle = input("책 제목을 입력하세요: ")
                writer = input("저자를 입력하세요: ")
                bornyears = input("출판 연도를 입력하세요: ")

                self.add_book(booknum, booktitle, writer, bornyears)
                print(f"{booktitle} 가 추가되었습니다.") #추가 성공 메세지입니다. 오류 메세지는 위의 함수에서 구현했습니다.
            
            elif choice == "2":
                num = input("삭제할 책 번호를 입력하세요:")
                replay = self.remove_book(num)
                if replay:
                        print(f"{num}번의 도서가 삭제되었습니다.") # if문 안썼다가 없는 번호를 삭제하는 참사가 생겨 수정했습니다.
            elif choice == "3":
                num = input("조회할 책 번호를 입력하세요 :")
                self.search_book(num)
                
            elif choice == "4":
                print(f"현재 등록된 도서 목록 :")
                self.display_books()
            elif choice =="5":
                print("프로그램을 종료합니다.")
                break


if __name__ == "__main__" :
    BookManagement().run() 