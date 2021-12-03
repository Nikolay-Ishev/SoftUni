function getPersons() {
    class Person {
        constructor(fName, lName, age, email) {
            this.firstName = fName;
            this.lastName = lName;
            this.age = age;
            this.email = email;
        }
        toString() {
            return `${this.firstName} ${this.lastName} (age: ${this.age}, email: ${this.email})`
        }
    }

    const guy1 = new Person(`Anna`, `Simpson`, 22, `anna@yahoo.com`)
    const guy2 = new Person(`SoftUni`)
    const guy3 = new Person(`Stephan`, `Johnson`, 25)
    const guy4 = new Person(`Gabriel`, `Peterson`, 24, `g.p@gmail.com`)

    return [guy1, guy2, guy3, guy4]
}