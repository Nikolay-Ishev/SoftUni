function fromJSONToHTMLTable(json) {
 
    let arr = JSON.parse(json);
 
    let outputArr = ["<table>"];
    outputArr.push(makeKeyRow(arr));
    arr.forEach(obj => outputArr.push(makeValueRow(obj)));
    outputArr.push("</table>");
 
    console.log(outputArr.join('\n'));
 
 
    function makeKeyRow(arr) {
        let keys = []
        for (let key in arr[0]) {
            keys.push(`<th>${escapeHtml(key)}</th>`)
        };
        result =  `    <tr>` + keys.join("") + `</tr>`
        return result
    }

    function makeValueRow(obj) {
        let values = [];
        for (let key in obj) {
            let value = String(obj[key])
            values.push(`<td>${escapeHtml(value)}</td>`)
        };
        result = `    <tr>` + values.join("") + `</tr>`;
        return result
    }
 
    function escapeHtml(str) {
        // html escape from Underscore.js https://coderwall.com/p/ostduq/escape-html-with-javascript
        let entityMap = {
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': '&quot;',
            "'": '&#39;',
        };
        return str.replace(/[&<>"']/g, (s) => entityMap[s]);
    }
}


fromJSONToHTMLTable(`[{"Name":"Stamat",
"Score":5.5},
{"Name":"Rumen",
"Score":6}]`)




// whole function below (not working for this exersize because / should not be escaped in order to get the correct answer)

// function escapeHtml(str) {
//     // html escape from Underscore.js https://coderwall.com/p/ostduq/escape-html-with-javascript
//     let entityMap = {
//         "&": "&amp;",
//         "<": "&lt;",
//         ">": "&gt;",
//         '"': '&quot;',
//         "'": '&#39;',
//         "/": '&#x2F;'
//     };
//     return str.replace(/[&<>"'\/]/g, (s) => entityMap[s]);
// }