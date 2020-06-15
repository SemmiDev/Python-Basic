class HappyBirthday:
    def special(self):
        message = "::: Happy Birthday Java:::"
        return message
    def details(self):
        details = {
            "Name": "Java",
            "Designed by": "James Gosling",
            "Developer": "Sun Microsystems",
            "Release": "May 23, 1995",
            "Age": 25
        }
        for k, v in details.items():
            print(f'{k} => {v}')

if __name__ == '__main__':
    topic = HappyBirthday()
    temp = topic.special()
    print(temp)
    topic.details()
