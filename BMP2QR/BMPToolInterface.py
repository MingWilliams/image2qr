from BMPToolCore import *


class BMPTool:

    def __init__(self, bmp_file_name, qr_code_type, qr_code_size):

        BMPToolCoreClass = BasicBMPInfo(bmp_file_name, qr_code_size, qr_code_type)

        if BMPToolCoreClass.isImageFileExists() == False:
            print("error exiting...")
            return
        if BMPToolCoreClass.readBMPFileHeader() == False:
            print("error exiting...")
            return
        if BMPToolCoreClass.readBMPInfoHeader() == False:
            print("error exiting...")
            return
        if BMPToolCoreClass.createAnotherFile() == False:
            print("error exiting...")
            return
        if BMPToolCoreClass.writingHeader2QRFile() == False:
            print("error exiting...")
            return
        if BMPToolCoreClass.writingPalette2QRFile() == False:
            print("error exiting...")
            return
        if BMPToolCoreClass.QRFileAlgorithm() == False:
            print("error exiting...")
            return
        BMPToolCoreClass.closeBMPHeaderPointer()

        return
