function extract(content) {
    let el = document.getElementById(content).textContent;
    
    const pattern = /\((.+?)\)/g;
    const result = []
    let match = pattern.exec(el)
    while (match != null) {
        result.push(match[1]);
        match = pattern.exec(el);
    }
    console.log(result.join("; "))
    return result.join("; ")
}