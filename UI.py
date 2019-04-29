from Qt.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLable, QLineEdit, QListWidget, QComboBox
from Qt.QtGui import QIcon, QPixmap
from Qt.QtCore import Qt as qtc

class UI(QWidget):
  """
  UI initializing
  """
  
  def __init__(self):
    super(UI, self).__init__()
    self.textbox = QLineEdit(self)
    self.item_list_widget = QCombobox(self)
    self.showUI()
    
  def showUI(self):
    """
    UI action linking and layout here
    """
    self.btn_press = QPushButton('Press Here', self)
    self.btn_press.clicked.connect(self.action)
    self.item_list_widget.currentIndexChanged.connect(self.selectionChanged)
    
    # creating list with None
    self.item_list_widget.addItem("None")
    
    # UI layout
    
    layout = QVBoxLayout(self)
    layout.addWidget(self.textbox)
    layout.addWidget(self.btn_press)
    layout.addWidget(self.item_list_widget)
    
  def action(self):
    """
    action after pressing buttopm
    """
    self.item_list_widget.clear()
    ls = []
    text_box_value = self.textbox.text()
    print text_box_value
    ls = ['test1', 'test2', 'test3']
    self.item_list_widget.addItems(ls)
    
  def selectionChanged(self):
    """
    changing selection on qcombobox will bring you here
    """
    print self.item_list_widget.currentText()
