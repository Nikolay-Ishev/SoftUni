function validate(obj) {
    const validMethods = [`GET`, `POST`, `DELETE`, `CONNECT`]
    const validVersions = [`HTTP/0.9`, `HTTP/1.0`, `HTTP/1.1`, `HTTP/2.0`]
    let validUri = /^[0-9a-zA-Z\.]+$/
    let validMsg = /([\r\n<>\\&'"]+)/
    if (!obj.method || !validMethods.includes(obj.method)) {
        throw new Error("Invalid request header: Invalid Method")
    }
    if (!obj.uri || !obj.uri.match(validUri)) {
        throw new Error("Invalid request header: Invalid URI")
    }
    if (!obj.version || !validVersions.includes(obj.version)) {
        throw new Error("Invalid request header: Invalid Version")
    }
    if (!obj.hasOwnProperty(`message`) || obj.message.match(validMsg)) {
        throw new Error("Invalid request header: Invalid Message")
    }      
    return obj
}


validate({
    method: 'GET',
    uri: 'svn.public.catalog',
    version: 'HTTP/1.1',
  })