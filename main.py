from ursina import *
from random import randint

# Deklarasi variabel global untuk status permainan dan kecepatan slot
run = run1 = run2 = run3 = False
speed1 = speed2 = speed3 = 0
m1 = m2 = m3 = 0
k1 = k2 = k3 = 0
mm1 = mm2 = mm3 =0

# Fungsi untuk menangani input dari pengguna
def input(key):
	if key=="left mouse down":
		Audio("assets/Starlight Princess Free Spin Mode (320).mp3")
		Animation("assets/spark", parent=camera.ui, fps=5, scale=.1, position=(.19, -.03), loop=False)

# Fungsi untuk memperbarui posisi slot setiap frame
def update():
    global m1, m2, m3, mm1, mm2, mm3, k1, k2, k3
    global run, run1, run2, run3
    global speed1, speed2, speed3

# Perbarui posisi slot dalam kolom pertama
    if run:
        for i, slot in enumerate(slots_1):
            slot.y -= speed1 * time.dt
            if slot.y < -3:
                m1 += 1
                slot.y = slots_1[i - 2].y + 1.2
                if m1 == mm1:
                    k1 += mm1
                    speed1 = 0
                    run1 = True
   # Perbarui posisi slot dalam kolom kedua
        for j, slot in enumerate(slots_2):
            slot.y -= speed2 * time.dt
            if slot.y < -3:
                m2 += 1
                slot.y = slots_2[j - 2].y + 1.2
                if m2 == mm2:
                    k2 += mm2
                    speed2 = 0
                    run2 = True
# Perbarui posisi slot dalam kolom kedua
        for l, slot in enumerate(slots_3):
            slot.y -= speed3 * time.dt
            if slot.y < -3:
                m3 += 1
                slot.y = slots_3[l - 2].y + 1.2
                if m3 == mm3:
                    k3 += mm3
                    speed3 = 0
                    run3 = True
                    
# Cek apakah semua slot telah berhenti dan hasilnya sama
        if run1 and run2 and run3 and (k1 % 3 == k2 % 3 == k3 % 3):
            money.y -= time.dt * 3

# Fungsi untuk memulai permainan
def go():
    global m1, m2, m3, mm1, mm2, mm3
    global run, run1, run2, run3
    global speed1, speed2, speed3

    run = True
    run1 = run2 = run3 = False
    m1 = m2 = m3 = 0
    speed1 = speed2 = speed3 = 2

    mm1 = randint(3, 11)
    mm2 = randint(3, 11)
    mm3 = randint(3, 11)
    money.y = 10


# Kelas untuk halaman utama
class HomePage(Entity):
    def __init__(self):
        super().__init__()

        print("Initializing Home Page")

        self.main_menu = Entity(parent=self, enabled=True)

 # Latar belakang halaman utama
        self.background = Entity(
            model="quad",
            parent=self.main_menu,
            position=(0, 0, 1),
            scale=(200 / 12, 141 / 12),
            texture="assets/main_bg.jpg",
        )

 # Logo di halaman utama
        Entity(
            parent=self.main_menu,
            model="quad",
            texture="assets/logo.png",
            position=(0, 2.5, 0),
            scale=(825 / 100, 466 / 100),
        )
 # Tombol untuk memulai permainan
        self.start_button = Button(
            text="Start Game",
            color=color.rgba(1, 1, 1, 0.8),
            scale=(5, 1),
            y=-0.1,
            parent=self.main_menu,
            radius=0.25,
            highlight_color=color.rgba(161 / 255, 89 / 255, 1, 0.8),
            on_click=self.start_game
        )

        self.start_button.text_entity.color = color.rgb(55 / 255, 31 / 255, 83 / 255)
        
# Tombol untuk membuka halaman pengaturan
        self.settings_button = Button(
            text="Settings",
            color=color.rgba(1, 1, 1, 0.8),
            scale=(5, 1),
            y=-1.3,
            parent=self.main_menu,
            radius=0.25,
            highlight_color=color.rgba(161 / 255, 89 / 255, 1, 0.8),
            on_click=self.go_to_settings
        )

        self.settings_button.text_entity.color = color.rgb(55 / 255, 31 / 255, 83 / 255)
# Tombol untuk keluar dari aplikasi
        self.quit_button = Button(
            text="Quit",
            color=color.rgba(1, 1, 1, 0.8),
            scale=(5, 1),
            y=-2.5,
            parent=self.main_menu,
            radius=0.25,
            highlight_color=color.rgba(161 / 255, 89 / 255, 1, 0.8),
            on_click=application.quit
        )

        self.quit_button.text_entity.color = color.rgb(55 / 255, 31 / 255, 83 / 255)
        
# Fungsi untuk memulai permainan dari halaman utama
    def start_game(self):
        print("Starting the game!")
        self.main_menu.enabled = False
        show_slot_game()
        
# Fungsi untuk membuka halaman pengaturan
    def go_to_settings(self):
        print("Going to settings page")
        self.main_menu.enabled = False
        settings_page.enabled = True
        
# Kelas untuk halaman pengaturan
class SettingsPage(Entity):
    def __init__(self):
        super().__init__(enabled=False)
        print("Initializing Settings Page")

        self.settings_menu = Entity(parent=self, enabled=True)

# Latar belakang halaman pengaturan
        self.background = Entity(
            model="quad",
            parent=self.settings_menu,
            position=(0, 0, 1),
            scale=(200 / 12, 141 / 12),
            texture="assets/setting_bg.jpg",
        )


# Tombol untuk kembali ke halaman utama
        self.back_button = Button(
            text="Back",
            color=color.rgba(1, 1, 1, 0.8),
            scale=(5, 1),
            y=-0.5,
            parent=self.settings_menu,
            radius=0.25,
            highlight_color=color.rgba(161 / 255, 89 / 255, 1, 0.8),
            on_click=self.go_back
        )

        self.back_button.text_entity.color = color.rgb(55 / 255, 31 / 255, 83 / 255)

# Fungsi untuk kembali ke halaman utama
    def go_back(self):
        print("Going back to home page")
        self.enabled = False
        home_page.main_menu.enabled = True

# Fungsi untuk menampilkan permainan slot
def show_slot_game():
    global slots_1, slots_2, slots_3, machine, money
    global run, speed1, speed2, speed3, m1, m2, m3, k1, k2, k3

    window.color = color.rgb(128, 255, 128)
    run = False
    speed1 = speed2 = speed3 = 0
    m1 = m2 = m3 = 0
    k1 = k2 = k3 = 0
    
# Entitas mesin slot dan uang
    imgs = ['assets/coin.png', 'assets/diamond.png', 'assets/star.png']
    machine = Entity(model='quad', scale=(10, 8), texture='assets/jackpot.png', z=-0.1)
    money = Entity(model='quad', scale=(10, 8), texture='assets/money.png', z=-0.15, y=10)
    slot10 = Entity(model='quad', scale=(1, 1), texture=imgs[0], x=-2.5, y=1.8)
    slot11 = duplicate(slot10, texture=imgs[1], y=0.6)
    slot12 = duplicate(slot10, texture=imgs[2], y=-0.6)

 # Slot pertama dalam kolom pertama
    slot20 = Entity(model='quad', scale=(1, 1), texture=imgs[0], x=-0.4, y=0.6)
    slot21 = duplicate(slot20, texture=imgs[1], y=-0.6)
    slot22 = duplicate(slot20, texture=imgs[2], y=-1.8)
   
# Slot kedua dalam kolom kedua
    slot30 = Entity(model='quad', scale=(1, 1), texture=imgs[0], x=1.7, y=-0.6)
    slot31 = duplicate(slot30, texture=imgs[1], y=-1.8)
    slot32 = duplicate(slot30, texture=imgs[2], y=-3)

    slots_1 = [slot10, slot11, slot12]
    slots_2 = [slot20, slot21, slot22]
    slots_3 = [slot30, slot31, slot32]

    B = Button(text='', color=color.rgba(0,0,0,0),
           icon = 'assets/button.png',scale= .2, x=.4,y=-.35)
    B.on_click = go

    back_button = Button(
        text='Kembali ke Halaman Utama',
        color=color.rgba(1, 1, 1, 0.8),
        scale=(0.3, 0.1),
        x=-0.8,
        y=-0.4,
        on_click=back_to_home
    )

    go()

def back_to_home():
    print("Going back to home page")
    for entity in scene.entities:
        destroy(entity)
    home_page.main_menu.enabled = True

app = Ursina()
home_page = HomePage()
settings_page = SettingsPage()
app.run()
