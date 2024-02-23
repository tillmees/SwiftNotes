class TaskColors:
    def __init__(self):
        self.Color1 = f"#b4ded6"
        self.Color2 = f"#8ac6d1"
        self.Color3 = f"#73c6a3"
        self.Color4 = f"#91d35a"
        self.Color5 = f"#f6cf2f"
        self.Color6 = f"#f6ad4b"
        self.Color7 = f"#f88020"
        self.Color8 = f"#d1404d"
        self.Color9 = f"#ffb6b9"
        self.Color10 = f"#fadae4"

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
