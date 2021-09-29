function gcd(a,b) {
    a = Math.abs(a);
    b = Math.abs(b);
    if (b > a) {let temp = a; a = b; b = temp;}
    while (true) {
        if (b == 0) {
            console.log(a);
            break;
        }
        a %= b;
        if (a == 0) {
            console.log(b);
            break;
        }
        b %= a;
    }
}

gcd(15, 5)
gcd(2154, 458)