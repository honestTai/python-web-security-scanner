#!/usr/bin/env python3

import base64
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA

class Rsa_Crypto():  
    def __init__(self):
        self.rsa_private_key = """CHANGE_ME_BEFORE_RUNNING
        """

        self.rsa_public_key = """-----BEGIN PUBLIC KEY-----
        MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC+UHO/FX+mqq68COGYqk82/3xw
        7vfhNJIM58lrjI0T+zXIx6AsaNgrelM7Z+raDIRDJvdObz6qVbJ5L1IhcreeZWUm
        EtmOetqtkF4i/rhthVFmSDAKyZi8a6/SulpU8bHEsi2M3gyp25pi7R68GzcAmm1y
        KCusOaABFa4M7vuC8wIDAQAB
        -----END PUBLIC KEY-----
        """


    def encrypt(self, content):
        """
        进行rsa加密

        :param str content: 待加密字符串
        :return: str result: 加密后的字符串
        """
        content = content.encode('utf-8')
        length = len(content)
        default_length = 117
        # 公钥加密
        pubobj = Cipher_pkcs1_v1_5.new(RSA.importKey(self.rsa_public_key))
        # 长度不用分段
        if length < default_length:
            return base64.b64encode(pubobj.encrypt(content)).decode('utf-8')
        # 需要分段
        offset = 0
        res = []
        while length - offset > 0:
            if length - offset > default_length:
                res.append(pubobj.encrypt(content[offset:offset + default_length]))
            else:
                res.append(pubobj.encrypt(content[offset:]))
            offset += default_length
        byte_data = b''.join(res)
        result = base64.b64encode(byte_data).decode('utf-8')
        return result

    def decrypt(self, content):
        
        """
        进行rsa解密

        :param str content: 待解密字符串
        :return: str result: 解密后的字符串
        """
        
        content = base64.b64decode(content)
        length = len(content)
        default_length = 128
        # 私钥解密
        priobj = Cipher_pkcs1_v1_5.new(RSA.importKey(self.rsa_private_key))
        # 长度不用分段
        if length < default_length:
            return b''.join(priobj.decrypt(content, b'xyz')).decode('utf8')
        # 需要分段
        offset = 0
        res = []
        while length - offset > 0:
            if length - offset > default_length:
                res.append(priobj.decrypt(content[offset:offset + default_length], b'xyz'))
            else:
                res.append(priobj.decrypt(content[offset:], b'xyz'))
            offset += default_length
        result = b''.join(res).decode('utf8')
        return result

if __name__ == '__main__':
    crypto = Rsa_Crypto()
    data = 'd34sdg'
    encrypt = crypto.encrypt(data)
    decrypt = crypto.decrypt(encrypt)
    print(encrypt)
    print(decrypt)




