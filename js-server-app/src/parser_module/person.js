class Person {
    constructor(name, weight, hobbies) {
        this.name = name;
        this.weight = weight;
        this.hobbies = hobbies;
    }
    greet() {
        return `Hello, my name is ${this.name} and I weigh ${this.weight} kg. and my hobbies are ${this.hobbies.join(', ')}`;
    }
}

export default Person;