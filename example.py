from base.encoder import Encoder
from algorithms.tucker import TuckerDecoder, TuckerEncoder, TuckerTdv
from base.config import Config
from base.util import calculate_psnr, claculate_compression_ratio


# initialize stateless encoder and decoder
conf = Config()
conf.set("ranks", [20, 20, 50, 3])
coder = TuckerEncoder(conf)
decoder = TuckerDecoder(conf)

# encode a file
tdv = coder.encode_file("file_example_MP4_480_1_5MG.mp4")

tdv.persist("compressed_video.tdv")
decoder.decode_to_file(tdv, "output.mp4")


# load again from file
tdv_loaded = TuckerTdv.load("compressed_video.tdv")
decoder.decode_to_file(tdv_loaded, "output_loaded.mp4")


# calculate psnr
psnr = calculate_psnr("file_example_MP4_480_1_5MG.mp4", "output.mp4")
ratio = claculate_compression_ratio(
    "file_example_MP4_480_1_5MG.mp4", "output.mp4")
print(psnr, ratio)
