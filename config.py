class Config:
    keyboard = {}
    min_volume = None
    min_hz = None

    def __init__(self):
        self.reading()

    def reading(self):
        with open("config.conf", "r") as f:
            data = "".join(f.read().split())

            data = data.split(";")

            for i in data:
                i = i.split("=")
                if i[0] == "keyboard":
                    pairs = i[1].strip('{}').split(',')
                    for j in pairs:
                        j = j.split(":")
                        self.keyboard.update({int(j[0]): j[1][1:-1]})
                elif i[0] == "min_volume":
                    self.min_volume = int(i[1])
                elif i[0] == "min_hz":
                    self.min_hz = int(i[1])
