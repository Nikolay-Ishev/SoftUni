function constrCrew(worker) {
    if (worker.dizziness) {
        requiredWater = 0.1 * worker.weight * worker.experience;
        worker.levelOfHydrated += requiredWater
        worker.dizziness = false
    }
    return worker
}

console.log(constrCrew({ weight: 80,
    experience: 1,
    levelOfHydrated: 0,
    dizziness: true }))

