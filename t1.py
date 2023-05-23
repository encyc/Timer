
class NoteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Note")

        self.title_label = QLabel("Title:")
        self.title_edit = QLineEdit()
        self.content_label = QLabel("Content:")
        self.content_edit = QPlainTextEdit()
        self.save_button = QPushButton("Save")
        self.cancel_button = QPushButton("Cancel")

        layout = QVBoxLayout(self)
        layout.addWidget(self.title_label)
        layout.addWidget(self.title_edit)
        layout.addWidget(self.content_label)
        layout.addWidget(self.content_edit)
        layout.addWidget(self.save_button)
        layout.addWidget(self.cancel_button)

        self.save_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        self.nm = NoteManager()

    def get_note(self):
        title_edit = self.title_edit.text()
        content_edit = self.content_edit.toPlainText()
        # note = {'title:' self.title_edit, 'content':self.content_edit}
        # set_title(self.title_edit.text())
        # set_content(self.content_edit.toPlainText())
        return title_edit, content_edit

