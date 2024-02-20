def update_combo_box(combo_box_obj, string):
    index = combo_box_obj.findText(string)
    if index != -1:
        # a project with that name already exists
        return
    combo_box_obj.addItems([string])
    index = combo_box_obj.findText(string)
    combo_box_obj.setCurrentIndex(index)
    combo_box_obj.model().sort(0)


def add_string_to_combo_box(combo_box_obj, string):
    index = combo_box_obj.findText(string)
    if index != -1:
        # a project with that name already exists
        return
    combo_box_obj.addItems([string])
    combo_box_obj.model().sort(0)


def add_whitespace_string_to_combo_box(combo_box_obj):
    combo_box_obj.addItems([" "])
    index = combo_box_obj.findText(" ")
    combo_box_obj.setCurrentIndex(index)
    combo_box_obj.model().sort(0)


def delete_whitespace_string_from_combo_box(combo_box_obj):
    index = combo_box_obj.findText(" ")
    if index != -1:
        combo_box_obj.removeItem(index)


def delete_string_from_combo_box(combo_box_obj, string):
    index = combo_box_obj.findText(string)
    if index != -1:
        combo_box_obj.removeItem(index)


def get_current_project(combo_box_obj):
    return combo_box_obj.currentText()
