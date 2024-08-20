// This ia a psudo database
// this will be used for testing purposes to store data on users who register and login to the page
const users = [
  {
    id: 1,
    firstName: "John",
    lastName: "Doe",
    phone: "(999) 999-9999",
    email: "john@test.com",
    password: "1xyzpasswordxyz1",
  },
  {
    id: 2,
    firstName: "Jane",
    lastName: "Doe",
    phone: "(999) 999-9999",
    email: "jane@test.com",
    password: "1xyzpasswordxyz1",
  },
];

function registerUser(user) {
  console.log("registering user", user);
  users.push(user);
}

function getUserByEmail(email) {
  return users.find((user) => user.email === email);
}

function emailTaken(email) {
  if (getUserByEmail(email)) {
    return true;
  }
}

function signInUser(email, password) {
  const user = getUserByEmail(email);
  if (user && user.password === encryptPassword(password)) {
    return user;
  }
  return null;
}

function encryptPassword(password) {
  return `1xyz${password}xyz1`;
}

function decryptPassword(password) {
  return password.replace("1xyz", "").replace("xyz1", "");
}

function createUser(firstName, lastName, phone, email, password) {
  return {
    id: users.length + 1,
    firstName,
    lastName,
    phone,
    email,
    password: encryptPassword(password),
  };
}


// This will be used for user reservations booking rooms

