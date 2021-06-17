import sys
from argparse import Namespace

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QMessageBox
from PyQt5.QtCore import Qt
import itertools
import os
import threading
import MainWindowUI
import SetCategoryUI
import TrainSettingUI
import glob
import yaml


class SetCategoryWindow(QWidget):
    def __init__(self):
        super(SetCategoryWindow, self).__init__()
        self.ui = SetCategoryUI.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("ICON/window.ico"))
        self.ui.btn_close.clicked.connect(self.close)

    def closeEvent(self, event) -> None:
        reply = QMessageBox.question(self, 'Close?',
                                     "About to close the window, do you want to save the changes?", QMessageBox.Save |
                                     QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Cancel)
        if reply == QMessageBox.Save:
            self.save_category()
        elif reply == QMessageBox.Cancel:
            event.ignore()
            return
        event.accept()

    def save_category(self):
        try:
            with open("./LabelImg/data/predefined_classes.txt", 'w') as f:
                f.write(self.ui.textEdit.toPlainText())
        except:
            QMessageBox.critical(self, "Error", "Cannot save file!")
            return
        QMessageBox.information(self, "Success", "Save success!")

    def show(self) -> None:
        with open("./LabelImg/data/predefined_classes.txt", 'r') as f:
            self.ui.textEdit.setText(f.read())
        self.setWindowModality(Qt.ApplicationModal)
        super().show()


class TrainSettingWindow(QWidget):
    def __init__(self):
        super(TrainSettingWindow, self).__init__()
        self.ui = TrainSettingUI.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("ICON/window.ico"))
        self.ui.btn_select_weight.clicked.connect(self.select_weights)

    def select_weights(self):
        path = QFileDialog.getOpenFileName(
            None, "Please Select 5s/5l/5m/5x.pt",
            '', "Model Files (*.pt)")[0]
        if path:
            self.ui.lineEdit_weight.setText(path)

# redirect stdout to textEdit
class Stream(QtCore.QObject):
    newText = QtCore.pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.ui = MainWindowUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.setWindowIcon(QIcon("ICON/window.ico"))
        self.set_category_window = SetCategoryWindow()
        self.train_setting_window = TrainSettingWindow()
        self.init_event()

        # redirect print output
        sys.stdout = Stream(newText=self.onUpdateText)
        sys.stderr = Stream(newText=self.onUpdateText)

    def onUpdateText(self, text):
        cursor = self.ui.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.ui.textEdit.setTextCursor(cursor)
        self.ui.textEdit.ensureCursorVisible()

    def init_event(self):
        self.ui.btn_set_category.clicked.connect(self.set_category)
        self.ui.btn_select_dataset.clicked.connect(self.select_dataset_path)
        self.ui.btn_openlabelimg.clicked.connect(self.open_labelimg)
        self.ui.btn_split.clicked.connect(self.split_dataset)

        self.ui.btn_select_train_dataset.clicked.connect(self.select_train_path)
        self.ui.btn_select_test_dataset.clicked.connect(self.select_test_path)
        self.ui.btn_select_val_dataset.clicked.connect(self.select_val_path)
        self.ui.btn_select_classes_file.clicked.connect(self.select_classes_file_path)

        self.ui.btn_train.clicked.connect(self.train)
        self.ui.btn_train_setting.clicked.connect(self.train_setting)

    def open_labelimg(self):
        t = threading.Thread(target=os.system("python ./LabelImg/labelImg.py"))
        t.start()

    def train(self):
        opt = Namespace(adam=False, batch_size=4, bucket='', cache_images=False, cfg='', data='data/coco128.yaml',
                        device='', entity=None, epochs=300, evolve=False, exist_ok=False, hyp='data/hyp.scratch.yaml',
                        image_weights=False, img_size=[640, 640], linear_lr=False, local_rank=-1, log_artifacts=False,
                        log_imgs=16, multi_scale=False, name='exp', noautoanchor=False, nosave=False, notest=False,
                        project='runs/train', quad=False, rect=False, resume=False, single_cls=False, sync_bn=False,
                        weights='yolov5s.pt', workers=8)

        if self.train_setting_window.ui.lineEdit_name.text():
            opt.name = self.train_setting_window.ui.lineEdit_name.text()

        # generate data file
        data = {'train': self.ui.le_train_path.text(), 'test': self.ui.le_test_path.text(),
                'val': self.ui.le_val_path.text(), 'names': []}
        with open(self.ui.le_classes_path.text()) as f:
            for line in f:
                data['names'].append(line.rstrip())
        data['nc'] = len(data['names'])

        with open(f'Yolov5Train/data/{opt.name}.yaml', 'w') as f:
            yaml.dump(data, f, sort_keys=False)
        opt.data = f'./Yolov5Train/data/{opt.name}.yaml'

        if self.train_setting_window.ui.lineEdit_weight.text():
            opt.weights = self.train_setting_window.ui.lineEdit_weight.text()
        if self.train_setting_window.ui.lineEdit_epoch.text():
            opt.epochs = self.train_setting_window.ui.lineEdit_epoch.text()
        if self.train_setting_window.ui.lineEdit_batch_size.text():
            opt.batch_size = self.train_setting_window.ui.lineEdit_batch_size.text()
        if self.train_setting_window.ui.lineEdit_img_size.text():
            opt.img_size = self.train_setting_window.ui.lineEdit_img_size.text()
        if self.train_setting_window.ui.lineEdit_device.text():
            opt.device = self.train_setting_window.ui.lineEdit_device.text()

        opt.linear_lr = True if self.train_setting_window.ui.checkBox_linearlr.checkState() else False
        opt.adam = True if self.train_setting_window.ui.checkBox_adam.checkState() else False
        opt.evolve = True if self.train_setting_window.ui.checkBox_evolve.checkState() else False
        opt.noautoanchor = True if self.train_setting_window.ui.checkBox_noautoanchor.checkState() else False
        opt.nosave = True if self.train_setting_window.ui.checkBox_nosave.checkState() else False
        opt.notest = True if self.train_setting_window.ui.checkBox_notest.checkState() else False
        opt.resume = True if self.train_setting_window.ui.checkBox_resume.checkState() else False
        opt.rect = True if self.train_setting_window.ui.checkBox_rect.checkState() else False
        print(opt)
        sys.path.append('Yolov5Train')
        from Yolov5Train import train

        t = threading.Thread(target=train.train_model, args=(opt,))
        t.setDaemon(True)
        t.start()
        # train.train_model(opt)
        # if self.train_setting_window.ui.lineEdit_data

        # os.chdir("./LabelImg")
        # exec(".\LabelImg\labelImg.py")

    def train_setting(self):
        self.train_setting_window.show()

    def select_classes_file_path(self):
        path = QFileDialog.getOpenFileName(
            None, "Please Select classes.txt file",
            self.ui.le_dataset_path.text() if self.ui.le_dataset_path.text() else '',
            "Text Files (classes.txt)")[0]
        if path:
            self.ui.le_classes_path.setText(path)

    def select_train_path(self):
        path = QFileDialog.getOpenFileName(
            None, "Please Select train.txt file",
            self.ui.le_dataset_path.text() if self.ui.le_dataset_path.text() else '',
            "Text Files (train.txt)")[0]
        if path:
            self.ui.le_train_path.setText(path)

    def select_val_path(self):
        path = QFileDialog.getOpenFileName(
            None, "Please Select val.txt file",
            self.ui.le_dataset_path.text() if self.ui.le_dataset_path.text() else '',
            "Text Files (val.txt)")[0]
        if path:
            self.ui.le_val_path.setText(path)

    def select_test_path(self):
        path = QFileDialog.getOpenFileName(
            None, "Please Select test.txt file",
            self.ui.le_dataset_path.text() if self.ui.le_dataset_path.text() else '',
            "Text Files (test.txt)")[0]
        if path:
            self.ui.le_test_path.setText(path)

    def set_category(self):
        if self.set_category_window.isHidden():
            print("show")
            self.set_category_window.show()
        else:
            QMessageBox.critical(self, 'Error',
                                 "Window is already opened.")

    def select_dataset_path(self):
        split_dataset_path = QFileDialog.getExistingDirectory()
        self.ui.le_dataset_path.setText(split_dataset_path)

        files_grabbed = list(itertools.chain.from_iterable(
            [glob.glob(split_dataset_path + e) for e in [r'\*.bmp', r'\*.jpg']]))
        if len(files_grabbed) > 3:  # 最少三张，不然怎么训练嘛
            self.ui.label_dataset_info.setText(f"The dataset contains {len(files_grabbed)} pictures.")
            self.ui.btn_split.setEnabled(True)
        else:
            self.ui.label_dataset_info.setText(f"Picture no found.")
            self.ui.btn_split.setEnabled(False)

    def split_dataset(self):
        dataset_path = self.ui.le_dataset_path.text()
        train_val_percent = self.ui.doubleSpinBox_trainval.value()
        val_percent = self.ui.doubleSpinBox_val.value()
        image_ids = glob.glob(dataset_path + r"/*[jpg,bmp]")

        from sklearn.model_selection import train_test_split
        trainval_files, test_files = train_test_split(image_ids, test_size=1 - train_val_percent, random_state=55)
        train_files, val_files = train_test_split(trainval_files, test_size=val_percent, random_state=55)
        with open(dataset_path + '/test.txt', 'w') as f:
            for i in test_files:
                f.write(i + "\n")
        with open(dataset_path + '/train.txt', 'w') as f:
            for i in train_files:
                f.write(i + "\n")
        with open(dataset_path + '/val.txt', 'w') as f:
            for i in val_files:
                f.write(i + "\n")
        QMessageBox.information(self, "Suceess", "Split dataset sucess!\n"
                                                 "Train/Test/Val/Classes file will save in dataset path.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec_())
