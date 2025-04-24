# 📦 專案名稱 RobocoPy-GUI

## 📝 專案簡介
本專案基於 Python 與 PyQt5 開發的桌面應用程式。  
主要功能為提供圖形化介面，方便使用者操作Robocopy，可依照需求調整參數，適用於備份、轉移檔案等用途。  


# 使用者專區

## 🚨 警告
- 本程式目前還在Beta版本
- 由於本人沒有申請數位憑證，可能會被系統判斷為病毒

## 💡 使用方式
1. 雙擊exe檔案即可使用
2. 使用者可透過圖形介面進行"複製、移動檔案"等操作。
3. 功能包含參數設定、資料夾路徑、設定檔等，詳見程式內選項說明。

##

# 開發者專區

## 🛠️ 使用技術
- Python 3.13
- 請參考requirements.txt

## 🧰 安裝方式

### 開發環境建立
- 點擊build_env/_venv.bat 即可自動建立venv開發環境

## 💡 使用方式
1. 啟動主程式：
```bash
#進入venv環境後
python app.py
```

## 📂 專案結構範例
```
project/
├── assets/                # 圖片、圖示等資源(空)
├── build_env/_venv.bat    # 根據requirements自動建立venv
├── resources/             # 其他資源(空)
├── UI_files/      
│         ├──__init__.py   # 空白文件，用於識別UI檔案(不要刪除)       
│         ├── untitled.ui  # QT .ui檔案
│         └── UI.py        # 轉換後的.py檔
├── _py2exe.bat            # 自動打包成.exe
├── _requirements.bat      # 輸出當前venv環境至requirements.txt
├── _UI2py.bat             # 將.ui檔轉換為.py檔
├── app.py                 # 主程式
├── README.md
└── requirements.txt       # 所需套件列表
```
- venv會建立至project目錄內
- 請不要移動.bat檔案位置

## 💻 執行環境需求
- 作業系統：僅能使用於Windows 7含以上(建議使用win10)

## 🔧 開發環境
- Python 版本：3.13
- 請參考requirements.txt
- 最低建議硬體：4GB RAM，基本 CPU

## 📸 擷圖與範例 (Optional)
> 可在此放上程式畫面截圖或使用流程示意圖

## 📄 授權條款
本專案採用 [GNU General Public License v3.0 (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.html) 授權條款：
- ✅ 可自由使用、修改、再發佈
- 🔁 衍生作品須以相同授權條款開源
- ❌ 禁止將本專案整合至專有或商業軟體中

## 👤 作者
- 作者：Seanut

