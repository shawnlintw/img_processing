# OpenCV Video Writer on Mac OS X

# Fourcc tests:

- x : not worked
- o: worked (able to open in quicktime but need conversion)
- oo: worked well (preview worked but wrong aspect ratio)
- ooo: worked very well (preview worked, and aspect ratio’s right)

(Codecs are extracted from https://web.archive.org/web/20120722124832/http://opencv.willowgarage.com/wiki/QuickTimeCodecs )

FourCC | Result | Codec Name | Description |
-------|--------|------------|-------------|
‘3IV2'| x | 3ivx D4 4.5.1 | Compresses an image into 3ivx D4 format.
‘8BPS' | o  | Apple Planar RGB | Compresses images in the Planar RGB format.
‘SVQ1' | o | Sorenson Video™ Compressor | Compresses video using the Sorenson Video™  V2.30.302 compressor from Sorenson™ Media, Inc.
‘SVQ3' | o | Sorenson Video 3 Compressor | Compresses video using the Sorenson Video® 3 SE V 3.3.302 compressor from Sorenson® Media, Inc.
‘WRLE' | o | Apple BMP | Compresses images in the BMP format.
‘XVID' | x | XviD | Decompresses video stored in XviD format.
‘avc1' | ooo | H.264 Encoder | Compresses video to the H.264 format.
‘cvid' | o | Apple Cinepak | Compresses images using Apple Computer's Cinepak compression algorithm
‘dv5n' | oo | Apple DVCPRO50 - NTSC | Compresses an image to DVCPRO50 NTSC format.
‘dv5p' | oo | Apple DVCPRO50 - PAL | Compresses an image to DVCPRO50 PAL format.
'dvc ‘ | oo | Apple DV/DVCPRO - NTSC | Compresses an image to DV/DVCPRO NTSC format.
‘dvcp' | oo | Apple DV - PAL | Compresses an image to DV PAL format.
‘dvpp' | oo | Apple DVCPRO - PAL | Compresses an image to DVCPRO PAL format.
‘h261’ | o (but small) | Apple H.261 | Compresses images using H.261 compression algorithm
‘h263’ | ooo (but small) | H.263 | Compresses images using H.263 compression algorithm
‘jpeg' | ooo | Apple Photo - JPEG | Compresses images using the ISO standard baseline JPEG algorithm
‘mjp2' | o | JPEG 2000 Encoder | Compresses images to the JPEG 2000 JP2 format.
‘mjpa' | o | Apple Motion JPEG A | Compresses images compressed using Motion JPEG Format A
‘mjpb' | o | Apple Motion JPEG B | Compresses images compressed using Motion JPEG Format B
‘mp4v' | ooo | Apple MPEG4 Compressor | Compresses images using MPEG4 compression algorithm
'png ‘ | o | Apple PNG | Compresses images in the PNG format.
‘pxlt' | o | Apple Pixlet Video | Apple Pixlet Video Info
'raw ‘ | ooo (but preview didn’t work) | Apple None | Stores images without any compression
'rle ‘ | o | Apple Animation | Compresses images using run length encoding
‘rpza' | o | Apple Video | Compresses images using Apple Computer's Video compression algorithm
'smc ‘ | x | Apple Graphics | Compresses images using Sean's secret recipe (optimal for 8-bit dithered images)
'tga ‘ | o | Apple TGA | Compresses images stored into the TGA format.
‘tiff' | o | Apple TIFF | Compresses images in the TIFF format.
‘yuv2' | o | Apple Component Video - YUV422 | Compresses an image into YUV format.

# Conclusion

Use **'mp4v'** or **'avc1'**