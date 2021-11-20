import random
import sys
from PyQt5 import uic
import Ui
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class main(Ui.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.pushButton.hide()
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        r = random.randint(1, 100)
        qp.drawEllipse(350, 350, r, r)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main()
    ex.show()
    sys.exit(app.exec())