import struct
import time
from BMPToolBeans import *


class BMPToolUtils:
    @staticmethod
    def rgb_quad_read(BMPImageFile, BMPRGBBeans):
        BMPRGBBeans.set_byteBlue(struct.unpack("<B", BMPImageFile.read(1))[0])
        BMPRGBBeans.set_byteGreen(struct.unpack("<B", BMPImageFile.read(1))[0])
        BMPRGBBeans.set_byteRed(struct.unpack("<B", BMPImageFile.read(1))[0])
        return

    @staticmethod
    def rgb2gray_float(BMPRGBBeans):

        iblue = BMPRGBBeans.get_byteBlue()
        igreen = BMPRGBBeans.get_byteGreen()
        ired = BMPRGBBeans.get_byteRed()

        igray = iblue * 0.11 + igreen * 0.59 + ired * 0.3

        return igray

    @staticmethod
    def rgb2gray_average(BMPRGBBeans):

        iblue = BMPRGBBeans.get_byteBlue()
        igreen = BMPRGBBeans.get_byteGreen()
        ired = BMPRGBBeans.get_byteRed()

        igray = (iblue + igreen + ired) // 3

        return igray

    @staticmethod
    def rgb2gray_green_only(BMPRGBBeans):

        return BMPRGBBeans.get_byteGreen()

##############################################################################################################
##灰度图转二值图时因为规则上讲要从一个颜色占用一个字节变为一个颜色占用一个比特，操作难度有些上升，所以我决定沿用一个颜色占用一个字节##
##############################################################################################################
    @staticmethod
    def gray2bin(igray):

        if igray < 128:
            bytegray = 0
        else:
            bytegray = 1

        return bytegray

    @staticmethod
    def rgb2bin_float(BMPRGBBeans):

        iblue = BMPRGBBeans.get_byteBlue()
        igreen = BMPRGBBeans.get_byteGreen()
        ired = BMPRGBBeans.get_byteRed()

        floatgray = iblue * 0.11 + igreen * 0.59 + ired * 0.3

        if floatgray < 128:
            bytegray = 0 #black
        else:
            bytegray = 1 #white

        return bytegray

    @staticmethod
    def rgb2bin_average(BMPRGBBeans):

        iblue = BMPRGBBeans.get_byteBlue()
        igreen = BMPRGBBeans.get_byteGreen()
        ired = BMPRGBBeans.get_byteRed()

        igray = (iblue + igreen + ired) // 3

        if igray < 128:
            bytegray = 0#black
        else:
            bytegray = 1#white

        return bytegray

    @staticmethod
    def rgb2bin_green_only(BMPRGBBeans):

        igray = BMPRGBBeans.get_byteGreen()

        if igray < 128:
            bytegray = 0
        else:
            bytegray = 1

        return bytegray

    @staticmethod
    def image_quad_pixels_determination(qr_code_size, image_width, image_height):
        if image_height >= image_width:
            min_length = image_width
        else:
            min_length = image_height

        pixels_per_block = min_length // qr_code_size

        return pixels_per_block

    @staticmethod
    def size_image_calculation(pixels_per_block, qr_code_size):

        return (pixels_per_block * pixels_per_block * qr_code_size * qr_code_size)

    @staticmethod
    def WritingGrayPalette(FileCreated):

        for i in range(0, 256):
            FileCreated.write(struct.pack("<B", i))  # B
            FileCreated.write(struct.pack("<B", i))  # G
            FileCreated.write(struct.pack("<B", i))  # R
            FileCreated.write(struct.pack("<B", 0))  # A
            FileCreated.flush()
        return

    @staticmethod
    def WritingHeader2QRFile(size_image, FileCreated, pixels_per_block, qr_code_size):

        FileCreated.write(struct.pack("<B", 66)) #B
        FileCreated.write(struct.pack("<B", 77)) #M
        FileCreated.write(struct.pack("<L", (size_image + 54 + 1024))) #dwSize
        FileCreated.write(struct.pack("<H", 0))#wReserved1
        FileCreated.write(struct.pack("<H", 0))#wReserved2
        FileCreated.write(struct.pack("<L", 54 + 1024))#dwBitMapFileHeader

        FileCreated.write(struct.pack("<L", 40))#dwSize
        FileCreated.write(struct.pack("<L", (pixels_per_block * qr_code_size)))#dwWidth
        FileCreated.write(struct.pack("<L", (pixels_per_block * qr_code_size)))#dwHeight
        FileCreated.write(struct.pack("<H", 1))#wPlanes
        FileCreated.write(struct.pack("<H", 8))#wBitCount
        FileCreated.write(struct.pack("<L", 0))#dwCompression
        FileCreated.write(struct.pack("<L", 0))#dwSizeImage
        FileCreated.write(struct.pack("<L", 2835))#dwXPixelsPerMeter 0x0B13
        FileCreated.write(struct.pack("<L", 2835))#dwYPixelsPerMeter 0x0B13
        FileCreated.write(struct.pack("<L", 0))#dwColorUsed
        FileCreated.write(struct.pack("<L", 0))#dwColorImportant

        return
