from flet import*
import sqlite3

conn = sqlite3.connect("dato.db",check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stdname Text,
    stdmail Text,
    stdphone Text,
    stdaddress Text,
    stdmathiq INTEGER,
    stdarabin INTEGER,
    stdenglish INTEGER,
    stdfrench INTEGER,
    stdfilo INTEGER,
    stdsport INTEGER               
               
               )
""")
#
conn.commit()
######################

tabe_name = 'student'
query = f'SELECT COUNT(*) FROM {tabe_name}'
cursor.execute(query)
result = cursor.fetchone()
row_count = result[0]





def main(page:Page):
    page.title = 'Hedaji'
    page.scroll = 'auto'
    page.window.top = 1
    page.window.left = 960
    page.window.width = 390
    page.window.height = 740
    page.bgcolor = 'white'
    #page.theme_mode = ThemeMode.LIGHT

    ##############
    def add(e):
        cursor.execute("INSERT INTO student(stdname,stdmail,stdphone,stdaddress,stdmathiq,stdarabin,stdenglish,stdfrench,stdfilo,stdsport) VALUES (?,?,?,?,?,?,?,?,?,?)",(tname.value,tmail.value,tphone.value,taddress.value,mathmatique.value,arabic.value,english.value,français.value,filo.value,sport.value))
        conn.commit()


    def show(e):
        page.clean()
        c = conn.cursor()
        c.execute("SELECT * FROM student")
        users = c.fetchall()
        print(users)

        if not users == "":
            keys = ['id','stdname','stdmail','stdphone','stdaddress','stdmathiq','stdarabin','stdenglish','stdfrench','stdfilo','stdsport']
            result = [dict(zip(keys,values)) for values in users]
            for x in result:

                m = x['stdmathiq']
                a = x['stdarabin']
                f = x['stdenglish']
                e = x['stdfrench']
                d = x['stdfilo']
                c = x['stdsport']
                res = m+a+f+e+d+c
                if res < 50 :
                    a = Text('😥 Refusé',color='white',size=19)
                if res > 50 :
                    a = Text('🥰 Reussit',color='white',size=19)



                page.add(
                    Card(
                        color='black',
                        content= Container(
                            content=Column([
                                ListTile(
                                    bgcolor = 'black',
                                    leading=Icon(icons.PERSON),
                                    title = Text('Name : ' + x['stdname'],color ='red'),
                                    subtitle= Text('Email : '+ x['stdmail'],color='green')


                                ),
                                Row([
                                    Text('Phone : '+ x['stdphone'],color='green'),
                                    Text('Address : '+ x['stdaddress'],color='green')
                                ],alignment=MainAxisAlignment.CENTER),
                                Row([
                                    Text('Math : '+ str(x['stdmathiq']),color = 'blue'),
                                    Text('Arabic : '+ str(x['stdarabin']),color = 'blue'),
                                    Text('English : '+ str(x['stdenglish']),color = 'blue'),

                                ],alignment=MainAxisAlignment.START),
                                Row([
                                    Text('Frensh : ' + str(x['stdfrench']),color = 'blue'),
                                    Text('Filo : ' + str(x['stdfilo']),color = 'blue'),
                                    Text('Sport : ' + str(x['stdfilo']),color = 'blue')

                                ],alignment=MainAxisAlignment.START),

                                Row([
                                    a
                                ],alignment=MainAxisAlignment.CENTER)
                            ])
                        )

                    )
                )
                page.update()


    ##### fields

    tname = TextField(label ='Nom étudient',icon=icons.PERSON,height=38)
    tmail = TextField(label ='Email étudient',icon=icons.MAIL,height=38)
    tphone = TextField(label ='Phone étudient',icon=icons.PHONE,height=38)
    taddress = TextField(label ='Address étudient',icon=icons.PERSON,height=38)
    ##### Marks

    marktext = Text("Resultat d'étudient",text_align='center',weight='bold')
    mathmatique = TextField(label='Math',width=110,height=38)
    arabic = TextField(label='Arabic',width=110,height=38)
    english = TextField(label='English',width=110,height=38)
    français = TextField(label='Frensh',width=110,height=38)
    filo = TextField(label='Filosophie',width=110,height=38)
    sport = TextField(label='Sport',width=110,height=38)

    addbuton =ElevatedButton('Ajouter nouveau étudient',
                             width=170,
                             style=ButtonStyle(bgcolor='blue',color=   'white',padding=15),
                             on_click=add)
    showbuton =ElevatedButton('Afficher tout les étudients',
                              width=170,
                              style=ButtonStyle(bgcolor='blue',color=   'white',padding=15),
                              on_click=show)


    page.add(

        Row([
            Image(src='home.gif',width=400,height=200)
        ],alignment=MainAxisAlignment.CENTER),
        Row([
            Text("Application d'etudiant",size=20,font_family="Courier",color='black')
        ],alignment=MainAxisAlignment.CENTER),

        Row([
            Text("Nombre d'etudiant enregistrer :",size=20,font_family="Courier",color='blue'),
            Text(row_count,size=20,font_family="Courier",color='black')
        ],alignment=MainAxisAlignment.CENTER),
        tname,
        tmail,
        tphone,
        taddress,
        Row([
            marktext

        ],alignment=MainAxisAlignment.CENTER),

        Row([
            mathmatique,
            arabic,
            english
        ],alignment=MainAxisAlignment.CENTER),

        Row([
            français,
            filo,
            sport
        ],alignment=MainAxisAlignment.CENTER),
        Row([
            addbuton,
            showbuton


        ],alignment=MainAxisAlignment.CENTER)




    )


    page.update()
app(main)
