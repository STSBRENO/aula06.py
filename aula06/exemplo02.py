#importa classes principais para criar interface
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

#cria o aplicativo
app = QApplication([])

#cria a janela
Janela = QWidget()
Janela.setWindowTitle("Minha primeira janela")

#cria o texto dentro da janela
rotulo = QLabel("Olá, mundo!", parent=Janela)

#define o tamanho da janela
Janela.resize(300, 200)

#exibe a janela
Janela.show()

#mantem o app em execução
app.exec_()