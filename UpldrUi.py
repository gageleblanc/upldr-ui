import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QTreeWidgetItem
from upldr_libs.put.put_api import PutApi
from pathlib import Path
from upldr_libs.config_utils.loader import Loader
from upldr_libs.update.remote_indexes import RemoteIndexes
from upldr_libs.get.remote_get import get_file
from clilib.util.util import Util
from mainwindow import Ui_Upldr
from SettingsWidget import SettingsWidgetUIClass
import sys
import os
from model import Model
import threading
import requests


class MainWindowUIClass(QObject):
    progress_signal = pyqtSignal(int, name="progressChanged")

    def __init__(self):
        '''Initialize the super class
        '''
        super().__init__()
        self.model = Model()
        put = PutApi(False)
        self.config = put.get_remotes()
        self.log = Util.configure_logging(name=__name__)
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            self.resource_path = sys._MEIPASS
        except Exception:
            self.resource_path = os.path.abspath(".")
        # self.progress_signal = pyqtSignal(int, name="progressChanged")

    def setupUi(self, Upldr):
        Upldr.setObjectName("Upldr")
        Upldr.resize(892, 1200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Upldr.sizePolicy().hasHeightForWidth())
        Upldr.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(Upldr)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.outputTextBrowser = QtWidgets.QTextBrowser(self.frame)
        self.outputTextBrowser.setObjectName("outputTextBrowser")
        self.gridLayout_3.addWidget(self.outputTextBrowser, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)
        self.uploadFrame = QtWidgets.QFrame(self.tab)
        self.uploadFrame.setEnabled(True)
        self.uploadFrame.setMinimumSize(QtCore.QSize(100, 25))
        self.uploadFrame.setBaseSize(QtCore.QSize(250, 30))
        self.uploadFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uploadFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.uploadFrame.setObjectName("uploadFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.uploadFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.fileNameLabel = QtWidgets.QLabel(self.uploadFrame)
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.gridLayout.addWidget(self.fileNameLabel, 0, 0, 1, 1)
        self.fileNameEdit = QtWidgets.QLineEdit(self.uploadFrame)
        self.fileNameEdit.setObjectName("fileNameEdit")
        self.gridLayout.addWidget(self.fileNameEdit, 0, 1, 1, 1)
        self.browseButton = QtWidgets.QPushButton(self.uploadFrame)
        self.browseButton.setObjectName("browseButton")
        self.gridLayout.addWidget(self.browseButton, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.uploadFrame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.categoryLine = QtWidgets.QLineEdit(self.uploadFrame)
        self.categoryLine.setObjectName("categoryLine")
        self.gridLayout.addWidget(self.categoryLine, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.uploadFrame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.tagLine = QtWidgets.QLineEdit(self.uploadFrame)
        self.tagLine.setObjectName("tagLine")
        self.gridLayout.addWidget(self.tagLine, 2, 1, 1, 2)
        self.uploadButton = QtWidgets.QPushButton(self.uploadFrame)
        self.uploadButton.setObjectName("uploadButton")
        self.gridLayout.addWidget(self.uploadButton, 3, 2, 1, 1)
        self.gridLayout_2.addWidget(self.uploadFrame, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)
        self.downloadLocation = QtWidgets.QLineEdit(self.frame_4)
        self.downloadLocation.setObjectName("downloadLocation")
        self.gridLayout_7.addWidget(self.downloadLocation, 0, 1, 1, 2)
        self.downloadBrowseButton = QtWidgets.QPushButton(self.frame_4)
        self.downloadBrowseButton.setObjectName("downloadBrowseButton")
        self.gridLayout_7.addWidget(self.downloadBrowseButton, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 1, 0, 1, 1)
        self.downloadProgress = QtWidgets.QProgressBar(self.frame_4)
        self.downloadProgress.setProperty("value", 0)
        self.downloadProgress.setObjectName("downloadProgress")
        self.gridLayout_7.addWidget(self.downloadProgress, 2, 0, 1, 4)
        self.downloadRemoteComboBox = QtWidgets.QComboBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downloadRemoteComboBox.sizePolicy().hasHeightForWidth())
        self.downloadRemoteComboBox.setSizePolicy(sizePolicy)
        self.downloadRemoteComboBox.setObjectName("downloadRemoteComboBox")
        self.gridLayout_7.addWidget(self.downloadRemoteComboBox, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.resource_path + "/icons/refresh-icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_7.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.downloadButton = QtWidgets.QPushButton(self.frame_4)
        self.downloadButton.setObjectName("downloadButton")
        self.gridLayout_7.addWidget(self.downloadButton, 1, 3, 1, 1)
        self.gridLayout_9.addWidget(self.frame_4, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.treeView = QtWidgets.QTreeWidget(self.frame_3)
        self.treeView.setObjectName("treeView")
        self.treeView.setHeaderLabels(["Files"])
        self.gridLayout_8.addWidget(self.treeView, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_3, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)
        Upldr.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Upldr)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 892, 21))
        self.menubar.setObjectName("menubar")
        self.menuUpldr = QtWidgets.QMenu(self.menubar)
        self.menuUpldr.setObjectName("menuUpldr")
        Upldr.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Upldr)
        self.statusbar.setObjectName("statusbar")
        Upldr.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(Upldr)
        self.actionSettings.setObjectName("actionSettings")
        self.menuUpldr.addAction(self.actionSettings)
        self.menubar.addAction(self.menuUpldr.menuAction())

        self.retranslateUi(Upldr)
        self.tabWidget.setCurrentIndex(0)
        self.browseButton.clicked.connect(self.browseSlot)
        self.uploadButton.clicked.connect(self.uploadSlot)
        self.fileNameEdit.returnPressed.connect(self.returnPressedSlot)
        self.actionSettings.triggered.connect(self.openSettingsSlot)
        self.downloadRemoteComboBox.currentTextChanged.connect(self.build_tree)
        self.pushButton_2.clicked.connect(self._refresh_dropdown)
        self.downloadBrowseButton.clicked.connect(self.browseDownloadSlot)
        self.downloadButton.clicked.connect(self.download_file)
        self.progress_signal.connect(self._update_progressbar)
        QtCore.QMetaObject.connectSlotsByName(Upldr)
        self.refreshAll()

    def retranslateUi(self, Upldr):
        _translate = QtCore.QCoreApplication.translate
        Upldr.setWindowTitle(_translate("Upldr", "Upldr"))
        self.fileNameLabel.setText(_translate("Upldr", "File Name"))
        self.browseButton.setText(_translate("Upldr", "Browse"))
        self.label_2.setText(_translate("Upldr", "Category"))
        self.label_3.setText(_translate("Upldr", "Tag"))
        self.uploadButton.setText(_translate("Upldr", "Upload"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Upldr", "Upload"))
        self.label.setText(_translate("Upldr", "Download Location"))
        self.downloadBrowseButton.setText(_translate("Upldr", "Browse"))
        self.label_4.setText(_translate("Upldr", "Remote"))
        self.downloadButton.setText(_translate("Upldr", "Download"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Upldr", "Download"))
        self.menuUpldr.setTitle(_translate("Upldr", "Upldr"))
        self.actionSettings.setText(_translate("Upldr", "Settings"))

        # self.tabWidget.setCurrentIndex(0)
        # self.browseButton.clicked.connect(self.browseSlot)
        # self.uploadButton.clicked.connect(self.uploadSlot)
        # self.fileNameEdit.returnPressed.connect(self.returnPressedSlot)
        # self.actionSettings.triggered.connect(self.openSettingsSlot)
        # self.downloadRemoteComboBox.currentTextChanged.connect(self._build_tree)
        # self.pushButton_2.clicked.connect(self._refresh_dropdown)
        # self.downloadBrowseButton.clicked.connect(self.browseDownloadSlot)
        # self.downloadButton.clicked.connect(self._download_file)

        # self.treeView = QtWidgets.QTreeWidget(self.frame_3)
        # self.treeView.setObjectName("treeView")
        # self.treeView.setHeaderLabels(["Files"])

    def _update_progressbar(self, val):
        self.downloadProgress.setValue(val)

    def _get_file(self, remote, category, tag, filename, output=None):
        self.downloadProgress.setValue(0)
        file_path = "%s://%s:%s/%s/%s/%s" % (remote["scheme"], remote["url"], remote["port"], category, tag, filename)
        file_res = requests.get(file_path, stream=True)
        if file_res.status_code != 200:
            self.log.fatal("Get failed with response: %d" % file_res.status_code)
        else:
            with open(output if output else filename, 'wb') as f:
                total_length = file_res.headers.get('content-length')

                if total_length is None:  # no content length header
                    f.write(file_res.content)
                else:
                    dl = 0
                    total_length = int(total_length)
                    for data in file_res.iter_content(chunk_size=4096):
                        dl += len(data)
                        f.write(data)
                        done = int(50 * dl / total_length)
                        self.progress_signal.emit(int(100 * dl / total_length))
                        # self._update_progressbar()
                        sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                        sys.stdout.flush()
            print()

    def download_file(self):
        threading.Thread(target=self._download_file).start()

    def _download_file(self):
        local_dir = self.downloadLocation.text()
        if local_dir.isspace():
            local_dir = "."
        self.log.info(self.downloadLocation.text())
        remote, category, tag, filename = self.treeView.selectedIndexes()[0].data(QtCore.Qt.UserRole).split('/')
        self.log.info("Download [%s/%s/%s] from [%s] to [%s/%s]" % (category, tag, filename, remote, local_dir, filename))
        remote_spec = self.config.remotes[remote]
        self._get_file(remote_spec, category, tag, filename, "%s/%s" % (local_dir, filename))
        self.log.info("Download Complete.")
        # print(index[0].data(QtCore.Qt.UserRole))
        # self._get_tree_path(index[0].internalPointer())

    def _update_indexes(self):
        RemoteIndexes()
        home = str(Path.home())
        config_dir = "%s/.config/upldr" % home
        config_path = "%s/.config/upldr/indexes.json" % home
        Path(config_dir).mkdir(parents=True, exist_ok=True)
        try:
            config_loader = Loader(config_path, auto_create=True, keys=['indexes'])
            self.index_object = config_loader.get_config()
        except TypeError as type_error:
            self.log.fatal(type_error)
            exit(1)

    def build_tree(self):
        self._update_configs()
        self._build_tree()

    def _build_tree(self):
        self.treeView.setHeaderLabel("Files")
        # self._update_configs()
        self.treeView.clear()
        selected_remote = self.downloadRemoteComboBox.currentText()
        items = []
        if isinstance(self.index_object.indexes, dict):
            if selected_remote in self.index_object.indexes:
                for key, values in self.index_object.indexes[selected_remote].items():
                    item = QTreeWidgetItem([key])
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemIsSelectable)
                    for tag, files in values.items():
                        child = QTreeWidgetItem([tag])
                        child.setFlags(child.flags() & ~QtCore.Qt.ItemIsSelectable)
                        for file in files:
                            file_item = QTreeWidgetItem([file])
                            file_item.setData(0, QtCore.Qt.UserRole, "%s/%s/%s/%s" % (selected_remote, key, tag, file))
                            child.addChild(file_item)
                        item.addChild(child)
                    items.append(item)
                self.treeView.insertTopLevelItems(0, items)
                self.treeView.expandAll()

    def _refresh_dropdown(self):
        self._update_configs()
        self.downloadRemoteComboBox.currentTextChanged.disconnect()
        self.downloadRemoteComboBox.clear()
        if isinstance(self.config.remotes, dict):
            for name, remote in self.config.remotes.items():
                self.downloadRemoteComboBox.addItem(name)
        self._build_tree()
        self.downloadRemoteComboBox.currentTextChanged.connect(self._build_tree)

    def _update_configs(self):
        self._update_indexes()
        self.config.reload()
        self.index_object.reload()

    def debugPrint(self, msg):
        '''Print the message in the text edit at the bottom of the
        horizontal splitter.
        '''
        self.outputTextBrowser.append(msg)

    def refreshAll(self):
        '''
        Updates the widgets whenever an interaction happens.
        Typically some interaction takes place, the UI responds,
        and informs the model of the change.  Then this method
        is called, pulling from the model information that is
        updated in the GUI.
        '''
        self.fileNameEdit.setText(self.model.getFileName())
        self._refresh_dropdown()
        # self.textEdit.setText(self.model.getFileContents())

    def _reset_form(self):
        self.categoryLine.setText("")
        self.tagLine.setText("")
        self.fileNameEdit.setText("")

    # slot
    def returnPressedSlot(self):
        ''' Called when the user enters a string in the line edit and
        presses the ENTER key.
        '''
        fileName = self.lineEdit.text()
        if self.model.isValid(fileName):
            self.model.setFileName(self.lineEdit.text())
            self.refreshAll()
        else:
            m = QtWidgets.QMessageBox()
            m.setText("Invalid file name!\n" + fileName)
            m.setIcon(QtWidgets.QMessageBox.Warning)
            m.setStandardButtons(QtWidgets.QMessageBox.Ok
                                 | QtWidgets.QMessageBox.Cancel)
            m.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            ret = m.exec_()
            self.lineEdit.setText("")
            self.refreshAll()
            self.debugPrint("Invalid file specified: " + fileName)


    # slot
    def uploadSlot(self):
        ''' Called when the user presses the Write-Doc button.
        '''
        self.outputTextBrowser.setText("")
        filename = self.fileNameEdit.text() # .split("/")[-1]
        category = self.categoryLine.text()
        tag = self.tagLine.text()
        self.debugPrint("File: %s" % filename)
        self.debugPrint("Category: %s" % category)
        self.debugPrint("Tag: %s" % tag)
        threading.Thread(target=self._run_upload, args=(filename, category, tag)).start()
        self._reset_form()

    def _run_upload(self, filename, category, tag):
        put = PutApi(False)
        config = put.get_remotes()
        self.debugPrint("Uploading to %s" % config.default)
        th = threading.Thread(target=put.make_request, kwargs={"config": config, "name": filename, "timeout": 1, "category": category, "tag": tag})
        th.start()
        th.join()
        self.debugPrint("Upload Complete")

    # slot
    def browseSlot(self):
        ''' Called when the user presses the Browse button
        '''
        # self.debugPrint( "Browse button pressed" )
        options = QtWidgets.QFileDialog.Options()
        # options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Choose file to upload",
            "",
            "All Files (*)",
            options=options)
        if fileName:
            # self.debugPrint("setting file name: " + fileName)
            self.fileNameEdit.setText(fileName)
            self.model.setFileName(fileName)
            self.refreshAll()

    def browseDownloadSlot(self):
        ''' Called when the user presses the Browse button
        '''
        # self.debugPrint( "Browse button pressed" )
        # options = QtWidgets.QFileDialog.Options()
        # options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Download Folder")
        if fileName:
            # self.debugPrint("setting file name: " + fileName)
            self.downloadLocation.setText(fileName)
            self.download_directory = fileName
            # self.refreshAll()

    def openSettingsSlot(self):
        self.SWidget = QtWidgets.QWidget()
        self.settings_ui = SettingsWidgetUIClass()
        self.settings_ui.setupUi(self.SWidget)
        self.SWidget.setWindowIcon(QtGui.QIcon(self.resource_path + "/icons/settings-icon.svg"))
        self.SWidget.show()


def main():
    """
    This is the MAIN ENTRY POINT of our application.  The code at the end
    of the mainwindow.py script will not be executed, since this script is now
    our main program.   We have simply copied the code from mainwindow.py here
    since it was automatically generated by '''pyuic5'''.

    """

    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon(base_path + "/icons/upldr-icon.svg"))
    ui = MainWindowUIClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


main()