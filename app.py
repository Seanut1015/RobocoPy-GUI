import subprocess
import sys
import time
from pathlib import Path

from PyQt6.QtCore import QObject, Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import (QApplication, QFileDialog, QMessageBox,
                             QStyleFactory, QWidget)

from config_util import *
from UI_files.UI import Ui_Form
from UI_files.UI_Color import *

QApplication.setHighDpiScaleFactorRoundingPolicy(
    Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)


class RobocopyWorker(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(str)
    result = pyqtSignal(int, float)

    def __init__(self, cmd):
        super().__init__()
        self.cmd = cmd

    def run(self):
        try:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = 0  # SW_HIDE
            start_time = time.time()
            result = subprocess.run(
                self.cmd,
                capture_output=True,
                text=True,
                check=False,
                startupinfo=startupinfo
            )
            elapsed = time.time() - start_time
            self.result.emit(result.returncode, elapsed)

        except Exception as e:
            self.error.emit(str(e))
        finally:
            self.finished.emit()


class MyWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.s1 = True
        self.s2 = False
        self.status = "複製"
        self.log_path.setText("log.txt")
        self.progressBar.setRange(0, 100)

        self.j_cb.stateChanged.connect(self.check_j_z_conflict)
        self.z_cb.stateChanged.connect(self.check_j_z_conflict)

        self.e_cb.stateChanged.connect(self.check_ees_conflict)
        self.not_e_s_cb.stateChanged.connect(self.check_ees_conflict)

        self.log_cb.stateChanged.connect(self.check_log_conflict)

        self.is_cb.stateChanged.connect(self.check_if_xn_xo_conflict)
        self.xn_cb.stateChanged.connect(self.check_if_xn_xo_conflict)
        self.xo_cb.stateChanged.connect(self.check_if_xn_xo_conflict)

        self.comboBox_2.currentIndexChanged.connect(self.limit_time)

        self.thread = None
        self.worker = None
        load_config(self)
        self.already = not self.preview_cb.checkState() == Qt.CheckState.Checked

    def source_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Source Folder")
        if folder:
            self.source_path.setText(folder)

    def det_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Target Folder")
        if folder:
            self.det_path.setText(folder)

    def preview_cmd(self):
        self.already = not self.already

    def start(self):
        source = Path(self.source_path.text())
        dest = Path(self.det_path.text())

        if self.source_path.text() == "":
            QMessageBox.critical(self, "錯誤", "請選擇來源資料夾")
            return
        if self.det_path.text() == "":
            QMessageBox.critical(self, "錯誤", "請選擇目標資料夾")
            return
        if not source.exists():
            QMessageBox.critical(self, "錯誤", f"來源資料夾不存在：{source}")
            return

        mt_s = self.mt_sb.value()
        if self.i_s_cb.checkState() == Qt.CheckState.Checked:
            dest = dest / source.name

        cmd = ["robocopy", str(source), str(dest)]

        if self.radioButton_2.isChecked():
            cmd.append("/MOVE")
            self.status = "移動"
            self.cancel_btn.setEnabled(False)
        elif self.radioButton_3.isChecked():
            self.status = "鏡像"
            cmd.append("/MIR")
        if self.mt_cb.checkState() == Qt.CheckState.Checked:
            cmd.append(f"/MT:{mt_s}")
        if self.j_cb.checkState() == Qt.CheckState.Checked:
            cmd.append("/J")
        if self.z_cb.checkState() == Qt.CheckState.Checked:
            cmd.append("/Z")
        if self.is_cb.checkState() == Qt.CheckState.Checked:
            cmd.append("/IS")
        if self.xn_cb.checkState() == Qt.CheckState.Checked:
            cmd.append("/XN")
        if self.xo_cb.checkState() == Qt.CheckState.Checked:
            cmd.append("/XO")
        cmd.append("/R:" + str(self.rt_time.value() *
                   10**self.comboBox.currentIndex()))
        cmd.append("/W:" + str(self.wait_time.value() *
                   60**self.comboBox_2.currentIndex()))
        e_ = "/E" if self.e_cb.checkState() == Qt.CheckState.Checked else "/S"
        if not self.not_e_s_cb.checkState() == Qt.CheckState.Checked:
            cmd.append(e_)

        exclude_file = source / "exclude.txt"
        try:
            with open(exclude_file, encoding="utf-8") as f:
                lines = [line.strip() for line in f if line.strip()]
                xd_list = []
                xf_list = ["exclude.txt"]
                for line in lines:
                    path = source / line
                    print(path)
                    if path.is_dir():
                        xd_list.append(line)
                    else:
                        xf_list.append(line)
            if self.xd_xf_cb.checkState() == Qt.CheckState.Checked:
                if xd_list:
                    cmd += ["/XD"] + xd_list
                if xf_list:
                    cmd += ["/XF"] + xf_list
        except FileNotFoundError:
            pass
        log_set = "/unilog:" if self.logp_cb.checkState() == Qt.CheckState.Checked else "/unilog+:"
        log_set += self.log_path.text()
        if self.log_cb.checkState() == Qt.CheckState.Checked:
            cmd.append(log_set)
        if not self.nfl_cb.checkState() == Qt.CheckState.Checked:
            cmd.append("/NFL")
            cmd.append("/NP")
        if not self.ndl_cb.checkState() == Qt.CheckState.Checked:
            cmd.append("/NDL")
        # 準備 QThread 任務
        if self.preview_cb.checkState() == Qt.CheckState.Checked:
            reply = QMessageBox.question(
                self, "預覽", f"Robocopy 命令：\n{' '.join(cmd)}",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.No:
                return
            self.already = not self.already

        if self.already:
            self.progressBar.setValue(0)
            self.progressBar.setRange(0, 0)
            self.label.setText(f"正在{self.status}中")
            self.thread = QThread()
            self.worker = RobocopyWorker(cmd)
            self.worker.moveToThread(self.thread)

            self.thread.started.connect(self.worker.run)
            self.worker.result.connect(self.on_result)
            self.worker.error.connect(self.on_error)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.start_btn.setEnabled(False)
            self.thread.start()

    def on_result(self, returncode, elapsed_time):
        self.progressBar.setRange(0, 100)
        self.progressBar.setValue(100)
        if returncode >= 8:
            QMessageBox.critical(
                self, "錯誤", f"Robocopy 失敗，返回碼：{returncode}")

        else:
            QMessageBox.information(
                self, "完成", f"資料傳輸完成\n耗時：{elapsed_time:.3f} 秒")
        self.already = not self.preview_cb.checkState() == Qt.CheckState.Checked
        self.label.setText("準備中...")
        self.progressBar.setValue(0)
        self.cancel_btn.setEnabled(True)
        self.start_btn.setEnabled(True)
        save_config(self)

    def on_error(self, message):
        self.progressBar.setValue(0)
        QMessageBox.critical(self, "異常錯誤", message)

    def cancel(self):
        save_config(self)
        self.close()

    def check_log_conflict(self):
        if self.log_cb.isChecked():
            self.logp_cb.setEnabled(True)
            self.ndl_cb.setEnabled(True)
            self.nfl_cb.setEnabled(True)
        else:
            self.logp_cb.setEnabled(False)
            self.ndl_cb.setEnabled(False)
            self.nfl_cb.setEnabled(False)

    def check_ees_conflict(self):
        if self.e_cb.isChecked():
            self.not_e_s_cb.setEnabled(False)
        else:
            self.not_e_s_cb.setEnabled(True)

        if self.not_e_s_cb.isChecked():
            self.e_cb.setEnabled(False)
        else:
            self.e_cb.setEnabled(True)

    def check_j_z_conflict(self):
        if self.j_cb.isChecked():
            self.z_cb.setEnabled(False)
        else:
            self.z_cb.setEnabled(True)

        if self.z_cb.isChecked():
            self.j_cb.setEnabled(False)
        else:
            self.j_cb.setEnabled(True)

    def check_if_xn_xo_conflict(self):
        if self.is_cb.isChecked():
            self.xn_cb.setEnabled(False)
            self.xo_cb.setEnabled(False)
        else:
            self.xn_cb.setEnabled(True)
            self.xo_cb.setEnabled(True)

        if self.xn_cb.isChecked() or self.xo_cb.isChecked():
            self.is_cb.setEnabled(False)
        else:
            self.is_cb.setEnabled(True)

    def limit_time(self):
        if self.comboBox_2.currentIndex() == 2:
            self.wait_time.setMaximum(18)
        else:
            self.wait_time.setMaximum(59)

    def log_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Log Folder")
        if folder:
            self.log_path.setText(folder+"/log.txt")

    def mir_warning(self):
        if self.mir_w_cb.checkState() == Qt.CheckState.Checked:
            return
        if self.radioButton_3.isChecked():
            reply = QMessageBox.warning(
                self, "警告", "使用鏡像會刪除目標資料夾中多出的檔案，是否繼續？",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.No:
                self.radioButton.setChecked(True)

    # def toggle_theme(self):
    #     if self.dark_cb.isChecked():
    #         app.setPalette(dark())
    #         app.setStyleSheet(dark_qss())

    #     else:
    #         app.setPalette(light())
    #         app.setStyleSheet(light_qss())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("WindowsVista"))
    # app.setStyle(QStyleFactory.create("Fusion"))

    ui = MyWindow()
    ui.setWindowTitle("RobocoPy-GUI")
    ui.show()
    sys.exit(app.exec())
