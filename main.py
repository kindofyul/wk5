import datetime
import re


def create_membership():
    # 아래 코드는 python에 내장되어 있는 datetime 모듈을 활용하여 오늘 날짜를 입력하는 코드입니다.
    # stnr_date 코드는 제가 작성했으니, 건드리지 않으셔도 되옵니다 :)
    now = datetime.datetime.now()
    stnr_date = now.strftime("%Y%m%d")

    users = []

    while True:
        user = {}

        while True:
            username = input("아이디를 입력하세요 \n>>")
            hangeul = re.compile('^[ㄱ-힇]$')
            hangeul_check = hangeul.match(username)
            # 한국어만 입력..?
            if len(username) >= 2 and len(username) <= 4:
                print("사용 가능한 아이디입니다")
                break
            else:
                print("2~4 글자 사이로 입력하세요")
                continue

        while True:
            password = input("비밀번호를 입력하세요 \n>>")

            if (
                password[0].isupper() == True
                and len(password) >= 8
                and (
                    "!" in password
                    or "@" in password
                    or "#" in password
                    or "$" in password
                )
            ):
                break
            else:
                print("올바르지 않은 비밀번호입니다")
                continue

        while True:
            email = input("이메일을 입력하세요 \n>>")
            regex_email = r"^[a-z0-9]+?[a-z0-9]+[@]\w+[.]\w+[.]?\w{2,3}$"
            valid = re.search(regex_email, email)
            if "@" in email and email.endswith(".com") == True:  # 영문, 숫자만 입력?
                break
            else:
                print("올바르지 않은 이메일입니다")
                continue

        user["username"] = username
        user["password"] = password
        user["email"] = email
        user["stnr_date"] = stnr_date

        users.append(user)
        print(users)

        while True:
          cont = input("계속 입력하시겠습니까? \n Y or N \n >>")
          if cont.upper() == "Y":
              break
          elif cont.upper() == "N":
              return users
          else:
              print("올바르지 않은 응답입니다")



def load_to_txt(user_list):
    f = open("memberdb.txt", "w", encoding="UTF-8")

    for i in user_list:
        data = i['username'] +", " + i['password'] + ", " + i['email'] + ", " + i['stnr_date'] + ", "       #왜 저장이 안 될까?
        f.write(data)
    f.close()


def run():
    user_list = create_membership()
    load_to_txt(user_list)


run()
