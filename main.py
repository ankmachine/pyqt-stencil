# add shebang here eg /usr/bin/env python
from Qt.QtWidgets import QApplication
from UI import UI
import sys

def main():
  """
  main codes goes here
  """
  app = QApplication(sys.argv)
  window_ui = UI()
  window_ui.setWindowTitle("PyQt application")
  window_ui.show()
  window_ui.resize(600, 800)
  sys.exit(app.exec_())

if __name__ == '__main__':
  print "starting application"
  main()
