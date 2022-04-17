let updateBtns = document.getElementsByClassName('update-cart')


for (let i=0; i < updateBtns.length;i++) {
    updateBtns[i].addEventListener('click', function (){
        let action = this.dataset.action
        let productId = this.dataset.product
        let inStock = this.dataset.type

        if (user === 'AnonymousUser') {
            updateAnonymousOrder(productId, inStock, action)
        } else {
            updateUserOrder(productId, action)
        }
    })
}

function updateAnonymousOrder(productId, inStock, action) {
    console.log('Not logged in..')

    if (action === 'add' && inStock !== 'Sold') {
        if (cart[productId] === undefined) {
            cart[productId] = {'quantity': 0}
        }
        if (inStock === 'Unique') {
            cart[productId]['quantity'] = 1
        }
        else {cart[productId]['quantity'] += 1}
    }
    else if (action === 'remove') {
        cart[productId]['quantity'] -= 1
        if (cart[productId]['quantity'] <=0) {
            delete cart[productId]
        }
    }
    setCookie('cart', cart, 864000)
    setCartTotal(cart)
    console.log(cart)

    //check if the location is cart and reloads it in order to update the DOM, temporary solution
    if (location.href === "http://127.0.0.1:8000/cart/") {
        location.reload()
    }
}

// accepts productId and action and then create async POST request
// sending the data to the view "update_item"
function updateUserOrder(productId, action) {
    const csrftoken = getCookie('csrftoken');
    console.log('User is logged in, sending data...')

    let url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            "X-CSRFToken": csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })
        .then((response) =>{
        return response.json()
    })
       .then((data) =>{
        console.log('data', data)
           // reloading the page in order to update cart total, temporary solution
           location.reload()
    })
}