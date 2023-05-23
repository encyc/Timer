items = [['燕十三', '21', 'Male', '武林大侠'], ['萧十一郎', '21', 'Male', '武功好']]

for i in range(len(items)):
    item = items[i]
    row = self.tableWidget.rowCount()
    self.tableWidget.insertRow(row)
    for j in range(len(item)):
        item = QTableWidgetItem(str(items[i][j]))
        self.tableWidget.setItem(row, j, item)



# 遍历数据，将数据插入到table中
for row in range(rows):
    for column in range(columns):
        # 创建QTableWidgetItem并设置其文本
        item = QTableWidgetItem(str(data[row][column]))
        item.setFlags(item.flags() ^ Qt.ItemIsEditable)  # 设置Item为只读
        table.setItem(row, column, item)

