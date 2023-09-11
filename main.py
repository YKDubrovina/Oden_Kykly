import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap, QIcon, QPainter, QImage
from PyQt5.QtCore import Qt

# Определение класса главного окна приложения
class Window(QWidget):

    # Инициализация и настройка интерфейса
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Установка заголовка окна
        self.setWindowTitle('Одень куклу')
        # Установка размера окна
        self.setGeometry(300, 300, 1000, 675)

# Блокировки изменения размера окна
    def resizeEvent(self, event):
        # Фиксированный размер
        self.setFixedSize(1000, 675)
        # Сброс к исходному размеру
        self.showNormal()
        # Убираем кнопки свернуть/развернуть
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)

        # Создание QLabel для отображения изображений
        self.image_label = QLabel()

        # Загрузка фонового изображения
        self.bg_img = QLabel(self)
        self.bg_img.setPixmap(QPixmap('img/start_model.png'))
        self.bg_img.setGeometry(0, 0, 1000, 675)
        self.bg_img.setScaledContents(True)

        # Создание QLabel для отображения юбки и топа
        self.skirt_img = QLabel(self)
        self.top_img = QLabel(self)

# КНОПКИ ОСНОВНОГО МЕНЮ
        self.button1 = QPushButton('Топы', self)
        self.button1.setGeometry(525, 50, 200, 150)
        self.button1.clicked.connect(self.show_tops)

        self.button2 = QPushButton('Юбки', self)
        self.button2.setGeometry(775, 50, 200, 150)
        self.button2.clicked.connect(self.show_skirts)

        self.button3 = QPushButton('Выход', self)
        self.button3.setGeometry(775, 450, 200, 150)
        self.button3.clicked.connect(self.show_result)

        self.button4 = QPushButton('Очистить все', self)
        self.button4.setGeometry(625,450,150,50)
        self.button4.clicked.connect(self.reset_all)

        self.button5 = QPushButton('Очистить юбки', self)
        self.button5.setGeometry(625,500,150,50)
        self.button5.clicked.connect(self.reset_skirt)

        self.button6 = QPushButton('Очистить топы', self)
        self.button6.setGeometry(625, 550, 150, 50)
        self.button6.clicked.connect(self.reset_top)

        self.button7 = QPushButton('Сохранить результат', self)
        self.button7.setGeometry(10, 10, 150, 50)
        self.button7.clicked.connect(self.save)

# КНОПКИ ВЫБОРА ЮБОК
        self.purple_skirt_btn = QPushButton('', self)
        self.purple_skirt_btn.setGeometry(525, 50, 200, 150)
        self.purple_skirt_btn.setIcon(QIcon('img/purple_skirt.png'))
        self.purple_skirt_btn.setIconSize(self.purple_skirt_btn.size())
        self.purple_skirt_btn.clicked.connect(self.put_on_purple)
        self.purple_skirt_btn.hide()

        self.pink_skirt_btn = QPushButton('', self)
        self.pink_skirt_btn.setGeometry(775, 50, 200, 150)
        self.pink_skirt_btn.setIcon(QIcon('img/pink_skirt.png'))
        self.pink_skirt_btn.setIconSize(self.pink_skirt_btn.size())
        self.pink_skirt_btn.clicked.connect(self.put_on_pink)
        self.pink_skirt_btn.hide()

        self.black_skirt_btn = QPushButton('', self)
        self.black_skirt_btn.setGeometry(775, 250, 200, 150)
        self.black_skirt_btn.setIcon(QIcon('img/black_skirt.png'))
        self.black_skirt_btn.setIconSize(self.black_skirt_btn.size())
        self.black_skirt_btn.clicked.connect(self.put_on_black)
        self.black_skirt_btn.hide()

        self.blue_skirt_btn = QPushButton('', self)
        self.blue_skirt_btn.setGeometry(525, 250, 200, 150)
        self.blue_skirt_btn.setIcon(QIcon('img/blue_skirt.png'))
        self.blue_skirt_btn.setIconSize(self.blue_skirt_btn.size())
        self.blue_skirt_btn.clicked.connect(self.put_on_blue)
        self.blue_skirt_btn.hide()

# КНОПКИ ВЫБОРА ТОПОВ
        self.sweater_btn = QPushButton('', self)
        self.sweater_btn.setGeometry(525, 50, 200, 150)
        self.sweater_btn.setIcon(QIcon('img/sweater_top.png'))
        self.sweater_btn.setIconSize(self.sweater_btn.size())
        self.sweater_btn.clicked.connect(self.put_on_sweater)
        self.sweater_btn.hide()

        self.black_top_btn = QPushButton('', self)
        self.black_top_btn.setGeometry(775, 50, 200, 150)
        self.black_top_btn.setIcon(QIcon('img/blackk_top.png'))
        self.black_top_btn.setIconSize(self.black_top_btn.size())
        self.black_top_btn.clicked.connect(self.put_on_blackk)
        self.black_top_btn.hide()

        self.red_top_btn = QPushButton('', self)
        self.red_top_btn.setGeometry(525, 250, 200, 150)
        self.red_top_btn.setIcon(QIcon('img/red_top.png'))
        self.red_top_btn.setIconSize(self.red_top_btn.size())
        self.red_top_btn.clicked.connect(self.put_on_red)
        self.red_top_btn.hide()

        self.chorn_top_btn = QPushButton('', self)
        self.chorn_top_btn.setGeometry(775, 250, 200, 150)
        self.chorn_top_btn.setIcon(QIcon('img/black1_top.png'))
        self.chorn_top_btn.setIconSize(self.chorn_top_btn.size())
        self.chorn_top_btn.clicked.connect(self.put_on_black1)
        self.chorn_top_btn.hide()

# МЕТОД ОТОБРАЖЕНИЯ КНОПОК ВЫБОРА ТОПОВ
    def show_tops(self):

        # Скрываем кнопки основного меню
        self.button1.hide()
        self.button2.hide()
        self.button7.hide()

        # Показываем кнопки выбора топов
        self.sweater_btn.show()
        self.black_top_btn.show()
        self.red_top_btn.show()
        self.chorn_top_btn.show()

        # Кнопка "Назад"
        self.back_top_btn = QPushButton('Назад', self)
        self.back_top_btn.setGeometry(10, 10, 100, 30)
        self.back_top_btn.clicked.connect(self.back2)
        self.back_top_btn.show()

# МЕТОД ОТОБРАЖЕНИЯ КНОПОК ВЫБОРА ЮБОК
    def show_skirts(self):

        # Скрываем кнопки основного меню
        self.button1.hide()
        self.button2.hide()
        self.button7.hide()

        # Показываем кнопки выбора юбок
        self.purple_skirt_btn.show()
        self.pink_skirt_btn.show()
        self.black_skirt_btn.show()
        self.blue_skirt_btn.show()

        # Кнопка "Назад"
        self.back_btn = QPushButton('Назад', self)
        self.back_btn.setGeometry(10, 10, 100, 30)
        self.back_btn.clicked.connect(self.back1)
        self.back_btn.show()

# МЕТОДЫ ОТРИСОВКИ ЮБОК
    def put_on_black(self):
        # Скрываем предыдущую юбку
        self.skirt_img.hide()

        # Загружаем картинку черной юбки
        skirt_pixmap = QPixmap('img/black_skirt.png')
        # Масштабируем картинку
        skirt_pixmap = skirt_pixmap.scaled(200, 100)
        # Устанавливаем картинку на QLabel
        self.skirt_img.setPixmap(skirt_pixmap)
        # Устанавливаем позицию
        self.skirt_img.move(180, 340)
        # Показываем QLabel с юбкой
        self.skirt_img.show()

    def put_on_blue(self):
        self.skirt_img.hide()

        skirt_pixmap = QPixmap('img/blue_skirt.png')
        skirt_pixmap = skirt_pixmap.scaled(210, 100)
        self.skirt_img.setPixmap(skirt_pixmap)
        self.skirt_img.move(180, 340)
        self.skirt_img.show()

    def put_on_purple(self):
        self.skirt_img.hide()

        skirt_pixmap = QPixmap('img/purple_skirt.png')
        skirt_pixmap = skirt_pixmap.scaled(220, 100)
        self.skirt_img.setPixmap(skirt_pixmap)
        self.skirt_img.move(170, 340)
        self.skirt_img.show()

    def put_on_pink(self):
        self.skirt_img.hide()

        skirt_pixmap = QPixmap('img/pink_skirt.png')
        skirt_pixmap = skirt_pixmap.scaled(220, 100)
        self.skirt_img.setPixmap(skirt_pixmap)
        self.skirt_img.move(170, 340)
        self.skirt_img.show()

# МЕТОД ВОЗВРАТА В ГЛАВНОЕ МЕНЮ ИЗ РАЗДЕЛА ЮБОК
    def back1(self):
        # Показываем кнопки главного меню
        self.button1.show()
        self.button2.show()
        self.button7.show()

        # Скрываем кнопки выбора юбок
        self.purple_skirt_btn.hide()
        self.pink_skirt_btn.hide()
        self.black_skirt_btn.hide()
        self.blue_skirt_btn.hide()

        # Скрываем кнопку "Назад"
        self.back_btn.hide()

# МЕТОДЫ ОТРИСОВКИ ТОПОВ
    def put_on_black1(self):
        # Скрываем предыдущий топ
        self.top_img.hide()

        # Загружаем картинку черного топа
        top_pixmap = QPixmap('img/black1_top.png')
        # Масштабируем
        top_pixmap = top_pixmap.scaled(300, 185)
        # Устанавливаем изображение
        self.top_img.setPixmap(top_pixmap)
        # Указываем позицию
        self.top_img.move(200, 240)
        # Показываем QLabel с топом
        self.top_img.show()

    def put_on_red(self):
        self.top_img.hide()

        top_pixmap = QPixmap('img/red_top.png')
        top_pixmap = top_pixmap.scaled(300, 200)
        self.top_img.setPixmap(top_pixmap)
        self.top_img.move(130, 240)
        self.top_img.show()

    def put_on_blackk(self):
        self.top_img.hide()

        top_pixmap = QPixmap('img/blackk_top.png')
        top_pixmap = top_pixmap.scaled(280, 160)
        self.top_img.setPixmap(top_pixmap)
        self.top_img.move(200, 240)
        self.top_img.show()

    def put_on_sweater(self):
        self.top_img.hide()

        top_pixmap = QPixmap('img/sweater_top.png')
        top_pixmap = top_pixmap.scaled(290, 165)
        self.top_img.setPixmap(top_pixmap)
        self.top_img.move(130, 230)
        self.top_img.show()

# МЕТОД ВОЗВРАТА В ГЛАВНОЕ МЕНЮ ИЗ РАЗДЕЛА ТОПОВ
    def back2(self):
        # Показываем кнопки главного меню
        self.button1.show()
        self.button2.show()
        self.button7.show()

        # Скрываем кнопки выбора топов
        self.red_top_btn.hide()
        self.sweater_btn.hide()
        self.black_top_btn.hide()
        self.chorn_top_btn.hide()

        # Скрываем кнопку "Назад"
        self.back_top_btn.hide()

    # МЕТОДЫ СБРОСА ЭЛЕМЕНТОВ ОДЕЖДЫ
    def reset_all(self):
        # Сброс юбки
        self.current_skirt = None
        self.skirt_img.hide()
        self.skirt_img.setPixmap(QPixmap())
        self.previous_skirt = None
        self.saved_skirt = None

        # Сброс топа
        self.current_top = None
        self.top_img.hide()
        self.top_img.setPixmap(QPixmap())
        self.previous_top = None
        self.saved_top = None

    def reset_skirt(self):
        # Сброс юбки
        self.current_skirt = None
        self.skirt_img.hide()
        self.skirt_img.setPixmap(QPixmap())
        self.previous_skirt = None
        self.saved_skirt = None

    def reset_top(self):
        # Сброс топа
        self.current_top = None
        self.top_img.hide()
        self.top_img.setPixmap(QPixmap())
        self.previous_top = None
        self.saved_top = None

    # МЕТОД СОХРАНЕНИЯ СКРИНШОТА ВЫБРАННОЙ ОДЕЖДЫ
    def save(self):
        screen = QApplication.primaryScreen()
        x = 100
        y = 100
        width = 300
        height = 450
        screenshot = screen.grabWindow(self.winId(), x, y, width, height)

        fname = QFileDialog.getSaveFileName(self, 'Save Screenshot', 'screenshot.png')
        if fname[0]:
            screenshot.save(fname[0])

# МЕТОД ЗАКРЫТИЯ ПРИЛОЖЕНИЯ
    def show_result(self):
        print('Закрытие приложения')
        app = QApplication.instance()
        app.close()

# Запуск приложения
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
