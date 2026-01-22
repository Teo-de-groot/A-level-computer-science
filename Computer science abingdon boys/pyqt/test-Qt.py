import math
import sys
import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg

def cancel():
    sys.exit()

timesclicked = 0
def buttonclicked(item: qtw.QLabel):
    global timesclicked
    item.setText(f"Button pressed {timesclicked} times.")
    timesclicked += 1

class CatapultSlider(qtw.QWidget):
    valueChanged = qtc.pyqtSignal(int)
    angularVelocityChanged = qtc.pyqtSignal(float)
    angleChanged = qtc.pyqtSignal(float)

    def __init__(self, minimum=0, maximum=100):
        super().__init__()
        self.setMinimumSize(220, 220)
        self.minimum = minimum
        self.maximum = maximum
        self.angle = 0.0
        self.angular_vel = 0.0
        self.drag_start_angle = 0.0
        self.is_dragging = False
        self.radius = 70
        self.handle_radius = 8
        self.timer = qtc.QTimer(self)
        self.timer.timeout.connect(self.update_physics)
        self.timer.start(16)

    def mousePressEvent(self, e):
        self.is_dragging = True
        self.drag_start_angle = self.angle_from_mouse(e.position())
        self.angular_vel = 0.0
        self.angularVelocityChanged.emit(self.angular_vel)

    def mouseMoveEvent(self, e):
        if self.is_dragging:
            self.angle = self.angle_from_mouse(e.position())
            self.emit_value()

    def mouseReleaseEvent(self, e):
        if self.is_dragging:
            release_angle = self.angle_from_mouse(e.position())
            self.angular_vel = (self.drag_start_angle - release_angle) * 0.25
            self.is_dragging = False
            self.angularVelocityChanged.emit(self.angular_vel)

    def update_physics(self):
        if not self.is_dragging:
            self.angle += self.angular_vel
            self.angular_vel *= 0.95
            self.angle %= 360
            self.emit_value()
            self.angularVelocityChanged.emit(self.angular_vel)
        self.angleChanged.emit(self.angle)
        self.update()

    def angle_from_mouse(self, pos):
        cx = self.width() / 2
        cy = self.height() / 2
        dx = pos.x() - cx
        dy = pos.y() - cy
        return math.degrees(math.atan2(dy, dx)) % 360

    def emit_value(self):
        ratio = self.angle / 360.0
        value = int(self.minimum + ratio * (self.maximum - self.minimum))
        self.valueChanged.emit(value)

    def paintEvent(self, e):
        p = qtg.QPainter(self)
        p.setRenderHint(qtg.QPainter.RenderHint.Antialiasing)
        cx = self.width() // 2
        cy = self.height() // 2
        p.setPen(qtg.QPen(qtg.QColor("#444"), 6))
        p.setBrush(qtc.Qt.BrushStyle.NoBrush)
        p.drawEllipse(cx - self.radius, cy - self.radius, self.radius * 2, self.radius * 2)
        rad = math.radians(self.angle)
        hx = cx + math.cos(rad) * self.radius
        hy = cy + math.sin(rad) * self.radius
        p.setPen(qtc.Qt.PenStyle.NoPen)
        p.setBrush(qtg.QColor("black"))
        p.drawEllipse(int(hx - self.handle_radius), int(hy - self.handle_radius), self.handle_radius * 2, self.handle_radius * 2)

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Template Window")
        layout = qtw.QVBoxLayout()
        self.comboBox = qtw.QComboBox()
        self.comboBox.addItems(["Cerise", "Black", "Partymode (epilepsy warning)"])
        layout.addWidget(self.comboBox)
        self.slider = CatapultSlider(0, 100)
        self.valueLabel = qtw.QLabel("Value: 0")
        self.valueLabel.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        self.velocityLabel = qtw.QLabel("Speed: 0.00")
        self.velocityLabel.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        self.slider.valueChanged.connect(lambda v: self.valueLabel.setText(f"Value: {v}"))
        self.slider.angularVelocityChanged.connect(lambda v: self.velocityLabel.setText(f"Speed: {v:.2f}"))
        slider_layout = qtw.QVBoxLayout()
        slider_layout.addWidget(self.slider)
        slider_layout.addWidget(self.valueLabel)
        slider_layout.addWidget(self.velocityLabel)
        layout.addLayout(slider_layout)
        form = qtw.QFormLayout()
        self.nameEdit = qtw.QLineEdit()
        self.nameEdit.setPlaceholderText("Username")
        self.PasswordEdit = qtw.QLineEdit()
        self.PasswordEdit.setPlaceholderText("Password")
        form.addRow("Username:", self.nameEdit)
        form.addRow("Password:", self.PasswordEdit)
        layout.addLayout(form)
        def toggle_password():
            if self.PasswordEdit.echoMode() == qtw.QLineEdit.EchoMode.Normal:
                self.PasswordEdit.setEchoMode(qtw.QLineEdit.EchoMode.Password)
            else:
                self.PasswordEdit.setEchoMode(qtw.QLineEdit.EchoMode.Normal)
        self.showPasswordButton = qtw.QPushButton("Show/Hide Password")
        self.showPasswordButton.clicked.connect(toggle_password)
        layout.addWidget(self.showPasswordButton)
        self.formlayout = qtw.QFormLayout()
        self.label=qtw.QLabel("Celcius to:")
        self.celciusinput=qtw.QLineEdit()
        self.Kelvinoutput=qtw.QLabel("Kelvin:")
        def convertkelvintocelcius():
            try:
                celcius=float(self.celciusinput.text())
                kelvin=celcius+273.15
                self.Kelvinoutput.setText(f"Kelvin: {kelvin:.2f}")
            except ValueError:
                self.Kelvinoutput.setText("Kelvin: Invalid input")
        self.celciusinput.textChanged.connect(convertkelvintocelcius)
        self.formlayout.addRow(self.label, self.celciusinput)
        self.formlayout.addRow(self.Kelvinoutput)
        layout.addLayout(self.formlayout)
        self.buttton = qtw.QPushButton("Count clicks")
        self.buttton.clicked.connect(lambda: buttonclicked(self.buttton))
        layout.addWidget(self.buttton)
        self.cancelButton = qtw.QPushButton("Ok")
        self.cancelButton.clicked.connect(cancel)
        layout.addWidget(self.cancelButton)
        self.textbox = qtw.QTextEdit()
        self.textbox.setPlaceholderText("Dont put text here...")
        layout.addWidget(self.textbox)
        self.textbox_timer = qtc.QTimer(self)
        self.textbox_timer.setSingleShot(True)
        self.textbox_timer.timeout.connect(self.clear_textbox)
        self.textbox.textChanged.connect(self.on_textbox_changed)
        widget = qtw.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.rainbow_timer = qtc.QTimer(self)
        self.rainbow_timer.timeout.connect(self.update_rainbow)
        self.hue = 0
        self.comboBox.currentTextChanged.connect(self.update_background)
        self.update_background(self.comboBox.currentText())

    def on_textbox_changed(self):
        self.textbox_timer.start(350)

    def clear_textbox(self):
        self.textbox.clear()

    def update_background(self, text: str):
        if text == "Partymode (epilepsy warning)":
            self.hue = 0
            self.rainbow_timer.start(1)
            return
        self.rainbow_timer.stop()
        if text == "Cerise":
            color = "#de3163"
            style = ""
        elif text == "Black":
            color = "#0a0700"
            style = "color: #ffffff;"
        else:
            color = "#ffffff"
            style = ""
        self.centralWidget().setStyleSheet(f"background-color: {color}; {style}")

    def update_rainbow(self):
        color = qtg.QColor.fromHsv(self.hue, 255, 255)
        self.centralWidget().setStyleSheet(f"background-color: {color.name()};")
        self.hue = (self.hue + 5) % 360

app = qtw.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
