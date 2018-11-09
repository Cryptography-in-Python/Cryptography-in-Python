function DES(){
    # python3 -m cryptography.DES.cryptography_des
    return 0
}

function RSA(){
    python3 -m cryptography.RSA.cryptography_rsa
    return $?
}

function MD5(){
    # python3 -m cryptography.MD5.cryptography_md5
    return 0
}

function unittest(){
    python3 -m cryptography.test.cryptography_test
    return $?
}

DES
DES_ret_val=$?
RSA
RSA_ret_val=$?
MD5
MD5_ret_val=$?
unittest
unittest_ret_val=$?

exit $(($DES_ret_val | $RSA_ret_val | $MD5_ret_val | $unittest_ret_val))
