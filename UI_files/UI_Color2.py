from PyQt6 import QtGui


def light():
    palette = QtGui.QPalette()

    palette.setColor(QtGui.QPalette.ColorRole.Window,
                     QtGui.QColor(255, 255, 255))
    palette.setColor(QtGui.QPalette.ColorRole.WindowText,
                     QtGui.QColor(0, 0, 0))
    palette.setColor(QtGui.QPalette.ColorRole.Base,
                     QtGui.QColor(255, 255, 255))
    palette.setColor(QtGui.QPalette.ColorRole.AlternateBase,
                     QtGui.QColor(240, 240, 240))
    palette.setColor(QtGui.QPalette.ColorRole.ToolTipBase,
                     QtGui.QColor(255, 255, 220))
    palette.setColor(QtGui.QPalette.ColorRole.ToolTipText,
                     QtGui.QColor(0, 0, 0))
    palette.setColor(QtGui.QPalette.ColorRole.Text, QtGui.QColor(0, 0, 0))
    palette.setColor(QtGui.QPalette.ColorRole.Button,
                     QtGui.QColor(240, 240, 240))
    palette.setColor(QtGui.QPalette.ColorRole.ButtonText,
                     QtGui.QColor(0, 0, 0))
    palette.setColor(QtGui.QPalette.ColorRole.BrightText,
                     QtGui.QColor(255, 0, 0))
    palette.setColor(QtGui.QPalette.ColorRole.Highlight,
                     QtGui.QColor(0, 120, 215))
    palette.setColor(QtGui.QPalette.ColorRole.HighlightedText,
                     QtGui.QColor(255, 255, 255))

    return palette


def classic():
    palette = QtGui.QPalette()

    palette.setColor(QtGui.QPalette.ColorRole.Window,
                     QtGui.QColor(240, 240, 240))
    palette.setColor(QtGui.QPalette.ColorRole.WindowText,
                     QtGui.QColor(0, 0, 0))
    palette.setColor(QtGui.QPalette.ColorRole.Base,
                     QtGui.QColor(255, 255, 255))
    palette.setColor(QtGui.QPalette.ColorRole.AlternateBase,
                     QtGui.QColor(233, 231, 227))
    palette.setColor(QtGui.QPalette.ColorRole.ToolTipBase,
                     QtGui.QColor(255, 255, 220))
    palette.setColor(QtGui.QPalette.ColorRole.ToolTipText,
                     QtGui.QColor(0, 0, 0))
    palette.setColor(QtGui.QPalette.ColorRole.Text, QtGui.QColor(0, 0, 0))
    palette.setColor(QtGui.QPalette.ColorRole.Button,
                     QtGui.QColor(240, 240, 240))
    palette.setColor(QtGui.QPalette.ColorRole.ButtonText,
                     QtGui.QColor(0, 0, 0))
    palette.setColor(QtGui.QPalette.ColorRole.Highlight,
                     QtGui.QColor(0, 120, 215))
    palette.setColor(QtGui.QPalette.ColorRole.HighlightedText,
                     QtGui.QColor(255, 255, 255))

    return palette


def dark():
    palette = QtGui.QPalette()

    palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ColorRole.WindowText,
                     QtGui.QColor(204, 204, 204))
    palette.setColor(QtGui.QPalette.ColorRole.Base, QtGui.QColor(35, 35, 35))
    palette.setColor(QtGui.QPalette.ColorRole.AlternateBase,
                     QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ColorRole.ToolTipBase,
                     QtGui.QColor(255, 255, 220))
    palette.setColor(QtGui.QPalette.ColorRole.ToolTipText,
                     QtGui.QColor(0, 0, 0))
    palette.setColor(QtGui.QPalette.ColorRole.Text,
                     QtGui.QColor(204, 204, 204))
    palette.setColor(QtGui.QPalette.ColorRole.Button, QtGui.QColor(51, 51, 51))
    palette.setColor(QtGui.QPalette.ColorRole.ButtonText,
                     QtGui.QColor(204, 204, 204))
    palette.setColor(QtGui.QPalette.ColorRole.Highlight,
                     QtGui.QColor(142, 45, 197))
    palette.setColor(QtGui.QPalette.ColorRole.HighlightedText,
                     QtGui.QColor(0, 0, 0))

    return palette
