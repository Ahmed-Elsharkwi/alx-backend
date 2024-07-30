import { createClient } from 'redis';
import redis from 'redis'

const client = createClient();
client.on('error', (err) => console.log('Redis Client Error', err));
client.connect();
console.log('Redis client connected to the server')

const setNewSchool = async (schoolName, value) => {
   await client.set(schoolName, value);
}

const displaySchoolValue = async (schoolName) => {
  let value = await client.get(schoolName);
  console.log(value)
}
displaySchoolValue('Holberton')
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
