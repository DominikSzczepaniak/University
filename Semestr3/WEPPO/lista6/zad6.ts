type User = {
    name: string;
    age: number;
    occupation: string;
    type: 'user';
}
type Admin = {
    name: string;
    age: number;
    role: string;
    type: 'admin';
}
export type Person = User | Admin;

export const persons: Person[] = [
    {
        name: 'Jan Kowalski',
        age: 17,
        occupation: 'Student',
        type: 'user'
    },
    {
        name: 'Tomasz Malinowski',
        age: 20,
        role: 'Administrator',
        type: 'admin'
    }
];

export function isAdmin(person: Person) {
    return person.type === 'admin';
}
export function isUser(person: Person) {
    return person.type === 'user';
}
export function logPerson(person: Person) {
    let additionalInformation: string = '';
    if (isAdmin(person)) {
        additionalInformation = (person as Admin).role;
    }
    if (isUser(person)) {
        additionalInformation = (person as User).occupation;
    }
    console.log(person.name, person.age, additionalInformation);
}

logPerson(persons[0])
