from PyQt5.QtWidgets import QDialog, QLineEdit, QDateTimeEdit, QVBoxLayout, QFormLayout, QDialogButtonBox, QCheckBox


class MyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('My Dialog')

        # Create input boxes
        self.title_edit = QLineEdit()
        self.content_edit = QLineEdit()
        self.datetime_edit = QDateTimeEdit()

        # Create check box to show/hide date/time input box
        self.show_datetime_check_box = QCheckBox('Show Date/Time')
        self.show_datetime_check_box.setChecked(True)
        self.show_datetime_check_box.stateChanged.connect(self.on_show_datetime_state_changed)

        # Create form layout and add input boxes
        form_layout = QFormLayout()
        form_layout.addRow('Title:', self.title_edit)
        form_layout.addRow('Content:', self.content_edit)
        form_layout.addRow(self.show_datetime_check_box)
        self.datetime_row_index = form_layout.rowCount()
        form_layout.addRow('Date/Time:', self.datetime_edit)
        self.datetime_edit.setVisible(True)

        # Create Save and Cancel buttons
        button_box = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        # Create vertical layout and add form layout and button box
        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(button_box)

        # Set layout for QDialog
        self.setLayout(layout)

    def on_show_datetime_state_changed(self, state):
        self.datetime_edit.setVisible(state == Qt.Checked)
        self.layout().itemAt(self.datetime_row_index).widget().setVisible(state == Qt.Checked)