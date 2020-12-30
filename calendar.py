#Program To make a calendar for 2021
import texttable

names = [
    "January", "February", "March", "April", "May", "June", "July", "August",
    "September", "October", "November", "December"
]
week = ["Sun", "Mon", "Tues", "Wed", "Thur", "Fri", "Sat"]
holidays = {
    'June': [],
    'March': [('8', ' Maharishi Dayanand Saraswati Jayanti'),
              ('11', ' Maha Shivaratri/Shivaratri'), ('28', ' Holika Dahana'),
              ('29', ' Holi')],
    'July': [('12', ' Rath Yatra'), ('21', ' Bakr Id/Eid ul-Adha')],
    'February': [('16', ' Vasant Panchami'), ('19', ' Shivaji Jayanti'),
                 ('26', " Hazarat Ali's Birthday"),
                 ('27', ' Guru Ravidas Jayanti')],
    'September': [('10', ' Ganesh Chaturthi/Vinayaka Chaturthi')],
    'October': [('2', ' Mahatma Gandhi Jayanti'), ('12', ' Maha Saptami'),
                ('13', ' Maha Ashtami'), ('14', ' Maha Navami'),
                ('15', ' Dussehra'), ('19', ' Milad un-Nabi/Id-e-Milad'),
                ('20', ' Maharishi Valmiki Jayanti'),
                ('24', ' Karaka Chaturthi (Karva Chauth)')],
    'November': [('4', ' Naraka Chaturdasi'), ('4', ' Diwali/Deepavali'),
                 ('5', ' Govardhan Puja'), ('6', ' Bhai Duj'),
                 ('10', ' Chhat Puja (Pratihar Sashthi/Surya Sashthi)'),
                 ('19', ' Guru Nanak Jayanti'),
                 ('24', " Guru Tegh Bahadur's Martyrdom Day")],
    'January': [('1', " New Year's Day"), ('13', ' Lohri'), ('14', ' Pongal'),
                ('14', ' Makar Sankranti'), ('20',
                                             ' Guru Govind Singh Jayanti'),
                ('26', ' Republic Day')],
    'April': [('2', ' Good Friday'), ('4', ' Easter Day'),
              ('13', ' Chaitra Sukhladi'), ('14', ' Vaisakhi'),
              ('14', ' Mesadi'), ('14', ' Ambedkar Jayanti'),
              ('15', ' Bahag Bihu/Vaisakhadi'), ('21', ' Rama Navami'),
              ('25', ' Mahavir Jayanti')],
    'December': [('24', ' Christmas Eve'), ('25', ' Christmas')],
    'May': [('7', ' Jamat Ul-Vida'), ('9', ' Birthday of Ravindranath'),
            ('14', ' Ramzan Id/Eid-ul-Fitar'), ('14',
                                                ' Ramzan Id/Eid-ul-Fitar'),
            ('26', ' Buddha Purnima/Vesak')],
    'August': [('15', ' Independence Day'), ('16', ' Parsi New Year'),
               ('19', ' Muharram/Ashura'), ('21', ' Onam'),
               ('22', ' Raksha Bandhan (Rakhi)'), ('30', ' Janmashtami'),
               ('30', ' Janmashtami (Smarta)')]
}


class Year:
    def __init__(self):
        self.start_Day = "Fri"
        self.months = []
        for i in range(1, 13):
            holiday = holidays[names[i - 1]]
            temp = Month(i, self.start_Day, names[i - 1], holiday)
            self.start_Day = week[len(temp.weeks[-1]) - 7]
            self.months.append(temp)

        self.no_months = len(self.months)
        self.no_holidays = len(holidays)

    def show_full_year(self):
        for i in self.months:
            i.show_month()
            table_2.reset()


    def show_specific_month(self, which_month):
        self.months[which_month - 1].show_month()

    def check_date(self, date):
        day = int(date[0:2])
        month = self.months[int(date[3:5]) - 1]
        for i in month.weeks:
            counter = 0
            for j in i:
                if day == j:
                    print("\nDay on this date {} -->".format(date),
                          week[counter])
                    break
                counter += 1

    def list_holidays(self):
        tmp = [["Day","Month","Event"]]
        for i in names:
            for j in holidays[i]:
                tmp.append([j[0], i, j[1]])
        table_1.add_rows(tmp)
        print(table_1.draw())


class Month:
    def __init__(self, number, start_Day, name, holiday):
        self.name = name
        self.holiday = holiday
        #print(self.name,self.holiday)
        #print("\n\n\n")
        self.holiday_days = []
        self.weeks = []

        for i in self.holiday:
            self.holiday_days.append(i[0])

        if number == 2:
            self.days = 28
        elif number % 2 == 0:
            self.days = 30
        else:
            self.days = 31

        counter = week.index(start_Day)
        temp = [" " for i in range(counter)]
        for i in range(1, self.days + 1):
            temp.append(i)
            if len(temp) == 7 or i == self.days:
                self.weeks.append(temp)
                temp = []

    def show_month(self):
        print("\n\n\n\n")
        print("\t", self.name)
        for i in week:
            print("", i, end=" ", sep="")
        print("\n")

        for i in self.weeks:
            for j in i:
                if j == " ":
                    print(" ", j, end="", sep="  ")

                elif j <= 9:
                    if str(j) in self.holiday_days:
                        print("", j, sep="  *", end="")
                    else:
                        print(" ", j, end="", sep="  ")
                else:
                    if str(j) in self.holiday_days:
                        print("", j, sep=" *", end="")
                    else:
                        print("", j, sep="  ", end="")
            print("")
        print("")
        if len(self.holiday)!=0:
          tmp = ["Day","Event"]
          self.holiday.insert(0,tmp)
          table_2.add_rows( self.holiday )
          print(table_2.draw())

def operation(ch):
    if ch == 1:
        year.show_full_year()
    elif ch == 2:
        which_month = int(input("\nWhich month: "))
        print("\n")
        year.show_specific_month(which_month)
    elif ch == 3:
        date = input("\nEnter date(dd/mm/yy): ")
        print("\n")
        year.check_date(date)
    elif ch == 4:
        year.list_holidays()
    else:
        return False
    return True


year = Year()
#table = texttable()
table_1 = texttable.Texttable(0)
table_2 = texttable.Texttable(0)

# Set columns
table_1.set_cols_align(["l", "c", "c"])
table_2.set_cols_align(["l", "c"])

# Set datatype of each column
table_1.set_cols_dtype(["i", "t", "t"])
table_2.set_cols_dtype(["i", "t"])

# Adjust columns
table_1.set_cols_valign(["m", "m", "m"])
table_2.set_cols_valign(["m", "m"])

while True:
    print("\n\n\nWelcome to 2021 Calender", end="\n\n\n")
    print("1. Show Full Year")
    print("2. Show Month")
    print("3. Check date")
    print("4. List Days of holidays\n")
    print("5. EXIT")
    choice = int(input("Select any one option: "))

    val = operation(choice)
    if val == False:
        print("\n\n\nThank You")
        break
