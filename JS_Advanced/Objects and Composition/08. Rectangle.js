function rectangle(width, height, colour) {
    const color = colour.charAt(0).toUpperCase() + colour.slice(1)
    return {
        width,
        height,
        color,
        calcArea() {
            return this.height * this.width
        }
    }
}




let rect = rectangle(4, 5, 'red');
console.log(rect.width);
console.log(rect.height);
console.log(rect.color);
console.log(rect.calcArea());