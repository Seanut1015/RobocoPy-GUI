from PyQt6 import QtGui


def dark():
    palette = QtGui.QPalette()

    # 基本顏色設定
    palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor(37, 37, 38))
    palette.setColor(QtGui.QPalette.ColorRole.WindowText,
                     QtGui.QColor(220, 220, 220))
    palette.setColor(QtGui.QPalette.ColorRole.Base, QtGui.QColor(55, 55, 61))
    palette.setColor(QtGui.QPalette.ColorRole.AlternateBase,
                     QtGui.QColor(55, 55, 60))
    palette.setColor(QtGui.QPalette.ColorRole.ToolTipBase,
                     QtGui.QColor(45, 45, 50))
    palette.setColor(QtGui.QPalette.ColorRole.ToolTipText,
                     QtGui.QColor(230, 230, 230))
    palette.setColor(QtGui.QPalette.ColorRole.Text,
                     QtGui.QColor(220, 220, 220))
    palette.setColor(QtGui.QPalette.ColorRole.Button, QtGui.QColor(60, 60, 65))
    palette.setColor(QtGui.QPalette.ColorRole.ButtonText,
                     QtGui.QColor(220, 220, 220))
    palette.setColor(QtGui.QPalette.ColorRole.BrightText,
                     QtGui.QColor(255, 255, 255))
    # palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor(45, 45, 50))
    # palette.setColor(QtGui.QPalette.ColorRole.WindowText,
    #                  QtGui.QColor(230, 230, 230))
    # palette.setColor(QtGui.QPalette.ColorRole.Base, QtGui.QColor(30, 30, 35))
    # palette.setColor(QtGui.QPalette.ColorRole.AlternateBase,
    #                  QtGui.QColor(55, 55, 60))
    # palette.setColor(QtGui.QPalette.ColorRole.ToolTipBase,
    #                  QtGui.QColor(45, 45, 50))
    # palette.setColor(QtGui.QPalette.ColorRole.ToolTipText,
    #                  QtGui.QColor(230, 230, 230))
    # palette.setColor(QtGui.QPalette.ColorRole.Text,
    #                  QtGui.QColor(230, 230, 230))
    # palette.setColor(QtGui.QPalette.ColorRole.Button, QtGui.QColor(60, 60, 65))
    # palette.setColor(QtGui.QPalette.ColorRole.ButtonText,
    #                  QtGui.QColor(230, 230, 230))
    # palette.setColor(QtGui.QPalette.ColorRole.BrightText,
    #                  QtGui.QColor(255, 255, 255))

    # 高亮和焦點配色 - 使用更鮮明的藍色
    palette.setColor(QtGui.QPalette.ColorRole.Highlight,
                     QtGui.QColor(0, 120, 215))  # Qt5 風格藍色
    palette.setColor(QtGui.QPalette.ColorRole.HighlightedText,
                     QtGui.QColor(255, 255, 255))

    # 鏈接顏色
    palette.setColor(QtGui.QPalette.ColorRole.Link, QtGui.QColor(86, 153, 255))
    palette.setColor(QtGui.QPalette.ColorRole.LinkVisited,
                     QtGui.QColor(153, 123, 230))

    # 禁用控件的顏色
    palette.setColor(QtGui.QPalette.ColorGroup.Disabled,
                     QtGui.QPalette.ColorRole.Text, QtGui.QColor(150, 150, 150))
    palette.setColor(QtGui.QPalette.ColorGroup.Disabled,
                     QtGui.QPalette.ColorRole.ButtonText, QtGui.QColor(150, 150, 150))
    palette.setColor(QtGui.QPalette.ColorGroup.Disabled,
                     QtGui.QPalette.ColorRole.WindowText, QtGui.QColor(150, 150, 150))

    return palette


def dark_qss():
    return """
    QCheckBox::indicator:disabled,
    QRadioButton::indicator:disabled {
    background-color: #2c2c31;
    border: 1px solid #6e6e6e;
    }
    QCheckBox:disabled,
    QRadioButton:disabled {
    color: #8c8c8c;
    }
    """


def light():
    palette = QtGui.QPalette()

    # 基本顏色設定
    palette.setColor(QtGui.QPalette.ColorRole.Window,
                     QtGui.QColor(245, 245, 248))
    palette.setColor(QtGui.QPalette.ColorRole.WindowText,
                     QtGui.QColor(55, 55, 60))
    palette.setColor(QtGui.QPalette.ColorRole.Base,
                     QtGui.QColor(255, 255, 255))
    palette.setColor(QtGui.QPalette.ColorRole.AlternateBase,
                     QtGui.QColor(235, 235, 240))
    palette.setColor(QtGui.QPalette.ColorRole.ToolTipBase,
                     QtGui.QColor(235, 235, 240))
    palette.setColor(QtGui.QPalette.ColorRole.ToolTipText,
                     QtGui.QColor(55, 55, 60))
    palette.setColor(QtGui.QPalette.ColorRole.Text, QtGui.QColor(55, 55, 60))
    palette.setColor(QtGui.QPalette.ColorRole.Button,
                     QtGui.QColor(230, 230, 235))
    palette.setColor(QtGui.QPalette.ColorRole.ButtonText,
                     QtGui.QColor(55, 55, 60))
    palette.setColor(QtGui.QPalette.ColorRole.BrightText,
                     QtGui.QColor(20, 20, 25))

    # 高亮和焦點配色 - 使用更鮮明的藍色
    palette.setColor(QtGui.QPalette.ColorRole.Highlight,
                     QtGui.QColor(0, 120, 215))  # Qt5 風格藍色
    palette.setColor(QtGui.QPalette.ColorRole.HighlightedText,
                     QtGui.QColor(255, 255, 255))

    # 鏈接顏色
    palette.setColor(QtGui.QPalette.ColorRole.Link, QtGui.QColor(0, 102, 220))
    palette.setColor(QtGui.QPalette.ColorRole.LinkVisited,
                     QtGui.QColor(102, 51, 153))

    # 禁用控件的顏色
    palette.setColor(QtGui.QPalette.ColorGroup.Disabled,
                     QtGui.QPalette.ColorRole.Text, QtGui.QColor(170, 170, 170))
    palette.setColor(QtGui.QPalette.ColorGroup.Disabled,
                     QtGui.QPalette.ColorRole.ButtonText, QtGui.QColor(170, 170, 170))
    palette.setColor(QtGui.QPalette.ColorGroup.Disabled,
                     QtGui.QPalette.ColorRole.WindowText, QtGui.QColor(170, 170, 170))

    return palette


def light_qss():
    return """
    QCheckBox::indicator:disabled,
    QRadioButton::indicator:disabled {
    background-color: #e6e6e6;
    border: 1px solid #bebebe;
    }
    QCheckBox:disabled,
    QRadioButton:disabled {
    color: #b4b4b4;
    }
    """
