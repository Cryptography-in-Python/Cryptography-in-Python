function DES(){
    python3 -m cryptography.DES.cryptography_des
    return $?
}

function RSA(){
    # python3 -m cryptography.RSA.cryptography_rsa
    return 0
}

function MD5(){
    # python3 -m cryptography.MD5.cryptography_md5
    return 0
}

DES
DES_ret_val=$?
RSA
RSA_ret_val=$?
MD5
MD5_ret_val=$?

exit $(($DES_ret_val | $RSA_ret_val | $MD5_ret_val))
