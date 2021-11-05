function showText() {
    // select and reveal text
    const text = document.getElementById('text')
    text.style.display = 'inline'
    //select and hide 'a' tag (hyperlink)
    const aTag = document.getElementById(`more`)
    aTag.style.display = `none`   
}