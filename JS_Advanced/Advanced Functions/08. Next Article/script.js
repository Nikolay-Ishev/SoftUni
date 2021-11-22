function getArticleGenerator(articles) {
    let articlesArr = articles
    let inputBox = document.getElementById("content")
    function display() {
        if (articlesArr.length > 0) {
            const article = articlesArr.shift()
            var x = document.createElement("ARTICLE")
            x.textContent = article
            inputBox.appendChild(x)
        }
    }
    return display
}
