import configparser
from pathlib import Path

from PyQt6.QtWidgets import QMessageBox

CONFIG_FILE = "config.ini"


def load_config(self):
    config = configparser.ConfigParser()
    if not Path(CONFIG_FILE).exists():
        QMessageBox.information(
            self, "未配置", f"找不到配置文件：{CONFIG_FILE}\n將使用預設設置")
        return
    config.read(CONFIG_FILE)
    self.radioButton_2.setChecked(config.getboolean("Action", "action"))
    self.mt_cb.setChecked(config.getboolean("Function", "mt"))
    self.mt_sb.setValue(config.getint("Function", "mt_s"))
    self.j_cb.setChecked(config.getboolean("Function", "j"))
    self.z_cb.setChecked(config.getboolean("Function", "z"))
    self.is_cb.setChecked(config.getboolean("Function", "if"))
    self.xn_cb.setChecked(config.getboolean("Function", "xn"))
    self.xo_cb.setChecked(config.getboolean("Function", "xo"))
    self.rt_time.setValue(config.getint("Retry", "rt"))
    self.wait_time.setValue(config.getint("Retry", "wt"))
    self.comboBox.setCurrentIndex(config.getint("Retry", "rt_unit"))
    self.comboBox_2.setCurrentIndex(config.getint("Retry", "wt_unit"))
    self.i_s_cb.setChecked(config.getboolean("Advanced", "is"))
    self.e_cb.setChecked(config.getboolean("Advanced", "e"))
    self.xd_xf_cb.setChecked(config.getboolean("Advanced", "xdf"))
    self.mir_w_cb.setChecked(config.getboolean("Advanced", "mw"))
    self.preview_cb.setChecked(config.getboolean("Advanced", "preview"))
    self.log_cb.setChecked(config.getboolean("Log", "log"))
    self.logp_cb.setChecked(config.getboolean("Log", "logp"))
    self.nfl_cb.setChecked(config.getboolean("Log", "nfl"))
    self.ndl_cb.setChecked(config.getboolean("Log", "ndl"))
    self.log_path.setText(config.get("Log", "path"))


def save_config(self):
    config = configparser.ConfigParser()
    config["Action"] = {
        "action": str(self.radioButton_2.isChecked()),
    }
    config["Function"] = {
        "mt": str(self.mt_cb.isChecked()),
        "mt_s": str(self.mt_sb.value()),
        "j": str(self.j_cb.isChecked()),
        "z": str(self.z_cb.isChecked()),
        "if": str(self.is_cb.isChecked()),
        "xn": str(self.xn_cb.isChecked()),
        "xo": str(self.xo_cb.isChecked())
    }
    config["Retry"] = {
        "rt": str(self.rt_time.text()),
        "wt": str(self.wait_time.text()),
        "rt_unit": str(self.comboBox.currentIndex()),
        "wt_unit": str(self.comboBox_2.currentIndex())
    }
    config["Advanced"] = {
        "is": str(self.i_s_cb.isChecked()),
        "e": str(self.e_cb.isChecked()),
        "xdf": str(self.xd_xf_cb.isChecked()),
        "mw": str(self.mir_w_cb.isChecked()),
        "preview": str(self.preview_cb.isChecked()),
    }
    config["Log"] = {
        "log": str(self.log_cb.isChecked()),
        "logp": str(self.logp_cb.isChecked()),
        "nfl": str(self.nfl_cb.isChecked()),
        "ndl": str(self.ndl_cb.isChecked()),
        "path": str(self.log_path.text())
    }
    with open(CONFIG_FILE, "w") as configfile:
        config.write(configfile)
