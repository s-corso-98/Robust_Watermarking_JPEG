import argparse
import decompression as decompression
import image_block_permutation as img_permutation
import image_encrypt as img_encrypt
import watermarking as watermark
import numpy as np

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="path to the input image")
    parser.add_argument("output", help="path to the output image")
    parser.add_argument("swap_encrypted_array", help="path to the encrypted array")
    parser.add_argument("watermarking_blocks", help="path to the watermarking's blocks")
    parser.add_argument("key_permutation", help="path to the input image")
    parser.add_argument("key_cypher", help="path to the input image")
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output
    array_encrypt_file = args.swap_encrypted_array
    watermarking_blocks_file = args.watermarking_blocks
    key_permutation = args.key_permutation
    key_cipher = args.key_cypher



    ######################################  D E C O M P R E S S I O N  #################################################
    print("I'm doing the decompression...")
    image_decompression , dc_Y_mod = decompression.decompression(input_file)



    #########################################  D E C R Y P T I O N  ####################################################
    print("I'm decrypting...")
    array_encrypt = np.load(array_encrypt_file)
    image_decrypt = img_encrypt.deCryption(image_decompression, key_cipher, array_encrypt)



    ####################################  E X T R A C T   W A T E R M A R K  ###########################################
    print("I'm extracting the watermark...")
    watermarking_blocks = np.load(watermarking_blocks_file)
    watermark.extractWatermark(dc_Y_mod, watermarking_blocks)



    #######################################  D E P E R M U T A T I O N  ################################################
    print("I'm depermuting...")
    image_depermutation = img_permutation.dePermutation(image_decrypt, 16, key_permutation, output_file)



if __name__ == "__main__":
    main()