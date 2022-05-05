function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        // split cookie string and get all individual name-value pairs in an array
        const cookies = document.cookie.split(';');

        //loop through the array elements
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                //decode the cookie value
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


// creates or overwrite a cookie
// 1 Day = 24 Hrs = 24*60*60 = 86400.
// setting age to 0 will DELETE the cookie
function setCookie(name, value) {
    document.cookie = `${name}=` + JSON.stringify(value) + ";path=/;"
}

let cart = JSON.parse(getCookie('cart'))

if (cart === null) {
    cart = {}
    setCookie('cart', cart)
    console.log('Cart was created...')
}


let footer = document.querySelector('footer')
console.log(footer)




