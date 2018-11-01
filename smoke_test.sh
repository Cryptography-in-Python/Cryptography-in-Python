cd ..

function DES(){
    python3 -m cryptography.DES.cryptography_des
    return $?
}

function RSA(){
    # python3 -m cryptography.RSA.cryptography_rsa
    return 1
}

DES
DES_ret_val=$?
RSA
RSA_ret_val=$?

exit $(($DES_ret_val  | $RSA_ret_val))
