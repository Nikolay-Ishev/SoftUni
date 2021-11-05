function editElement(el, match, replacer) {    
    const text = el.textContent;
    const matcher = new RegExp(match, `g`);
    el.textContent = text.replace(matcher, replacer)
    //el.textContent = text.replaceAll(match, replacer);
    //el.textContent = text.split(match).join(replacer)
}