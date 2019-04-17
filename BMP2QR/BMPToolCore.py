from BMPToolBeans import *
from BMPToolUtils import *


class BasicBMPInfo:
    global FileCreated
    global BMPImageFile
    global BMPFileName, QRCodeSize, QRCodeType, FileCreated, QRCodeSizeImage, PixelsPerBlock
    BMPFileName = None
    QRCodeSize = 0
    QRCodeType = None
    QRCodeSizeImage = 0
    PixelsPerBlock = 0

    BMPImageFile = None
    FileExists = False

    FileCreated = None

    global BMPFileHeaderClass
    BMPFileHeaderClass = BMPFileHeaderBeans()
    global BMPInfoHeaderClass
    BMPInfoHeaderClass = BMPInfoHeaderBeans()
    global BMPRGBClass
    BMPRGBClass = BMPRGBBeans()
    global BMPGrayClass
    BMPGrayClass = BMPGrayBeans()

    def __init__(self, bmp_file, size, code_type):
        global BMPFileName, QRCodeSize, QRCodeType, FileWriting2BMP
        BMPFileName = bmp_file
        QRCodeSize = size
        QRCodeType = code_type
        print("QRcode size is :")
        print(QRCodeSize,end='')
        print("X",end='')
        print(QRCodeSize)
        print("Init finished")

        return

    def isImageFileExists(self):
        global FileExists, BMPImageFile
        try:
            BMPImageFile = open(BMPFileName, mode="rb+")
        except IOError:
            print("File open failed!")
            BMPImageFile.close()
            return False

            # BMPImageFile.close()

        else:
            BMPFileSymbol = BMPImageFile.read(2)
            if BMPFileSymbol != b'BM':
                print(BMPFileSymbol)
                print("Not a correct Windows BMP file!")
                BMPImageFile.close()
                return False

            else:
                FileExists = True

                BMPImageFile.seek(0, 0)
                print("File exists")

        return

    def readBMPFileHeader(self):
        global BMPImageFile
        try:
            wtype = struct.unpack("<H", BMPImageFile.read(2))[0]
            dwsize = struct.unpack("<L", BMPImageFile.read(4))[0]
            wreserved1 = struct.unpack("<H", BMPImageFile.read(2))[0]
            wreserved2 = struct.unpack("<H", BMPImageFile.read(2))[0]
            dwbitmapfileheader = struct.unpack("<L", BMPImageFile.read(4))[0]

        except IOError:
            print("Not a correct file header!")
            return False
        else:

            BMPFileHeaderClass.set_wType(wtype)
            BMPFileHeaderClass.set_dwSize(dwsize)
            BMPFileHeaderClass.set_wReserved1(wreserved1)
            BMPFileHeaderClass.set_wReserved2(wreserved2)
            BMPFileHeaderClass.set_dwBitMapFileHeader(dwbitmapfileheader)

        print("file header finished")
        return

    def readBMPInfoHeader(self):
        global BMPImageFile
        try:

            dwsize = struct.unpack("<L", BMPImageFile.read(4))[0]
            dwwidth = struct.unpack("<L", BMPImageFile.read(4))[0]
            dwheight = struct.unpack("<L", BMPImageFile.read(4))[0]
            wplanes = struct.unpack("<H", BMPImageFile.read(2))[0]
            wbitcount = struct.unpack("<H", BMPImageFile.read(2))[0]
            dwcompression = struct.unpack("<L", BMPImageFile.read(4))[0]
            dwsizeimage = struct.unpack("<L", BMPImageFile.read(4))[0]
            dwxpixelsperimage = struct.unpack("<L", BMPImageFile.read(4))[0]
            dwypixelsperimage = struct.unpack("<L", BMPImageFile.read(4))[0]
            dwcolorused = struct.unpack("<L", BMPImageFile.read(4))[0]
            dwcolorimportant = struct.unpack("<L", BMPImageFile.read(4))[0]
        except IOError:
            print("Not a correct info header!")
            return False
        else:
            BMPInfoHeaderClass.set_dwSize(dwsize)
            BMPInfoHeaderClass.set_dwWidth(dwwidth)
            BMPInfoHeaderClass.set_dwHeight(dwheight)
            BMPInfoHeaderClass.set_wPlanes(wplanes)
            BMPInfoHeaderClass.set_wBitCount(wbitcount)
            BMPInfoHeaderClass.set_dwCompression(dwcompression)
            BMPInfoHeaderClass.set_dwSizeImage(dwsizeimage)
            BMPInfoHeaderClass.set_dwXPixelsPerMeter(dwxpixelsperimage)
            BMPInfoHeaderClass.set_dwYPixelsPerMeter(dwypixelsperimage)
            BMPInfoHeaderClass.set_dwColorUsed(dwcolorused)
            BMPInfoHeaderClass.set_dwColorImportant(dwcolorimportant)

        print("info header finished")
        return


    def createAnotherFile(self):
        global FileCreated

        try:
            IfFileCreated = open("GeneratedQRCodeFile.bmp", "r")
            if type(IfFileCreated) != False :
                IfFileCreated.close()
                print("Generated QR File creation failed , file already exits?")
                return False
        except FileNotFoundError:
            FileCreated = open("GeneratedQRCodeFile.bmp", "wb+")
            print("Generated QR File created")

        except IOError:
            print("Generated QR File creation failed for IOError!")
            return False

        return

    def writingHeader2QRFile(self):
        global FileCreated, QRCodeSize, BMPInfoHeaderClass, PixelsPerBlock
        if FileCreated == False:
            print("File not created!")
            return False

        PixelsPerBlock = BMPToolUtils.image_quad_pixels_determination(QRCodeSize, BMPInfoHeaderClass.get_dwWidth(),
                                                                      BMPInfoHeaderClass.get_dwHeight())

        print("Pixels per block:")
        print(PixelsPerBlock)

        size_image = BMPToolUtils.size_image_calculation(PixelsPerBlock, QRCodeSize)

        BMPToolUtils.WritingHeader2QRFile(size_image, FileCreated, PixelsPerBlock, QRCodeSize)

        return

    def writingPalette2QRFile(self):
        global FileCreated
        if FileCreated == False:
            return False

        BMPToolUtils.WritingGrayPalette(FileCreated)

        return

    def QRFileAlgorithm(self):
        global BMPImageFile, QRCodeSize, PixelsPerBlock, FileCreated
        if (BMPImageFile == False) | (FileCreated == False):
            print("Algorithm is not executed!")
            return False

        bmp_rgb_class = BMPRGBBeans()

        buffer = []
        count = 0

        temp = 0

        for i in range(0, QRCodeSize * PixelsPerBlock):
            BMPImageFile.seek(i * BMPInfoHeaderClass.get_dwWidth() + 54, 0)

            buffer.append([])

            for j in range(0, QRCodeSize * PixelsPerBlock):
                BMPToolUtils.rgb_quad_read(BMPImageFile, bmp_rgb_class)
                actual_value = BMPToolUtils.rgb2bin_float(bmp_rgb_class)
                buffer[i].append(actual_value)
                count = count + 1
        print(count)

        for i in range(0, QRCodeSize):
            for j in range(0, QRCodeSize):

                for k in range(0, PixelsPerBlock):
                    for l in range(0, PixelsPerBlock):
                        #print(buffer[k + i * PixelsPerBlock][l + j * PixelsPerBlock],end='')
                        temp = temp + buffer[k + i * PixelsPerBlock][l + j * PixelsPerBlock]
                print("temp:",end='')
                print(temp)
                if temp / (PixelsPerBlock * PixelsPerBlock) >= 0.5:
                    for k in range(0, PixelsPerBlock):
                        for l in range(0, PixelsPerBlock):
                            buffer[k + i * PixelsPerBlock][l + j * PixelsPerBlock] = 1
                else:
                    for k in range(0, PixelsPerBlock):
                        for l in range(0, PixelsPerBlock):
                            buffer[k + i * PixelsPerBlock][l + j * PixelsPerBlock] = 0

                temp = 0

        if len(buffer) != (QRCodeSize * PixelsPerBlock):
            print(len(buffer))
            print(QRCodeSize * PixelsPerBlock)
            print("Internal Algorithm error")
            return False

        for i in range(0, QRCodeSize * PixelsPerBlock):
            for j in range(0, QRCodeSize * PixelsPerBlock):
                if(buffer[i][j] == 1):
                    buffer[i][j] = 255
                FileCreated.write(struct.pack("<B", buffer[i][j]))

        FileCreated.flush()
        print("Algorithm finished")
        return

    def closeBMPHeaderPointer(self):
        global BMPImageFile, FileCreated

        BMPImageFile.close()
        FileCreated.close()
        print("image file closed")
        return
