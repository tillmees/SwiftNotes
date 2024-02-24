class TaskColors:
    def __init__(self):
        self.Color1 = f"#799558"
        self.Color2 = f"#b0bf84"
        self.Color3 = f"#e17e44"
        self.Color4 = f"#f69d59"
        self.Color5 = f"#e8b449"
        self.Color6 = f"#d2838f"
        self.Color7 = f"#ae445a"
        self.Color8 = f"#732e54"
        self.Color9 = f"#216869"
        self.Color10 = f"#75a09b"

        self.color_mapping = {
            1: self.Color1,
            2: self.Color2,
            3: self.Color3,
            4: self.Color4,
            5: self.Color5,
            6: self.Color6,
            7: self.Color7,
            8: self.Color8,
            9: self.Color9,
            10: self.Color10,
        }

    def get_color_id_by_string(self, string):
        for key, val in self.color_mapping.items():
            if val == string:
                return key
        return None
