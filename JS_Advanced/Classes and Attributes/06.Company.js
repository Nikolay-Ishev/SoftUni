class Company {
    constructor() {
        this.departments = {}
    }

    addEmployee(eName, eSalary, ePosition, eDepartment) {
        if (!eName || !eSalary || !ePosition || !eDepartment || eSalary < 0) {
            throw new Error("Invalid input!")
        }
        if (!this.departments[eDepartment]) {
            this.departments[eDepartment] = []
        }

        let e = {name: eName, salary: parseFloat(eSalary), position: ePosition}
        this.departments[eDepartment].push(e)
        return `New employee is hired. Name: ${eName}. Position: ${ePosition}`
    }

    bestDepartment() {
        let bestDepartment = {name: undefined, avSalary: 0}
        for (const [key, value] of Object.entries(this.departments)) {
            let totalSalary = 0
            for (let e of value) {
                totalSalary += e.salary
            }
            let currentAvSalary = totalSalary / value.length
            if (currentAvSalary > bestDepartment.avSalary) {
                bestDepartment.name = key
                bestDepartment.avSalary = currentAvSalary
            }
        }
        const result = []
        result.push(`Best Department is: ${bestDepartment.name}`)
        result.push(`Average salary: ${bestDepartment.avSalary.toFixed(2)}`)
        
        this.departments[bestDepartment.name].sort(function (w1, w2) {
            if (w1.salary > w2.salary) return -1;
            else if (w1.salary < w2.salary) return 1;
            else return w1.name.localeCompare(w2.name)
        })

        for (let e of this.departments[bestDepartment.name]) {
            result.push(`${e.name} ${e.salary} ${e.position}`)
        }
        return result.join(`\n`)
    }
}

let c = new Company();
c.addEmployee("Stanimir", 2000, "engineer", "Construction");
c.addEmployee("Pesho", 1500, "electrical engineer", "Construction");
c.addEmployee("Slavi", 500, "dyer", "Construction");
c.addEmployee("Stan", 2000, "architect", "Construction");
c.addEmployee("Stanimir", 1200, "digital marketing manager", "Marketing");
c.addEmployee("Pesho", 1000, "graphical designer", "Marketing");
c.addEmployee("Gosho", 1350, "HR", "Human resources");
console.log(c.bestDepartment());