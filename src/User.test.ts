import { expect } from 'jest';
import { User } from './User';

describe('User model', () => {
  it('should create a new user', async () => {
    const user = new User({ name: 'John Doe', email: 'johndoe@example.com', password: 'password' });
    await user.save();
    expect(user.name).toBe('John Doe');
    expect(user.email).toBe('johndoe@example.com');
    expect(user.password).not.toBe('password');
  });
});