import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

def main():
    app = QApplication(sys.argv)

    # Ventana principal
    window = QWidget()
    window.setWindowTitle("Prueba PyInstaller")
    window.resize(300, 200)

    # Layout vertical
    layout = QVBoxLayout()

    # Etiqueta
    label = QLabel("¡Hola, PyQt!")
    label.setAlignment(Qt.AlignCenter)
    layout.addWidget(label)

    # Botón
    btn = QPushButton("Haz clic aquí")
    def on_click():
        label.setText("¡Funciona correctamente!")
    btn.clicked.connect(on_click)
    layout.addWidget(btn)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
