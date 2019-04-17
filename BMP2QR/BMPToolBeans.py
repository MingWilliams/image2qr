class BMPFileHeaderBeans:

    global BMPFileHeader
    BMPFileHeader = {"wType": None, "dwSize": None, "wReserved1": None, "wReserved2": None, "dwBitMapFileHeader": None}

    def get_file_header(self):
        global BMPFileHeader

        return BMPFileHeader

    def set_file_header(self, file_header):
        global BMPFileHeader

        BMPFileHeader = file_header

        return

    def set_wType(self, b):
        BMPFileHeader["wType"] = b
        return

    def get_wType(self):
        return BMPFileHeader["wType"]

    def set_dwSize(self, b):
        BMPFileHeader["dwSize"] = b
        return

    def get_dwSize(self):
        return BMPFileHeader["dwSize"]

    def set_wReserved1(self, b):
        BMPFileHeader["wReserved1"] = b
        return

    def get_wReserved1(self):
        return BMPFileHeader["wReserved1"]

    def set_wReserved2(self, b):
        BMPFileHeader["wReserved2"] = b
        return

    def get_wReserved2(self):
        return BMPFileHeader["wReserved2"]

    def set_dwBitMapFileHeader(self, b):
        BMPFileHeader["dwBitMapFileHeader"] = b
        return

    def get_dwBitMapFileHeader(self):
        return BMPFileHeader["dwBitMapFileHeader"]


class BMPInfoHeaderBeans:

    global BMPInfoHeader

    BMPInfoHeader = {"dwSize": None, "dwWidth": None, "dwHeight": None, "wPlanes": None, "wBitCount": None,
                     "dwCompression": None, "dwSizeImage": None, "dwXPixelsPerMeter": None, "dwYPixelsPerMeter": None,
                     "dwColorUsed": None, "dwColorImportant": None}
#BMPInfoHeader
    def get_info_header(self):
        global BMPInfoHeader

        return BMPInfoHeader

    def set_info_header(self, info_header):
        global BMPInfoHeader

        BMPInfoHeader = info_header
        return
#dwSize
    def set_dwSize(self, b):
        BMPInfoHeader["dwSize"] = b
        return

    def get_dwSize(self):
        return BMPInfoHeader["dwSize"]
#dwWidth
    def set_dwWidth(self, b):
        BMPInfoHeader["dwWidth"] = b
        return

    def get_dwWidth(self):
        return BMPInfoHeader["dwWidth"]
#dwHeight
    def set_dwHeight(self, b):
        BMPInfoHeader["dwHeight"] = b
        return

    def get_dwHeight(self):
        return BMPInfoHeader["dwHeight"]
#wPlanes
    def set_wPlanes(self, b):
        BMPInfoHeader["wPlanes"] = b
        return

    def get_wPlanes(self):
        return BMPInfoHeader["wPlanes"]
#wBitCount
    def set_wBitCount(self, b):
        BMPInfoHeader["wBitCount"] = b
        return

    def get_wBitCount(self):
        return BMPInfoHeader["wBitCount"]
#dwCompression
    def set_dwCompression(self, b):
        BMPInfoHeader["dwCompression"] = b
        return

    def get_dwCompression(self):
        return BMPInfoHeader["dwCompression"]
#dwSizeImage
    def set_dwSizeImage(self, b):
        BMPInfoHeader["dwSizeImage"] = b
        return

    def get_dwSizeImage(self):
        return BMPInfoHeader["dwSizeImage"]
#dwXPixelsPerMeter
    def set_dwXPixelsPerMeter(self, b):
        BMPInfoHeader["dwXPixelsPerMeter"] = b
        return

    def get_dwXPixelsPerMeter(self):
        return BMPInfoHeader["dwXPixelsPerMeter"]
#dwYPixelsPerMeter
    def set_dwYPixelsPerMeter(self, b):
        BMPInfoHeader["dwYPixelsPerMeter"] = b
        return

    def get_dwYPixelsPerMeter(self):
        return BMPInfoHeader["dwYPixelsPerMeter"]
#dwColorUsed
    def set_dwColorUsed(self, b):
        BMPInfoHeader["dwColorUsed"] = b
        return

    def get_dwColorUsed(self):
        return BMPInfoHeader["dwColorUsed"]
#dwColorImportant
    def set_dwColorImportant(self, b):
        BMPInfoHeader["dwColorImportant"] = b
        return

    def get_dwColorImportant(self):
        return BMPInfoHeader["dwColorImportant"]


class BMPRGBBeans:

    global Full24BitRGBQuad
    Full24BitRGBQuad = {"byteBlue": None, "byteGreen": None, "byteRed": None}

    def set_rgb_quad(self, rgbquad):
        global Full24BitRGBQuad
        Full24BitRGBQuad = rgbquad

        return

    def get_rgb_quad(self):
        global Full24BitRGBQuad

        return Full24BitRGBQuad
#byteBlue
    def set_byteBlue(self, b):
        Full24BitRGBQuad["byteBlue"] = b
        return Full24BitRGBQuad["byteBlue"]

    def get_byteBlue(self):
        return Full24BitRGBQuad["byteBlue"]
#byteGreen
    def set_byteGreen(self, b):
        Full24BitRGBQuad["byteGreen"] = b
        return Full24BitRGBQuad["byteGreen"]

    def get_byteGreen(self):
        return Full24BitRGBQuad["byteGreen"]
#byteRed
    def set_byteRed(self, b):
        Full24BitRGBQuad["byteRed"] = b
        return Full24BitRGBQuad["byteRed"]

    def get_byteRed(self):
        return Full24BitRGBQuad["byteRed"]


class BMPGrayBeans:

    global Full8bitGrayByte
    Full8bitGrayByte = 0

    def get_gray_byte(self):
        global Full8BitGrayByte

        return Full8BitGrayByte

    def set_gray_byte(self, gray_byte):
        global Full8BitGrayByte

        Full8BitGrayByte = gray_byte

        return

