// set the "cart total" element to the correct value
function setCartTotal(cart) {
    let cartTotal = 0
    if (cart !== null) {
        for (const [key, value] of Object.entries(cart)) {
            cartTotal += value['quantity']
        }
    }


    document.getElementById("cart-total").textContent = cartTotal.toString()
}


setCartTotal(cart);
